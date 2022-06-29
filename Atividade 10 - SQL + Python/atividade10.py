from modulos.postgres import Conector_postgres

host = "127.0.0.1"
db = "bc17"
# exercicio_1(host,db)
# exercicio_2(host,db)
# exercicio_3(host,db)
# exercicio_4(host,db)
# exercicio_5(host,db)

def exercicio_1(host,db):
    '''
    host: ip do banco de dados (ex:'127.0.0.1')
    db: nome do banco de dados (ex: 'bc17')
    '''
    try:
        banco = Conector_postgres(host,db)
        #Encontra a soma da coluna de valor_total
        consulta_vendas = banco.selecionar("SELECT sum(valor_total) FROM vendas")
        #Extraindo o valor da consulta de dentro de uma tupla aninhada dentro de uma lista
        for i in consulta_vendas:
            total = i[0]
        print(f"O valor total das vendas é: R${total}")
        print("--------------------------------------------")
        print("--------------------------------------------")
    except Exception as e:
        print(str(e))
        
def exercicio_2(host,db):
    '''
    host: ip do banco de dados (ex:'127.0.0.1')
    db: nome do banco de dados (ex: 'bc17')
    '''
    try:
        banco = Conector_postgres(host,db)
        #Encontrar o maior valor
        consulta_valor = banco.selecionar("SELECT max(valor_total) FROM vendas")
        for i in consulta_valor:
            maior_valor = i[0]
        #Utilizando o maior valor para encontrar o nome do funcionario
        consulta_funcionario = banco.selecionar(f"SELECT vendedor.nome from vendas left join vendedor on vendas.id_vendedor = vendedor.id_vendedor where vendas.valor_total = {maior_valor}")
        print(consulta_funcionario)
        for i in consulta_funcionario:
            funcionario = i[0]
        print(f"A maior venda foi de R$ {maior_valor} realizada por {funcionario}")
        print("--------------------------------------------")
        print("--------------------------------------------")
    except Exception as e:
        print (str(e))
        
def exercicio_3(host,db):
    '''
    host: ip do banco de dados (ex:'127.0.0.1')
    db: nome do banco de dados (ex: 'bc17')
    '''
    try:
        banco = Conector_postgres(host,db)
        #Query que obtem o nome e q quantidade de vezes que o id de cada vendedor aparece
        consulta_repeticoes = banco.selecionar(f"SELECT vendedor.nome, COUNT(vendedor.id_vendedor) FROM vendas LEFT JOIN vendedor on vendas.id_vendedor = vendedor.id_vendedor GROUP BY vendedor.id_vendedor")
        repeticao = 0
        vendedor = []
        #Determinando qual é o maior número de repetições
        for i in consulta_repeticoes:
            if i[1] > repeticao:
                repeticao = i[1]
        #Determinando quais foram os vendedores que obtiveram o maior número de vendas
        for i in consulta_repeticoes:
            if i[1] == repeticao:
                vendedor.append(i[0])
        print(f"{vendedor} vederam mais com {repeticao} vendas")
        print("--------------------------------------------")
        print("--------------------------------------------")    
    except Exception as e:
        print(str(e))
        

        
def exercicio_4(host,db):
    '''
    host: ip do banco de dados (ex:'127.0.0.1')
    db: nome do banco de dados (ex: 'bc17')
    '''
    try:
        banco = Conector_postgres(host,db)
        #Obtem o nome e a quantidade de vezes que cada fornecedor aparece
        consulta_fornecedor = banco.selecionar("SELECT count(fornecedor.id_fornecedor), fornecedor.nome from vendas left join produto on vendas.id_produto = produto.id_produto left join fornecedor on produto.id_fornecedor = fornecedor.id_fornecedor GROUP BY fornecedor.id_fornecedor")
        repeticao = 0
        fornecedor = []
        #Determina qual é o maior número de repetições que um fornecedor apareceu
        for i in consulta_fornecedor:
            if i[0] > repeticao:
                repeticao = i[0]
        #Determina quais fornecedores que obtiveram o maior numero de repetições
        for i in consulta_fornecedor:
            if i[0] == repeticao:
                fornecedor.append(i[1])
        print(f"{fornecedor} são os fornecedores mais utilizados ")
        print("--------------------------------------------")
        print("--------------------------------------------")
    except Exception as e:
        print(str(e))


def exercicio_5(host,db):
    '''
    host: ip do banco de dados (ex:'127.0.0.1')
    db: nome do banco de dados (ex: 'bc17')
    '''
    try:
        banco = Conector_postgres(host,db)
        #Obtem o nome do vendedor e qual o soma as vendas de um
        consulta_comissao = banco.selecionar("SELECT  vendedor.nome, sum(vendas.valor_total) FROM VENDAS LEFT JOIN vendedor ON vendas.id_vendedor = vendedor.id_vendedor GROUP BY vendedor.nome")
        comissao_porcentagem = 0.08
        #Cálculo de comissão de cada vendedor
        for i in consulta_comissao:
            vendedor = i[0]
            #Conversão para float para possibilitar o cálculo da porcentagem
            venda = float(i[1]) * comissao_porcentagem
            #Arredondando para duas casas decimais depois da vírgula
            comissao = round(venda,2)
            print(f"{vendedor} tem R$ {comissao} de comissão a receber")
        
        
    except Exception as e:
        print(str(e))        
        
def imprime_vendas(host, db):
    try:
        banco = Conector_postgres(host,db)
        consulta_venda = banco.selecionar("SELECT * FROM vendas")
        for i in consulta_venda:
            print(i)
    except Exception as e:
        print(str(e))
    
imprime_vendas(host,db)