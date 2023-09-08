# Script de Processamento de Arquivos FASTA

Este script permite processar múltiplos arquivos FASTA, combiná-los em um único arquivo, e realizar uma série de transformações nele, como limpeza e renomeação. Ele é útil em workflows de bioinformática que requerem a manipulação de sequências genômicas.

## Contexto

Este script é resultado da necessidade corriqueira de adaptar múltiplos fastas para o processo de alinhamento e posterior análise filogenética por programas com certas limitações quanto ao tamanho dos nomes, caracteres especiais e afins.
Dessa maneira, o script permite que o usuário combine múltiplos arquivos FASTA em um único arquivo, e realize uma série de transformações nele, como limpeza e renomeação de maneira RASTREÁVEL e AUDITÁVEL. Por isso são guardados os scripts intermediários de renomeação.
Ao fim ele também gera um script para renomear uma árvore filogenética baseado nos códigos do ncbi, caso o usuário deseje.

As premissas assumidas são:
- Você possui uma pasta com muitos arquivos fasta
- Estes arquivos estão nomeados conforme os códigos NCBI (ex: NC_000001.11.fasta)

## Requisitos

- bash
- awk
- sed
- grep

## Uso

Para usar o script, execute:

./script_name.sh <diretório_dos_fastas> <nome_do_fasta_final>

Onde:
- `<diretório_dos_fastas>` é o diretório contendo os arquivos FASTA que você deseja processar.
- `<nome_do_fasta_final>` é o nome que você deseja dar ao arquivo FASTA combinado.

## Funcionalidades

1. **Combinação**: Combina todos os arquivos FASTA do diretório especificado.
2. **Extração de Cabeçalhos**: Extrai e salva os cabeçalhos dos arquivos FASTA.
3. **Limpeza**: Realiza limpeza do arquivo FASTA, removendo certos caracteres especiais.
4. **Renomeação**: Renomeia sequências no arquivo FASTA.
5. **Renomeação de Árvore Filogenética**: Opcionalmente, cria um script para renomear uma árvore filogenética posteriormente, baseado nas sequências processadas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.