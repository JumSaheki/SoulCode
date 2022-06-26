#1) Crie um código que apresenta "Parabéns!" caso o usuário insira em sequência os números 1, 2, 3, e 4.

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))
num_4 = int(input("Digite o quarto número: "))

if (num_1 == 1 and num_2 == 2 and num_3 == 3 and num_4 == 4):
    print("Parabéns!")
else:
    print("Você digitou os números na sequência errada")

#2) Crie um código que pede nomes em sequencia, e apresenta a lista completa conforme o usuário digita.
i=0
lista = []
while i<3 :
    nome = input("Digite um nome: ")
    lista.append(nome) 
    print(lista)
    i += 1

#3) Crie um código em que o usuário digite o código de um estado e o computador apresente o estado por extenso. Ex: RJ > Rio de Janeiro

dicionario_estados = {
    "AC":"Acre",
    "AL":"Alagoas",
    "AP":"Amapá",
    "AM":"Amazonas",
    "BA":"Bahia",
    "CE":"Ceará",
    "DF":"Distrito Federal",
    "ES":"Espírito Santo",
    "GO":"Goiás",
    "MA":"Maranhão",
    "MT":"Mato Grosso",
    "MS":"Mato Grosso do Sul",
    "MG":"Minas Gerais",
    "PA":"Pará",
    "PB":"Paraíba",
    "PE":"Pernambuco",
    "PI":"Piauí",
    "RJ":"Rio de Janeiro",
    "RN":"Rio Grande do Norte",
    "RS":"Rio Grande do Sul",
    "RO":"Rondônia",
    "RR":"Roraima",
    "SC":"Santa Catarina",
    "SP":"São Paulo",
    "SE":"Sergipe",
    "TO":"Tocantins"
}

sigla = input("Digite a Sigla de um estado brasileiro: ")
estado = dicionario_estados.get(sigla.upper())
print("O nome completo do Estado é: ", estado)


#4) Crie um código que receba 2 números e resolva a potencia do primeiro ao segundo. Ex: 5², 3³, ...

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

calc_expoente = base**expoente

print("O número ", base, " elevado a ", expoente, " é igual a ", calc_expoente)

#5) Crie um código que conte por quantos segundos uma tecla é pressionada.

import time

tecla_1 = input("Pressione uma tecla: ")
inicio = time.time()
tecla_2 = input("Pressione a tecla novamente: ")
duracao = time.time() - inicio

print("O intervalo foi de ",duracao)

#6) Crie um código que receba em sequencia de produtos contendo nome de produto, descrição, preço e quantidade em estoque.
j=0
lista_produtos = []
while j<3:
    produto =[]
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto em estoque: "))
    produto.append(nome)
    produto.append(descricao)
    produto.append(preco)
    produto.append(quantidade)
    lista_produtos.append(produto)
    print(lista_produtos)
    j+=1 

#Desafios:
#1) Crie um código que receba uma matriz e calcule sua inversa.
#2) Crie um código que dado o símbolo de um elemento da tabela periódica, este retorne o elemento correspondente e suas informações.
