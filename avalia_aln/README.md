# Documentação do Script de Avaliação de Sequências de Alinhamento

Este script é utilizado para identificar sequências de DNA que potencialmente prejudicam o alinhamento em arquivos no formato FASTA.

## Pré-requisitos

- Python 3
- Biblioteca Biopython
- NumPy

## Configuração

Antes de executar o script, você deve ter um arquivo de alinhamento no formato FASTA contendo todas as sequências de DNA que deseja analisar. Certifique-se de que as bibliotecas necessárias estão instaladas:

```bash
pip install biopython numpy
```

## Uso

1. Substitua o valor de `ALINHAMENTO_ARQUIVO` no cabeçalho do script pelo caminho do seu arquivo de alinhamento FASTA.

```python
ALINHAMENTO_ARQUIVO = "caminho/para/seu/arquivo/alinhamento.fasta"
```

2. Se desejar, ajuste os parâmetros `COMPRIMENTO_FATOR` e `GAP_FATOR` para mudar a sensibilidade na detecção de outliers.

```python
COMPRIMENTO_FATOR = 1.2  # Fator de comprimento da sequência
GAP_FATOR = 0.8          # Fator de gaps da sequência
```

3. Execute o script. As sequências que potencialmente estão prejudicando o alinhamento serão impressas na tela.

## Código do Script

```python
# Script para avaliação de sequências de alinhamento ...
# (Inclua o script completo aqui)
```

## Exemplo de Saída

```
Sequências que podem estar prejudicando o alinhamento:
seq_id_1
seq_id_2
...
```

## Autor

- Seu Nome (opcional)

## Licença
