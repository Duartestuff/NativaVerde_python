import matplotlib.pyplot as plt
import pandas as pd

def crearGrafica(data, ciudad, ciudad_filename):

    data['Fecha'] = pd.to_datetime(data['Fecha'])

    aggregated_data = data.groupby('Fecha')['Arboles'].sum()

    aggregated_data

    plt.figure(figsize=(12, 6))
    plt.scatter(aggregated_data.index, aggregated_data.values, marker='o')
    plt.plot(aggregated_data.index, aggregated_data.values, color='skyblue', alpha=0.7)
    plt.xlabel('Fecha')
    plt.ylabel('Árboles sembrados')
    plt.title(f'Árboles sembrados en {ciudad}')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f'../graphics/{ciudad_filename}.png')