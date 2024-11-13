N = int(input("Digite um número inteiro N: "))

# Laço para verificar e imprimir os números primos entre 1 e N
print(f"Números primos entre 1 e {N}:")
for num in range(2, N + 1):
    divisores = 0  # Variável para contar o número de divisores do número
    for i in range(1, num + 1):  # Verifica todos os divisores de num
        if num % i == 0:  # Se num for divisível por i
            divisores += 1  # Incrementa o contador de divisores
    if divisores == 2:  # Se o número tem exatamente dois divisores, é primo
        print(num, end=" ")
