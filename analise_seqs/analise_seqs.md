
# Análise de Sequências FASTA

Este repositório contém um script Python para análise de sequências FASTA, identificação de outliers com base no tamanho do arquivo e verificação de incongruências em sequências de aminoácidos e nucleotídeos.

## Características

- Identifica arquivos FASTA multifasta.
- Calcula estatísticas de tamanho de arquivo e identifica outliers.
- Verifica incongruências em sequências de aminoácidos e nucleotídeos.
- Gera gráficos de outliers.
- Produz relatórios detalhados de incongruências.

## Requisitos

- Python 3
- Biopython
- NumPy
- pandas
- Matplotlib

## Instalação

Para instalar as dependências, execute:

```bash
pip install biopython numpy pandas matplotlib
```

## Uso

Para executar o script:

```bash
python analise_seqs.py
```

## Configuração

No início do script, ajuste as seguintes variáveis conforme necessário:

- `DIRECTORY_PATH`: Caminho para o diretório contendo os arquivos FASTA.
- `OUTLIER_PERCENTAGE_THRESHOLD`: Limite percentual para considerar um arquivo um outlier.
- `SEQUENCE_TYPE`: Defina como 'nucleotide' ou 'aminoacid' dependendo do tipo de sequência.

## Funcionalidades

### Identificação de Multifasta

O script identifica e lista arquivos que contêm mais de uma sequência FASTA, considerados como multifasta.

### Análise de Outliers

Calcula a média do tamanho dos arquivos e identifica outliers com base em um limiar percentual definido pelo usuário.

### Verificação de Incongruências

Para sequências de aminoácidos, o script verifica a presença de stopcodons e aminoácidos faltantes (X).
Para sequências de nucleotídeos, verifica nucleotídeos faltantes (N) e nucleotídeos não padrão.

### Geração de Gráficos

Cria um gráfico de dispersão mostrando os outliers de tamanho de arquivo.

### Relatórios de Incongruências

Produz um relatório detalhado das incongruências encontradas em cada arquivo FASTA.

## Contribuições

Contribuições para este projeto são bem-vindas. Para contribuir, por favor, faça um fork do repositório, faça suas alterações e submeta um Pull Request.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.