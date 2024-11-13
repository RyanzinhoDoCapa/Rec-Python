n = int(input("Digite um número para a pirâmide: "))

# Gera a pirâmide
for i in range(1, n + 1):  # Para cada linha da pirâmide
    linha = ""  # Inicializa a variável para armazenar a linha
    for x in range(1, i + 1):  # Para cada número na linha
        linha += str(x) + " "  # Adiciona o número seguido de um espaço
    print(linha)  
