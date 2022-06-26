def soma(x, y):
    return(x+y)

def mult(x, y):
    return(x*y)

def calculadora():
    print("Selecione uma operação")
    print("1-soma 2-subtacao 3-multiplicacao 4-divisao 0-sair")
    selecao = input("opcao: ")
    if selecao == "1":
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        print(soma(num1, num2))

calculadora()
