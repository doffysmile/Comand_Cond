# Calculadora com menu
opcao = -1
while opcao != 0:
    opcao = int(input("Escolha Uma Opção\n1-Soma  2-Subtracao  3-Multiplicacao  4-Divisao  0-Sair"))
    if opcao == 0:
        print("Sair")
    elif 1 <= opcao <= 4:
            a = float(input("Numero 1: "))
            b = float(input("Numero 2: "))

    if opcao == 1:
            print("Resultado:", a + b)
    elif opcao == 2:
            print("Resultado:", a - b)
    elif opcao == 3:
            print("Resultado:", a * b)
    elif opcao == 4:
        if b == 0:
            print("Erro: divisao por zero!")
        else:
            print("Resultado:", a / b)
    else:
        print("Opcao invalida!")

#