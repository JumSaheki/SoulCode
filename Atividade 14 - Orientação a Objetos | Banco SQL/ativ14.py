
  
'''
Obs 01: criar uma pasta modules para criar os aquivos do banco e das classes separadamente.

Obs 02: o  comando abaixo função nativa do pandas utilizada para formatar todos os retornos do banco e traze-los como tabelas, pode ser útil no projeto

import pandas
df = pd.read_sql(query, conn)
print(df.head(26))

Obs 03: Menu criado testado e está funcionando, porem ao fazer uma query o python reporta um erro na classe postgres.

'''




'''
  Documentação do que foi feito:

  01:  foi aplicada uma correção em todas as classes, onde elas não estavam trazendo o resultado.

  02:  O Menu foi atualizado com todas as opções de inserts funcionando corretamente.

  03: Corrigido o problema das query insert into cliente

  04: corrigido o problema em que a query select não retornava os dados no terminal.

====================================================================================================================================================================================
  
  Documentação  do que precisa ser feito:

  Criar a rotina de testes para o reabastecimento do estoque.

  Criar uma função para a inserção múltipla dos dados


'''




#todos os imports necessários para rodar a aplicação
#Se não tiver a lib. tqdm, tem que rodar um pip para instalar "pip install tqdm"

import csv
from modules.pessoa import Cliente
from modules.funcionario import Funcionario
from modules.produto import Produto
from modules.postgres import Conector_postgres
import pandas as pd
from tqdm import tqdm
from os import system
from time import sleep

#limpando despoluindo o teminal
system('cls')




if __name__ =="__main__":
    try:
        banco = Conector_postgres(host="127.0.0.1", db="ATV14")
        cliente = Cliente
        funcionario = Funcionario
        produto = Produto
        
        
        #iniciando menu
        def menu():
                    
                    print('Carregando...')
                    print('===============================================================================================================================================================')
                    
                    #iniciando a barra de progresso.
                    for p in tqdm(range(5)):
                        sleep(1)
                    
                    sleep(1)
                    print('\n')
                    sleep(0.5)
                    print('==================================================================================')
                    sleep(0.5)
                    print('================      Bem vindo(a)       =========================================')
                    sleep(0.5)
                    print("================   Sistema PraQ? Admin   =========================================")
                    sleep(0.5)
                    print("==================================================================================")
                    sleep(0.5)
                    
                    #lista de opções
                    
                    print('Selecione uma opção abaixo: ')
                    sleep(0.1)
                    
                    #cadastrando cliente
                    print('1 - Cadastrar Cliente')
                    sleep(0.1)
                    
                    #cadastrando funcionario
                    print('2 - Cadastrar funcionario')
                    sleep(0.1)
                    
                    #cadastrando produto
                    print('3 - Cadastrar produto')
                    sleep(0.1)
                    
                    #cadastrando multiplos produtos
                    print('4 - inserir multiplos registros')
                    sleep(0.1)
                    
                    #carrinho de compras
                    print('5 - Carrinho')
                    sleep(0.1)
                    
                    #Listando todos clientes registrados no banco
                    print('6 - Consultar lista de clientes')
                    sleep(0.1)
                    
                    #Listando todos os funcionarios cadastrados no banco
                    print('7 - Consultar Funcionarios')
                    sleep(0.5)
                    
                    #Listando todos os produtos registrados no banco
                    print('8 - Consultar lista de Produtos')
                    sleep(0.1)
                    
                    #Listando todos os registros na tabela logs
                    print('9 - Consultar Registros')
                    sleep(0.1)
                    
                    #encerrando o sistema
                    print('0 - Sair do Sistema')
                    sleep(0.1)
                    print("================================================================================== \n")
                    
                    opcao: int = int(input("O que deseja fazer? "))
                    print('\n')
                    print("================================================================================== \n")
                    #criando a condição para rodar a opção selecionada
                    
                    #cadastrando cliente
                    if opcao == 1:
                        print('Digite o nome, cpf e telefone ')
                        print("================================================================================== \n")
                        sleep(1)
                        
                        #atributos sendo inseridos manualmente dentro da classe Pessoa.
                        cliente_nome = input('Digite o nome do cliente: ')
                        cliente_cpf = input('Digite o cpf: ')
                        cliente_telefone = input('Digite o telefone: ')
                        
                        print('"==================================================================================')
                        
                        #Alocando os inputs dentro da varíavel que contém a minha classe.
                        cliente(cliente_nome, cliente_cpf, cliente_telefone)
                        
                        #inserindo no banco o resultdado dos inputs
                        banco.inserir(f"INSERT INTO cliente (nome, cpf, telefone) VALUES ('{cliente_nome}', '{cliente_cpf}','{cliente_telefone}'); ")
                        sleep(2)
                        print('"==================================================================================')
                        print('Cliente Cadastrando com sucesso. \n')
                        print('Retornando ao menu principal...\n')
                        
                        #opção para cadastrar o funcionario
                    elif opcao == 2:
                        print('digite o nome e o telefone do funcionario.')
                        print("================================================================================== \n")
                        sleep(1)
                        
                        #gerando os inputs referentes a classe funcionario
                        funcio_nome = input('Digite o nome do funcionario: ')
                        funcio_telefone = input('Digite o telefone: ')
                        
                        #alocando o resultado dos inputs dentro da classe funcionario
                        funcionario(funcio_nome, funcio_telefone)
                        
                        #inserindo no banco o resultado dos inputs
                        banco.inserir(f"INSERT INTO funcionario (nome, telefone) VALUES ('{funcio_nome}','{funcio_telefone}'); ")
                        print("==================================================================================")
                        sleep(1.5)
                        print('Funcionario cadastrado com sucesso. \n')
                        print('Retornando ao menu principal...\n')
    
                        #cadastrando os produtos
                    elif opcao == 3:
                        print('Digite o nome, tipo do produto, preço, e a quantidade em estoque. ')
                        print("================================================================================== \n")
                        sleep(1)
                        
                        #criando os inputs dos produtos
                        produto_nome = input('Digite o nome do produto: ')
                        tipo_produto = input('Digite o tipo do produto: ')
                        produto_preco = input('Digite o valor desse produto: ')
                        qtde_estoque = input('Digite a quantidade a ser inserida no estoque: ')
                        
                        #alocando o resultado dos inputs dentro da classe produto
                        produto(produto_nome, tipo_produto, produto_preco, qtde_estoque)
                        
                        #inserindo o resultado dos inputs dentro do banco
                        banco.inserir(f"INSERT INTO produto (nome, tipo, preco, quant_estoque) VALUES ('{produto_nome}','{tipo_produto}','{produto_preco}','{qtde_estoque}'); ")
                        print("==================================================================================")
                        sleep(2)
                        print('Produto cadastrado com sucesso ')
                        print('Retornando ao menu principal...\n')

                    #Inserindo múltiplos dados através de arquivos no formato CSV.
                    elif opcao == 4:
                        csv1 = input('Insira o caminho do arquivo .csv ')
                        with open(csv1, newline='') as csvfile:
                            spamreader = csv.reader(csvfile, delimiter=',')
                            dados = []
                            for row in spamreader:
                                dados.append(row)
                        dados.pop(0)
                        print('Verificando o arquivo...')
                        sleep(3)
                        for i in tqdm(dados):
                            sleep(2)
                            df =pd.DataFrame(banco.inserir("INSERT INTO produto (nome, tipo, preco, quant_estoque) VALUES ("+i[0]+",'"+i[1]+"',"+i[2]+","+i[3]+")"))
                        sleep(1)
                        print('Todos os registros foram inseridos com sucesso.')


                    elif opcao == 5:
                        csv1 = input('Insira o caminho do arquivo .csv ')
                        with open(csv1, newline='') as csvfile:
                            spamreader = csv.reader(csvfile, delimiter=',')
                            dados = []
                            for row in spamreader:
                                dados.append(row)
                        dados.pop(0)
                        print('Verificando o arquivo...')
                        sleep(3)
                        for i in tqdm(dados):
                            sleep(2)
                            cod_prod = i[2]
                            quant_venda = i[5]
                            quant_estoque = banco.selecionar(f"SELECT quant_estoque FROM produto WHERE cod_produto = {cod_prod}")
                            if quant_estoque > quant_venda:
                                preco_prod = banco.selecionar(f"SELECT preco FROM produto WHERE cod_produto = {cod_prod}")
                                valor_total = preco_prod * quant_venda
                                df =pd.DataFrame(banco.inserir("INSERT INTO produto (cod_venda, cod_cliente, cod_produto, cod_funcionario, data_venda, quant_venda, valor_tot) VALUES ("+i[0]+",'"+i[1]+"',"+i[2]+","+i[3]+","+i[4]+","+i[5]+",'"+valor_total+"')"))
                                novo_estoque = quant_estoque - quant_venda
                                banco.inserir(f"UPDATE produto SET quant_estoque = {novo_estoque} WHERE cod_produto = {i[2]}")
                            else:
                                print("Não temos quantidade suficiente em estoque para realizar a venda")
                        sleep(1)
                        print('Todos os registros foram inseridos com sucesso.')
                    
                    
                    #listando todos os clientes
                    elif opcao == 6:
                        print('Carregando a lista de clientes...\n')
                        
                        #executando a barra de progresso
                        for p in tqdm(range(5)):
                            sleep(1)
                        
                        print('\n')
                        print("==================================================================================")
                        
                        #Executando a query e retornando os dados da tabela cliente via dataframe do pandas
                        df = pd.DataFrame(banco.selecionar(f"SELECT * FROM cliente "))
                        print(df)
                        print("==================================================================================")
                        print('\n')
                        sleep(2)
                        exit(0)
                    
                    #listando todos os vendedores    
                    elif opcao == 7:
                        print('Carregando a lista dos funcionarios... \n')
                        
                        # executando a barra de progressso
                        for p in tqdm(range(5)):
                            sleep(1)
                        print('\n')
                        print("==================================================================================")
                        
                        #Executando a query e retornando os dados da tabela funcionario via dataframe do pandas
                        df = pd.DataFrame(banco.selecionar(f"SELECT * FROM funcionario"))
                        print(df)
                        print("==================================================================================")
                        print('\n')
                        exit(0)
                    
                    #listando todos os produtos
                    elif opcao == 8:
                        print('Carregando a lista de produtos \n')
                        
                        #Executando a barra de progresso
                        for p in tqdm(range(5)):
                            sleep(1)
                        print('\n')
                        print("==================================================================================")
                        
                        #Executando a query e retornando os dados da tabela produto via dataframe do pandas
                        df = pd.DataFrame(banco.selecionar(f"SELECT * FROM produto"))
                        print(df)
                        print("==================================================================================")
                        print('\n')
                        exit(0)
                        
                        #listando todos os registros.
                    elif opcao == 9:
                        print('Abrindo a tabela de logs\n')
                        
                        #executando a barra de progresso.
                        for p in tqdm(range(5)):
                            sleep(1)
                        print('\n')
                        print("==================================================================================")
                        
                        #Executando a query e retornando os dados da tabela logs via dataframe do pandas
                        df = pd.DataFrame(banco.inserir(f"SELECT * FROM logs"))
                        print(df)
                        print("==================================================================================")
                        print('\n')
                        exit(0)
                    
                    #finalizando o menu
                    elif opcao == 0:
                        print('Ja vai tarde... \n')
                        sleep(2)
                        exit(0) 
                    
                    else:
                        print('Comando inválido! ')    
                        menu()

                   
                    

        #looping do menu
        menu()




            
    
    
    except Exception as e :
        print(str(e))
    