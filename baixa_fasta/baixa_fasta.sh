#!/bin/bash

# Verifica se as ferramentas necessárias estão instaladas
command -v esearch >/dev/null 2>&1 || { echo >&2 "esearch não encontrado. Por favor, instale E-utilities do NCBI."; exit 1; }
command -v efetch >/dev/null 2>&1 || { echo >&2 "efetch não encontrado. Por favor, instale E-utilities do NCBI."; exit 1; }

# Verifica se o número correto de argumentos foi fornecido
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <arquivo_de_entrada> <diretorio_de_saida>"
    exit 1
fi

ARQUIVO_ENTRADA="$1"
DIRETORIO_SAIDA="$2"

# Verifica se o arquivo de entrada existe
if [ ! -f "$ARQUIVO_ENTRADA" ]; then
    echo "Erro: Arquivo de entrada $ARQUIVO_ENTRADA não encontrado!"
    exit 1
fi

# Cria o diretório de saída se ele não existir
mkdir -p "$DIRETORIO_SAIDA"

# Processa cada sequência do arquivo de entrada
while IFS= read -r m; do
    esearch -db protein -query "$m" | efetch -format fasta > "$DIRETORIO_SAIDA/$m.fasta"
    if [ $? -ne 0 ]; then
        echo "Erro ao processar a sequência $m"
    fi
done < "$ARQUIVO_ENTRADA"
