num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")


if operador == '+':
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operador == '-':
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operador == '*':
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operador == '/':
    
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")
else:
    print("Operador inválido. Por favor, use +, -, * ou /")
