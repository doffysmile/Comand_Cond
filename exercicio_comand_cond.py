#1- Exercicio da Floresta

caminho = input("Escolha um caminho, entre direita e esquerda (em minusculo):")

if caminho == 'direita':
    atravessar = input("Você encontrou um rio, você quer atravessar ou voltar?")
    if atravessar == 'atravessar':
        print("Você chegou a uma vila")
    else:
        print("Você está perdido agora")
elif caminho == 'esquerda':
    subir = input("Você encontrou uma montanha, você quer subir ou voltar?")
    if subir == 'subir':
        print("Você encontrou um tesouro")
    else:
        print("Você está perdido agora")
else:
    print("Verifique se você escreveu a palavra corretamente, e em minusculo.")

#2 - Verificar o número

num = float(input("Informe um número:"))

if 10 <= num <=50:
    print("Seu número está entre 10 e 50")
elif num < 10:
    print("Seu número é menor que 10")
elif num > 50:
    print("Seu número é maior que 50")

#3 - Verificar se o ano é bissexto

ano = int(input("Insira o ano:"))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Seu ano é um ano Bissexto")
else:
    print("Seu ano não é um ano Bissexto")

#4 - Pedir usuario e senha

user = input("Você é admin ou convidado?(em minusculo:")

if user == 'admin':
    senha = input("Insira sua senha:")
    if senha == '1234':
        print("Bem-vindo")
    else:
        print("Sua senha está incorreta")
elif user == 'convidado':
    senha = input("Insira a senha:")
    if senha == '1234':
        print("Bem-vindo")
    else:
        print("Acesso restrito")

#5 - Peça coordenadas e informe se está ou não na fronteira

coord1 = float(input("Insira uma coordenada:"))
coord2 = float(input("Insira uma  segunda coordenada"))

if 0.0 <= coord1 <= 10.0 and 0.0 <= coord2 <= 10.0:
    if coord1 == 0.0 or coord1 == 10.0 or coord2 == 0.0 or coord2 == 10.0:
        print("Você está bem na borda")
    else:
        print("Você está dentro do quadrado")
else:
    print("Você está fora do quadrado")

#6 - Pedir tres lados de uma figura

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Sua figura é um triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Sua figura é um triângulo Isósceles")
    else:
        print("Sua figura é um triângulo Escaleno")
    lados = sorted([a, b, c])
    if lados[2] ** 2 == lados[0] ** 2 + lados[1] ** 2:
        print("Seu triângulo também é retângulo")

else:
    print("Sua figura não é um triângulo...")



