num1 = float(input("Insira um valor para calcular: "))
num2 = float(input("Insira mais um valor para calcular: "))

print("Selecione uma operação")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o numero da operação desejada:"))

if opcao == 1:
    resultado = num1 + num2
    print("O resultado da soma é: ", resultado)
elif opcao == 2:
    resultado = num1 - num2
    print("O resultado da subtração é: ", resultado)
elif opcao == 3:
    resultado = num1 * num2
    print("O reslutado da Multiplicação é: ", resultado)
elif opcao == 4:
    resultado = num1 % num2
    print("O resultado da Divisão é: ", resultado)




