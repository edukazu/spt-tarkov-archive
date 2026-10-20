"""Create one GitHub issue when the upstream latest version changes.
Requires GITHUB_TOKEN and GitHub Actions permission to create issues.
"""
import json
import os
import re
import urllib.request
from pathlib import Path

API = "https://api.github.com/repos/SP-Tushonka/build/releases/latest"
BASE = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((BASE / "data/version-manifest.json").read_text(encoding="utf-8"))
CURRENT = MANIFEST["reference_version"]

def request(url, method="GET", payload=None):
    headers={"Accept":"application/vnd.github+json", "User-Agent":"spt-tarkov-archive"}
    token=os.environ.get("GITHUB_TOKEN")
    if token: headers["Authorization"]="Bearer "+token
    if payload is not None:
        headers["Content-Type"]="application/json"
        payload=json.dumps(payload).encode()
    req=urllib.request.Request(url, data=payload, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=20) as resp: return json.load(resp)

latest=request(API)
tag=(latest.get("tag_name") or "").lstrip("vV")
version_match=re.search(r"\d+\.\d+\.\d+",tag)
if not version_match:
    print("Não foi possível obter versão semântica de release:", tag)
    raise SystemExit(0)
version=version_match.group(0)
if tuple(map(int,version.split('.'))) <= tuple(map(int,CURRENT.split('.'))):
    print("Sem versão superior à referência", CURRENT)
    raise SystemExit(0)
repo=os.environ.get("GITHUB_REPOSITORY")
if not repo:
    print("Versão superior detectada:",version)
    raise SystemExit(0)
issues=request(f"https://api.github.com/repos/{repo}/issues?state=all&per_page=100")
marker=f"[release-detected:{version}]"
if any(marker in (i.get('body') or '') for i in issues):
    print("Já registrada:",version)
    raise SystemExit(0)
body=(f"{marker}\n\nNova versão upstream encontrada: **{version}**\n\n"
      f"Fonte: {latest.get('html_url','')}\n\n"
      "Checklist editorial:\n- [ ] Conferir versão EFT requerida\n- [ ] Confirmar release estável\n"
      "- [ ] Avaliar compatibilidade de mods e perfis\n- [ ] Analisar diferenças com o snapshot atual\n"
      "- [ ] Criar novo snapshot somente se a build EFT mudar\n- [ ] Atualizar manifest após revisão\n")
request(f"https://api.github.com/repos/{repo}/issues", "POST", {"title":f"Verificar release SPT {version}","body":body})
print("Issue criada para",version)
