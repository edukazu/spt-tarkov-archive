# Hardcore Rules

| Campo | Registro |
|---|---|
| Presente na instalação | **Sim**, informado pelo usuário |
| Versão instalada | **3.1.0 + patch local “Wallet-only”**; não é um release oficial separado |
| Última compatível no Forge (20/10/2026) | **3.1.0** para SPT 4.1.6 |
| Desenvolvedor original | DanW |
| GUID | `com.danw.hardcorerules` |

[Consultar releases e notas originais no Forge](https://sp-mod.com/mod/784/hardcore-rules).

## Função original

Aplica regras de campanha hardcore e restrições à progressão/economia. A build documentada abaixo parte do Hardcore Rules 3.1.0, mas inclui uma alteração local no comportamento do container seguro.

## Build local personalizada — Wallet-only

**Esta instalação é diferente do release original do Forge.** O código base é Hardcore Rules 3.1.0 (SPT 4.1.6); a DLL local foi recompilada com um patch voltado a carteiras. O fonte-base utilizado está fixado no [commit upstream acd11d1](https://github.com/dwesterwick/SPTHardcoreRules/commit/acd11d139d3c8472047fe0f091985711111e7858).

Comportamento confirmado pelo usuário em jogo em **21/10/2026**:

- Permite guardar uma carteira com moedas dentro do container seguro.
- Permite colocar moedas na carteira enquanto ela está no container, inclusive arrastando-as sobre o ícone fechado.
- Bloqueia dinheiro solto no container.
- Bloqueia retirar moedas da carteira para espaços vazios do container seguro.
- As carteiras **Simple Wallet** (`5783c43d2459774bbe137486`) e **WZ Wallet** (`60b0f6c058e0b0481a09ad11`) foram incluídas e testadas.

**Limite conhecido:** outras carteiras ainda não foram verificadas. Não presumir compatibilidade até testá-las.

A build foi compilada localmente contra a instalação SPT do usuário. Este repositório registra a configuração e o comportamento observado, mas **não distribui a DLL modificada nem arquivos proprietários**. A alteração local não é uma versão oficial nem uma release mantida pelo autor original.

## Efeito sobre nosso catálogo

Pode conflitar com parâmetros do SVM. Há aviso de mudanças persistentes no perfil e opções próprias de flea market.

## Dependências anunciadas

Não há dependências obrigatórias listadas nas notas examinadas. Revalidar por release.

## Registro e verificações

- [x] Comportamento Wallet-only confirmado em jogo para Simple Wallet e WZ Wallet.
- [ ] Verificar outros tipos de carteira.
- [ ] Registrar configurações ativas do Hardcore Rules e do SVM.
- [ ] Separar efeitos de **EFT 40743**, **SPT 4.1.6** e **mods** ao documentar novos comportamentos.
- [ ] Registrar conflitos, performance e cuidados de atualização.

Fonte da release original: [Forge #784](https://sp-mod.com/mod/784/hardcore-rules), consultado em 2026-10-20. A seção Wallet-only descreve uma alteração local testada em 2026-10-21.