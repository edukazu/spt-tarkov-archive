# Monitoramento de atualizações

Mantemos um [inventário de mods em JSON](https://github.com/edukazu/spt-tarkov-archive/blob/main/data/mods/installed-spt-4.1.6.json) e uma [verificação diária](https://github.com/edukazu/spt-tarkov-archive/actions/workflows/check-mods.yml) via [API pública do Forge](https://sp-mod.com/developers).

A automação filtra releases por **SPT 4.1.6** e procura versões posteriores à baseline consultada em **20/10/2026**. Para cada novidade, abre uma [Issue de revisão](https://github.com/edukazu/spt-tarkov-archive/issues); não instala nem substitui nada automaticamente.

Uma versão nova destinada apenas a outra linha SPT não deve ser confundida com atualização elegível para nossa instalação. Antes de recomendar qualquer atualização, revisar changelog, dependências e conflitos (principalmente SAIN/ORBIT/BigBrain/Waypoints), migração e riscos de perfil (SVM/Hardcore Rules).

**Limitação:** sem os sete números de versão realmente instalados, o monitor detecta **novas publicações relativas à baseline**, não se a instalação local está atrasada. O Forge também oferece o endpoint `/mods/updates` para uso posterior após o inventário exato.
