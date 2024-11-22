import numpy as np

def calculate(input_list):
    # Verificar se a lista tem exatamente 9 elementos
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converter a lista para um array NumPy 3x3
    matrix = np.array(input_list).reshape(3, 3)

    # Calcular as métricas (média, variância, etc.) ao longo dos eixos e para a matriz achatada
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return calculations
