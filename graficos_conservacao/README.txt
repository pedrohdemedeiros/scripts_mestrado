# Gráfico de Conservação de Sequências

Este script Python gera um gráfico de média móvel para escores de conservação de sequências de proteínas ou nucleotídeos. É parte de uma coleção de scripts desenvolvida durante o meu mestrado na Universidade Federal do ABC (UFABC).

## Requisitos

- Python 3.x
- NumPy
- Matplotlib

### Instalação de Dependências

Para instalar as bibliotecas necessárias, você pode executar o seguinte comando:

\```bash
pip install -r requirements.txt
\```

O arquivo `requirements.txt` contém:

\```
argparse==1.1
numpy==1.23.1
matplotlib==3.7.2
\```

## Como Usar

### 1. Prepare o arquivo de entrada

O arquivo de entrada deve ser um arquivo de texto que contém os escores de conservação. Cada linha deve representar um resíduo e seu escore de conservação.

### 2. Execute o script

Use o terminal para navegar até o diretório onde o script está localizado e execute o seguinte comando:

\```bash
python nome_do_script.py <file_path> <start> <end> <region_name> [--window_size <window_size>]
\```

#### Parâmetros

- `file_path`: Caminho para o arquivo que contém os escores de conservação.
- `start`: Posição inicial da região a ser destacada no gráfico.
- `end`: Posição final da região a ser destacada no gráfico.
- `region_name`: Nome da região a ser destacada.
- `window_size` (opcional): Tamanho da janela para calcular a média móvel. O valor padrão é 3.

### 3. Visualize o gráfico

O script irá gerar e exibir o gráfico de conservação.

### Exemplo de Uso

\```bash
python nome_do_script.py conservation_scores.txt 50 150 'Região Alfa' --window_size 5
\```

## Licença

Este script é liberado sob a licença Creative Commons Zero (CC0), o que efetivamente coloca este trabalho no domínio público. Você está livre para usar, modificar e distribuir este script para qualquer finalidade.
