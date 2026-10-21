# Mods instalados — SPT 4.1.6

**Ambiente registrado:** SPT 4.1.6 · EFT 0.16.9.5.40743. Sete mods informados como instalados em 20/10/2026.

!!! important "Duas versões não são a mesma coisa"
    **Instalada** = arquivo no seu jogo; o número ainda não foi informado para os mods sem detalhe. **Última compatível anunciada** = release listada no Forge para SPT 4.1.6, consultada em 20/10/2026. Hardcore Rules tem uma alteração local descrita abaixo.

| Mod | Versão instalada | Última compatível no Forge | Fonte |
|---|---|---|---|
| [Server Value Modifier (SVM)](svm.md) | Não informada | 2.2.3 | [Forge](https://sp-mod.com/mod/236/server-value-modifier-svm) |
| [BigBrain](bigbrain.md) | Não informada | 1.5.0 | [Forge](https://sp-mod.com/mod/902/bigbrain) |
| [Waypoints — Expanded Navmesh](waypoints.md) | Não informada | 1.9.0 | [Forge](https://sp-mod.com/mod/827/waypoints-expanded-navmesh) |
| [SAIN — Solarint's AI Modifications](sain.md) | Não informada | 4.5.1 | [Forge](https://sp-mod.com/mod/791/sain-solarints-ai-modifications-full-ai-combat-system-replacement) |
| [ORBIT 2.0](orbit.md) | Não informada | 2.1.1 | [Forge](https://sp-mod.com/mod/2706/orbit-20) |
| [Vertical Hideout](vertical-hideout.md) | Não informada | 1.1.1 | [Forge](https://sp-mod.com/mod/2530/vertical-hideout) |
| [Hardcore Rules](hardcore-rules.md) | **3.1.0 + patch local “Wallet-only”** | 3.1.0 | [Forge](https://sp-mod.com/mod/784/hardcore-rules) |

A versão Wallet-only do Hardcore Rules é uma alteração local e **não** um release oficial. Para o comportamento confirmado, carteiras compatíveis, limite de suporte e status dos testes, consulte [Hardcore Rules](hardcore-rules.md).

## Como os mods se conectam

```text
BigBrain 1.5.0 ──────┐
                     ├── SAIN 4.5.1 ──┐
Waypoints 1.9.0 ─────┘                ├── ORBIT 2.0 2.1.1
BigBrain 1.5.0 ───────────────────────┤
Waypoints 1.9.0 ──────────────────────┘
```

A relação mostra as dependências **anunciadas**, não um inventário de arquivos. SAIN e ORBIT alteram comportamento de bots; SVM e Hardcore Rules podem alterar economia e progressão; Vertical Hideout altera interface.

## Regra editorial

Ao descrever uma missão, item, economia, rota de IA ou progressão, distinguir:

1. EFT **0.16.9.5.40743** (comportamento histórico).
2. SPT **4.1.6** (diferenças da implementação offline).
3. Plugins presentes e seus **presets/configurações**.
4. Verificações locais em jogo.

[Atualizações dos mods](updates.md) · [Candidatos complementares](recommendations.md)