# Script de Busca de Sequências

Este script busca sequências de proteínas no NCBI usando as ferramentas `esearch` e `efetch` do pacote E-utilities e salva os resultados em arquivos FASTA.
Você pode modificá-lo para baixar outros tipos de arquivos e acessar outras bases de dados. Para isso acesse o manual do [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK179288/)

## Pré-requisitos

Você precisará de um arquivo contendo uma lista de códigos do NCBI correspondentes a sua busca. Um códgo por linha, sem cabeçalho:

"
PNX93062
PNX87547
PNX86258
"

Antes de executar o script, certifique-se de ter as seguintes ferramentas instaladas:

### E-utilities do NCBI

O script utiliza as ferramentas `esearch` e `efetch` do pacote E-utilities do NCBI.

#### Instalação no Linux (Debian/Ubuntu):

```bash
sudo apt-get install ncbi-entrez-direct
```

#### Instalação no macOS (usando Homebrew):

```bash
brew install brewsci/bio/entrez-direct
```

#### Outras Plataformas:

Visite a página oficial do NCBI E-utilities para obter instruções de instalação: [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK179288/)

## Uso

1. Clone este repositório ou baixe o script.
2. Torne o script executável:

```bash
chmod +x baixa_fasta.sh
```

3. Execute o script fornecendo o arquivo de entrada e o diretório de saída:

```bash
./baixa_fasta.sh seu_arquivo_de_entrada.list seu_diretorio_de_saida
```


Por exemplo:

```bash
./baixa_fasta.sh novas_seqs.list novos_fastas
```

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests se tiver sugestões ou melhorias para este script.

