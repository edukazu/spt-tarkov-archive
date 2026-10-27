# ORBIT 3.0

| Campo | Registro |
|---|---|
| Presente na instalação | **Sim**, informado pelo usuário |
| Versão instalada | **Não confirmada** |
| Última versão compatível anunciada no Forge | **3.0.0** — SPT 4.1.6 |
| Data do release | **26/10/2026** |
| Baseline anterior | 2.1.1 (verificação de 20/10/2026) |
| Desenvolvedor | Chazut |
| GUID | `com.chazut.orbit` |

Fontes primárias: [ficha do Forge #2706](https://sp-mod.com/mod/2706/orbit-20) · [changelog completo 3.0.0](https://github.com/Chazut/ORBIT/releases/tag/3.0.0).

## O que mudou em 3.0.0

- **Objetivos de raid Rush:** perseguir spawns próximos, caçar bosses, buscar salas marcadas e destinos customizados.
- **Novos comportamentos de esquadrão:** posições de sniper, emboscadas, camp de extrações, rotas e pausas conforme personalidade, loot e regrouping.
- **Objetivos multi-etapa:** energia, interruptores, portas e leitores de keycard para locais como KIBA, ULTRA Medical, Saferoom, D-2, Hermetic e ZB-013.
- **Airdrops:** squads podem desviar, cobrir a área, saquear e retomar o plano.
- **Ghost Mode:** detecção ajustada por clima, visibilidade e equipamento; snipers Ghost podem detectar inimigos; bots nativos podem saquear corpos sem sair do modo em certas atividades; áudio de combate mais variado.
- **Desempenho:** planejamento, navegação, loot e logs divididos em trabalho menor ao longo dos frames para reduzir picos de CPU — o resultado continua dependente de mapa, bots, hardware e outros mods.
- **Configuração e diagnóstico:** ajustes por mapa, edição/criação de pontos Rush e Sniper, presets renomeáveis e ZIP de diagnóstico/replay.
- **Correções:** navegação, portas, loot, extrações, transições Ghost, bots presos e rotas bloqueadas.

## Dependências declaradas pelo Forge

- [SAIN](sain.md) **4.5.1**
- [Waypoints](waypoints.md) **1.9.0**
- [BigBrain](bigbrain.md) **1.5.0**

Essas versões continuam sendo as baselines publicadas para SPT 4.1.6. **As versões instaladas localmente ainda precisam ser confirmadas.**

## Atualização: compatibilidade e cautelas

O autor informa que presets e configurações existentes de **ORBIT 2.1 são preservados**, e novos campos recebem valores padrão. A instrução é instalar o **ZIP completo** com os componentes de cliente e servidor correspondentes; não há indicação de instalação limpa nem de apagar perfil para esta atualização.

!!! warning "Não atualizar às cegas"
    Faça backup do perfil, da pasta de configuração e dos presets. Depois, teste uma raid antes de adotar. Uma migração de presets preservada não garante que o comportamento novo será igual ao anterior.

### Interações com o nosso conjunto

- **SAIN:** dependência obrigatória. Se usar extrações do ORBIT, mantenha desativadas as extrações do SAIN para evitar duas lógicas de extração.
- **BigBrain + Waypoints:** dependências obrigatórias; mantenha as versões exigidas e verifique logs.
- **SVM:** ORBIT 3.0 suporta Scav Lands em Reserve quando SVM converte a saída em extração paga. Isso só importa se essa opção estiver habilitada.
- **Hardcore Rules:** revisar qualquer sobreposição de regras/economia separadamente; não há conflito específico declarado nas notas do ORBIT.
- **Vertical Hideout:** nenhuma interação direta indicada.
- **Looting Bots / Questing Bots:** candidatos ainda não instalados; podem sobrepor funções de loot/objetivos do ORBIT e precisam de testes próprios.

### Co-op (Fika)

O Fika Addon **1.2.0** é opcional e só é necessário em co-op. Se utilizado, o autor exige versões correspondentes no host/headless e em todos os clientes.

## Checklist para a instalação real

- [ ] Confirmar a versão local (não presumir que 3.0.0 já está instalada).
- [ ] Fazer backup de perfil, configurações e presets.
- [ ] Conferir SAIN extraction OFF caso ORBIT controle as extrações.
- [ ] Atualizar os componentes client/server juntos.
- [ ] Testar agressividade, rotas, loot, objetivos multi-etapa, extrações e desempenho.
- [ ] Registrar logs e observações antes de marcar a atualização como adotada.

**Estado:** release nova detectada e registrada; adoção local **pendente de decisão e teste**.
