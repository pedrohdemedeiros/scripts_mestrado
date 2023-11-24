#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This Python script generates a plot for moving averages of conservation scores. 
# Este script Python gera um gráfico para médias móveis de escores de conservação.

import argparse  # Parsing command-line arguments
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting

# Function to read conservation scores from a given file
# Função para ler escores de conservação de um arquivo dado
def read_conservation_file(file_path):
    positions = []
    conservation_scores = []
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file.readlines()):
                if i < 4:
                    continue
                parts = line.strip().split('\t')
                pos = int(parts[0].split(':')[1])
                score = float(parts[1])
                positions.append(pos)
                conservation_scores.append(score)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)
    return np.array(positions), np.array(conservation_scores)

# Function to annotate regions on the plot
# Função para anotar regiões no gráfico
def annotate_regions(ax, start, end, region_name):
    ax.axvspan(start, end, color='#e0e0e0', alpha=0.5)
    ax.text((start + end) / 2, ax.get_ylim()[1] * 0.9, region_name, 
            horizontalalignment='center', verticalalignment='center')

# Parsing command-line arguments
# Analisando argumentos da linha de comando
parser = argparse.ArgumentParser(description='Generate conservation plots.')
parser.add_argument('file_path', type=str, help='Path to the conservation file.')
parser.add_argument('start', type=int, help='Start position of the region to highlight.')
parser.add_argument('end', type=int, help='End position of the region to highlight.')
parser.add_argument('region_name', type=str, help='Name of the region to highlight.')
parser.add_argument('--window_size', type=int, default=3, help='Window size for moving average.')
args = parser.parse_args()

# Reading the conservation scores
# Lendo os escores de conservação
positions, conservation_scores = read_conservation_file(args.file_path)

# Plotting
# Plotagem
fig, ax = plt.subplots(figsize=(12, 6))

# Calculate and plot the moving average
# Calcular e plotar a média móvel
moving_avg = np.convolve(conservation_scores, np.ones(args.window_size)/args.window_size, mode='valid')
ax.plot(positions[:-args.window_size+1], moving_avg, linestyle='-', color='#007acc', linewidth=2)

# Setting the title and labels
# Definindo o título e os rótulos
ax.set_title(f"Moving Average of Conservation (Window size: {args.window_size})")
ax.set_xlabel("Residue Position")
ax.set_ylabel("Average Conservation Score")

# Annotations and grid
# Anotações e grade
annotate_regions(ax, args.start, args.end, args.region_name)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Setting limits and ticks for the Y-axis
# Definindo limites e ticks para o eixo Y
ax.set_ylim([0.0, 1.0])
ax.set_xlim([0, 450])
ax.set_yticks(np.arange(0.0, 1.1, 0.2))

# Saving the plot as an SVG file
# Salvando o gráfico como um arquivo SVG
fig.savefig("Moving_Average_Plot.svg", format='svg')

# Showing the plot
# Exibindo o gráfico
plt.tight_layout()
plt.show()
