# SPT Tarkov Archive

Arquivo comunitário **não oficial** para preservar informações de gameplay conforme a build do *Escape from Tarkov* utilizada pelo SPT.

**Baseline inicial:** SPT 4.1.6 → EFT 0.16.9.5.40743. O catálogo ainda está em fase de coleta e verificação.

## Site

Depois de publicar via GitHub Pages: https://edukazu.github.io/spt-tarkov-archive/

## Desenvolvimento local

```bash
python -m pip install -r requirements.txt
mkdocs serve
```

## Publicação

Na aba **Settings → Pages**, selecione **GitHub Actions** como fonte. Um push para `main` executa o workflow de publicação.

## Regras editoriais

- Nunca usar a wiki **atual** como prova suficiente de comportamento da build histórica.
- Registrar build EFT, versão SPT, fonte, data de verificação e status de confiança.
- Não copiar textos extensos/imagens protegidas de terceiros; escrever resumos próprios com atribuição.
- Não publicar executáveis nem arquivos proprietários do jogo.
- Uma nova versão do SPT não modifica automaticamente o snapshot anterior.

## Licença

Conteúdo original sob CC BY 4.0 (ver `LICENSE`). Marcas e conteúdo de terceiros pertencem aos respectivos titulares.
