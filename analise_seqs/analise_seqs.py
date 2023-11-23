import os
from Bio import SeqIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configurações
DIRECTORY_PATH = 'fastas/'  # Caminho para o diretório com arquivos FASTA
OUTLIER_PERCENTAGE_THRESHOLD = 100  # Limite percentual para considerar um arquivo um outlier
SEQUENCE_TYPE = 'aminoacid'  # Opções: 'nucleotide' ou 'aminoacid'

# Função para calcular estatísticas dos tamanhos dos arquivos
def calculate_file_size_statistics(file_sizes):
    average_size = np.mean(file_sizes)
    return average_size

# Função para identificar outliers baseado no tamanho dos arquivos
def identify_file_size_outliers(file_sizes, file_names, average_size, percentage_threshold):
    threshold = average_size * (percentage_threshold / 100.0)
    outlier_data = [(file_names[i], size, abs(size - average_size)) 
                    for i, size in enumerate(file_sizes) if abs(size - average_size) > threshold]
    return sorted(outlier_data, key=lambda x: x[2], reverse=True)

# Função para imprimir tabela de outliers
def print_outliers_table(outlier_data):
    if outlier_data:
        print("\nTabela de Outliers:")
        df = pd.DataFrame(outlier_data, columns=['File Name', 'Length', 'Deviation from Mean'])
        print(df)
    else:
        print("Nenhum outlier encontrado.")

# Função para plotar gráfico de outliers
def plot_outliers(outlier_data):
    if outlier_data:
        plt.figure(figsize=(10, 6))
        for file_name, length, deviation in outlier_data:
            plt.scatter(file_name, length, c='red', label=file_name if 'Outlier' not in plt.gca().get_legend_handles_labels()[1] else "")
        plt.axhline(y=np.mean([length for _, length, _ in outlier_data]), color='grey', linestyle='--', label='Média')
        plt.xticks(rotation=90)
        plt.xlabel('Nome do Arquivo')
        plt.ylabel('Comprimento do Arquivo (bytes)')
        plt.title('Outliers de Tamanho de Arquivo')
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("Nenhum outlier para exibir no gráfico.")


# Função para verificar e contar incongruências nas sequências

def check_sequences(filepath, sequence_type):
    incongruences = {'stopcodons': 0, 'missing_aminoacids': 0, 'missing_nucleotides': 0, 'non_standard_nucleotides': set()}
    sequence_length = 0

    with open(filepath, 'r') as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            sequence = str(record.seq).upper()
            sequence_length += len(sequence)
            if sequence_type == 'aminoacid' and '*' in sequence:
                incongruences['stopcodons'] += sequence.count('*')
            if sequence_type == 'aminoacid' and 'X' in sequence:
                incongruences['missing_aminoacids'] += sequence.count('X')
            if sequence_type == 'nucleotide' and 'N' in sequence:
                incongruences['missing_nucleotides'] += sequence.count('N')
            if sequence_type == 'nucleotide':
                incongruences['non_standard_nucleotides'].update(set(sequence) - set("ATCG"))
    
    # Calcula a porcentagem de incongruências
    incongruences_count = sum(val for key, val in incongruences.items() if key != 'non_standard_nucleotides')
    if incongruences_count > 0:
        incongruences['percentage'] = (incongruences_count / sequence_length) * 100
        return incongruences
    else:
        return None


# ... (restante do script anterior) ...

# Execução do script
if __name__ == "__main__":
    file_sizes = []
    file_names = []
    multifasta_files = []

    # Verifica cada arquivo no diretório
    for filename in os.listdir(DIRECTORY_PATH):
        if filename.endswith(".fasta"):
            filepath = os.path.join(DIRECTORY_PATH, filename)
            sequence_count = sum(1 for _ in SeqIO.parse(filepath, "fasta"))
            if sequence_count > 1:
                multifasta_files.append(filename)
            elif sequence_count == 1:
                file_size = os.path.getsize(filepath)
                file_sizes.append(file_size)
                file_names.append(filename)

    # Imprime a lista de arquivos multifasta, se houver
    if multifasta_files:
        print("Arquivos multifasta encontrados:")
        for file in multifasta_files:
            print(file)
    else:
        print("Nenhum arquivo multifasta encontrado.")

    # Continua com a análise dos arquivos que não são multifasta
    if file_sizes:
        average_size = calculate_file_size_statistics(file_sizes)
        outlier_data = identify_file_size_outliers(file_sizes, file_names, average_size, OUTLIER_PERCENTAGE_THRESHOLD)
        print_outliers_table(outlier_data)
        plot_outliers(outlier_data)

        # Verificação adicional do conteúdo das sequências nos arquivos que não são outliers
        incongruences_report = {}
        for file, length, deviation in outlier_data:
            filepath = os.path.join(DIRECTORY_PATH, file)
            incongruences = check_sequences(filepath, SEQUENCE_TYPE)
            if incongruences:
                incongruences_report[file] = incongruences

        # Imprime relatório de incongruências, se houver
        if incongruences_report:
            print("\nRelatório de Incongruências:")
            for file, incongruences in incongruences_report.items():
                print(f"{file}: {incongruences}")
        else:
            print("Nenhuma incongruência encontrada nos arquivos analisados.")
    else:
        print("Nenhum arquivo FASTA válido para análise encontrado.")
