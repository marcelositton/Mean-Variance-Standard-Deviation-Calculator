from mean_var_std import calculate

# Teste básico
try:
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print("Resultado do cálculo:")
    print(result)
except ValueError as e:
    print(f"Erro: {e}")
