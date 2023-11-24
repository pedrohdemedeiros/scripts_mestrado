#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORTANTE: Antes de executar este script, certifique-se de que você tem um arquivo de alinhamento no formato FASTA.
# O arquivo deve conter todas as sequências de DNA que você deseja analisar.

# Insira o caminho para o seu arquivo de alinhamento FASTA abaixo.
# Exemplo: "caminho/para/seu/arquivo/alinhamento.fasta"
ALINHAMENTO_ARQUIVO = "insira_o_caminho_do_seu_arquivo.fasta"

# Se você deseja ajustar os parâmetros para identificar outliers, modifique os seguintes valores:
# Fator de comprimento de sequência (padrão é 1.2)
COMPRIMENTO_FATOR = 1.2
# Fator de gap de sequência (padrão é 0.8)
GAP_FATOR = 0.8

# Não modifique o script abaixo a menos que você entenda como ele funciona.
from Bio import AlignIO
import numpy as np

def evaluate_alignment_sequences(alignment_file):
    # Lê o alinhamento do arquivo FASTA
    alignment = AlignIO.read(alignment_file, "fasta")
    alignment_length = alignment.get_alignment_length()
    num_sequences = len(alignment)
    
    # Calcula o comprimento das sequências sem contar os gaps
    sequence_lengths = np.array([len(record.seq.ungap("-")) for record in alignment])
    # Conta o número de gaps em cada sequência
    gap_counts = np.array([record.seq.count('-') for record in alignment])

    # Calcula as médias de comprimento e de gaps do alinhamento
    average_length = np.mean(sequence_lengths)
    average_gaps = np.mean(gap_counts)

    # Identifica sequências que potencialmente prejudicam o alinhamento
    # Sequências consideradas outliers são mais longas e têm menos gaps que a média
    outlier_sequences = []
    for i, record in enumerate(alignment):
        sequence_length = sequence_lengths[i]
        gaps = gap_counts[i]
        if sequence_length > average_length * COMPRIMENTO_FATOR and gaps < average_gaps * GAP_FATOR:
            outlier_sequences.append(record.id)

    return outlier_sequences

# Exemplo de uso do script
outlier_sequences = evaluate_alignment_sequences(ALINHAMENTO_ARQUIVO)
print("Sequências que podem estar prejudicando o alinhamento:")
for seq_id in outlier_sequences:
    print(seq_id)
