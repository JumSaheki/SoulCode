
import random
from modulos.postgres import Conector_postgres


# popula_vendas("127.0.0.1","bc17", 2000)



def popula_vendas(host,db,num_loop:int):
    '''
    host - ip do banco ex:("127.0.0.1")
    db - nome do banco ex:("bc17")
    num_loop - número de inserts quer serão realizados na tabela 'vendas'. 
    A função automaticamente preenche a tabela de forma pseudo aleatória, prestando atenção em relação ao estoque
    '''
    try:
        #Conectando ao banco de dados
        banco = Conector_postgres(host,db)
        #Determina qual o produto com o maior estoque, max_qtd, e o utiliza como o maior número possivel para cada venda
        consulta_max_venda = banco.selecionar("SELECT MAX(quant_estoque) FROM produto")
        for i in consulta_max_venda:
            max_qtd = i[0]

        #Determina quantos registro(linhas) vão ser adicionadas na tabela de vendas.
        numero_loop = num_loop
        #Consulta o banco de dados para descobrir qual é a quantidade total de produtos em estoque
        consulta_estoque_total = banco.selecionar("SELECT SUM(quant_estoque) FROM produto")
        for i in consulta_estoque_total:
            estoque_total = i[0]
        #Verifica se o número de vendas será excessivo. A lógica é determinar a (média da quantidade e itens por venda) e multiplicar pelo (número de vendas) e esse valor não deve ser maior do que o (estoque)
        while numero_loop * (max_qtd/2) > estoque_total:
            print("Erro: É possível que o estoque não tenha o número suficiente para preencher a tabela. Diminua a quantidade de vendas realizadas")
            numero_loop = int(input("Digite um número menor para a quantidade de vendas realizadas: "))        
        j=0

        while j < numero_loop:
            print(2)
            #alocando id aleatórios para o vendedor
            id_vendedor = random.randint(1,1000)
            
            #Verifica se um item em específica ainda está em estoque. Se estiver zerado outro item será escolhido
            quant_estoque = 0            
            while quant_estoque == 0:
                id_produto = random.randint(1,2000)
                consulta_quant_estoque = banco.selecionar(f"SELECT quant_estoque FROM produto WHERE id_produto = {id_produto}")
                for i in consulta_quant_estoque:
                    quant_estoque = i[0]

            #número de produtos de cada venda. Usando para calcular o preço total
            qtd_prod_vendido = random.randint(1,500)
            #O número de produtos vendidos não pode superar a quantidade disponivel no estoque. A quantidade vendida é alterada para um valor inferior ao estoque
            while qtd_prod_vendido > quant_estoque:
                qtd_prod_vendido = random.randint(1,500)
          
            #atualiza o estoque e insere a informação no banco de dados
            estoque_atualizado = quant_estoque - qtd_prod_vendido
            banco.inserir(f"UPDATE produto SET quant_estoque = {estoque_atualizado} WHERE id_produto = {id_produto}")
            

            #chamando a função para encontrar o preço de um produto de acordo com o seu id. Também é preciso informar qual é o banco de dados utilizado e ter credenciais para o seu acesso
            consulta_preco = banco.selecionar(f"SELECT preco FROM produto where id_produto = {id_produto}")
            for i in consulta_preco:
                preco = i[0]
            print(preco)

            #Para obter o valor total é preciso multiplicar a quantidade de itens vendidos pelo preço
            valor_total = preco * qtd_prod_vendido
            #A comissão é de 8% do valor de venda
            comissao = 0.08
            #concatenando os valores para construir a query
            parte_query = "("+ str(id_produto) +","+ str(id_vendedor) +","+ str(valor_total) +","+ str(comissao)+")"

            banco.inserir("INSERT INTO vendas(id_produto, id_vendedor, valor_total, comissao) VALUES " + parte_query)
            
            j+=1
            
    except Exception as e:
        print(str(e))
        

# popula_vendas("127.0.0.1","bc17", 2000)
    
        
