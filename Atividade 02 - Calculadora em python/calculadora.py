#TODO: completar calculadora, minimo 4 operacoes basicas, raiz e potencia
#TODO: desafio, calculadora cientifica
#TODO: desafio2, sem usar modulos

import math

def soma(x, y):
    return(x+y)

def mult(x, y):
    return(x*y)

def subt(x,y):
    return(x-y)

def div(x,y):
    return(x/y)

def raiz(x):
    return(math.sqrt(x))

def expon(x,y):
    return(x**y)

def calculadora():
    print("Selecione uma operação")
    print("1-soma 2-subtação 3-multiplicação 4-divisão 5-raiz quadrada 6-exponencial 0-sair")
    selecao = input("opcao: ")
    if selecao == "1":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(soma(num1, num2))
    elif selecao == "2":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(subt(num1, num2))
    elif selecao == "3":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(mult(num1, num2))
    elif selecao == "4":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero diferente de 0: "))
        while num2 == 0:
            print("Não divida por 0")
            num2 = float(input("Digite um numero diferente de 0: "))
        else:
            print(div(num1, num2))
    elif selecao == "5":
        num1 = float(input("Digite um numero: "))
        print(raiz(num1))
    elif selecao == "6":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(expon(num1, num2))
    else:
        print("Nenhuma operação selecionada")


calculadora()
