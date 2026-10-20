"""Detecta novas releases dos mods registrados, compatíveis com o SPT alvo.
Cria uma Issue por mod+versão; não instala ou altera o catálogo automaticamente.
"""
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/mods/installed-spt-4.1.6.json").read_text(encoding="utf-8"))
SPT = DATA["environment"]["spt"]
REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")


def request(url, body=None, github=False):
    headers = {
        "Accept": "application/vnd.github+json" if github else "application/json",
        "User-Agent": "spt-tarkov-archive-mod-monitor/1.0",
    }
    if github and TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    payload = None if body is None else json.dumps(body).encode("utf-8")
    if payload:
        headers["Content-Type"] = "application/json"
    for attempt in range(3):
        req = urllib.request.Request(
            url, headers=headers, data=payload, method="POST" if payload else "GET"
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as err:
            if err.code in (429, 502, 503, 504) and attempt < 2:
                time.sleep(min(int(err.headers.get("Retry-After", "5")), 60))
                continue
            raise


def semver(s):
    m = re.fullmatch(r"v?(\d+)\.(\d+)\.(\d+)", str(s))
    return tuple(map(int, m.groups())) if m else None


def existing_issue_markers():
    markers = set()
    if not REPO:
        return markers
    page = 1
    while True:
        issues = request(
            f"https://api.github.com/repos/{REPO}/issues?state=all&per_page=100&page={page}",
            github=True,
        )
        for issue in issues:
            markers.update(re.findall(r"\[mod-release:[0-9]+:[^ \]\r\n]+\]", issue.get("body") or ""))
        if len(issues) < 100:
            break
        page += 1
    return markers


def main():
    known = existing_issue_markers()
    for mod in DATA["mods"]:
        params = urllib.parse.urlencode({
            "filter[spt_version]": SPT,
            "sort": "-version",
            "per_page": 50,
        })
        url = f"https://sp-mod.com/api/v0/mod/{mod['forge_id']}/versions?{params}"
        answer = request(url)
        versions = answer.get("data")
        if answer.get("success") is not True or not isinstance(versions, list):
            raise RuntimeError(f"Falha consultando versões de {mod['name']}")
        stable = [v for v in versions if semver(v.get("version")) is not None]
        if not stable:
            raise RuntimeError(f"Nenhuma release compatível encontrada para {mod['name']}")
        latest = max(stable, key=lambda v: semver(v["version"]))["version"]
        baseline = mod["forge_latest_compatible_baseline"]
        if semver(latest) <= semver(baseline):
            print(f"{mod['name']}: sem release superior à baseline {baseline} para {SPT}")
            continue
        marker = f"[mod-release:{mod['forge_id']}:{latest}]"
        if marker in known:
            print("Já existe Issue", marker)
            continue
        body = (
            f"{marker}\n\n**Mod:** {mod['name']}\n"
            f"**SPT de referência:** {SPT}\n"
            f"**Baseline:** {baseline}\n**Nova versão compatível publicada:** {latest}\n\n"
            f"**Fonte:** {mod['source_url']}\n\n"
            "Atenção: não confirma versão instalada nem segurança de atualizar.\n\n"
            "- [ ] Checar changelog/versão exata e dependências\n"
            "- [ ] Verificar interação com os demais mods\n"
            "- [ ] Fazer backup e testar antes de instalar\n"
            "- [ ] Registrar manualmente mudanças relevantes no catálogo\n"
        )
        if REPO:
            if not TOKEN:
                raise RuntimeError("GITHUB_TOKEN ausente")
            request(
                f"https://api.github.com/repos/{REPO}/issues",
                {"title": f"[SPT {SPT}] Revisar atualização de {mod['name']} para {latest}", "body": body},
                github=True,
            )
            known.add(marker)
        print("Nova release detectada:", mod["name"], latest)


if __name__ == "__main__":
    main()
