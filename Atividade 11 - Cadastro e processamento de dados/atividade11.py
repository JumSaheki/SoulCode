import csv
import datetime
from modulos.postgres import Conector_postgres
import statistics as st
import numpy as np

'''
Trabalho em grupo da atividade 11

Ana Paula Guimarães Ribeiro
Bárbara Maria
Gustavo Simões
Jum Saheki
Ricardo Alex de Lima

'''


#Função que recebe e imprime uma mensagem e quando ela ocorreu 
def log(mensagem):
    data = datetime.datetime.now()
    print (f"{data}:{mensagem}")

if __name__ =="__main__":
    try:
        
         
          
        log("Preparando arquivo dados1.csv para carga...")
        with open('C:\\Users\\jumsa\\Documents\\Jum\\SoulCode\\Workspace\\Atividades\\atividade11\\dados\\DADOS1.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            dados1 = []
            for row in spamreader:
                dados1.append(row)
        dados1.pop(0)
        
    
        log("Preparando arquivo dados2.csv para carga...")
        with open('C:\\Users\\jumsa\\Documents\\Jum\\SoulCode\\Workspace\\Atividades\\atividade11\\dados\\DADOS2.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            dados2 = []
            for row in spamreader:
                dados2.append(row)
        dados2.pop(0)
        
        log("Preparando variável para unificar os arquivos dados1.csv e dados2.csv em uma única tabela")
        adiciona_index = len(dados1)
        log("adiciona_index criado")
        
        log("Removendo linhas que contém um dado vazio do arquivo dados1.csv...")
        new_dados = []
        for dado in dados1:
            if str(dado[1]) != '':
                if str(dado[2]) != '':
                    new_dados.append(dado)
        dados1 = new_dados
        log("Dados vazios removidos")
        
        log("Removendo linhas que contém um dado vazio do arquivo dados2.csv...")
        new_dados = []
        for dado in dados2:
            if str(dado[1]) != '':
                if str(dado[2]) != '':
                    new_dados.append(dado)
        dados2 = new_dados
        log("Dados vazios removidos")
        
        
        
        
        log("Conectando ao banco de dados...")
        banco = Conector_postgres('127.0.0.1','bc17')
        
       
        log("Criando tabela dados no banco...")        
        banco.inserir("CREATE TABLE IF NOT EXISTS dados\
            ( id serial,\
            data date,\
            valor decimal(10,2),\
            CONSTRAINT dados_pk PRIMARY KEY (id) );")
        log("Tabela 'dados' criada")
    
        log("Criando a tabela que receberá a média, mediana, moda, desvio_padrão, maior valor, menor valor, data inicial e data final...")
        banco.inserir("CREATE TABLE IF NOT EXISTS estatisticas\
            (num_bloco serial,\
            media decimal(10,2),\
            mediana decimal(10,2),\
            moda decimal(10,2),\
            desvio_padrao decimal(10,2),\
            valor_max integer,\
            valor_min integer,\
            data_inicial date,\
            data_final date,\
            constraint estatisticas_pk PRIMARY KEY (num_bloco));")
        log("Tabela 'estatisticas' criada")
        
               
        log("Criando tabelas, triggers e trigger functions para registrar todas as operações realizadas...")
        
        banco.inserir("CREATE TABLE IF NOT EXISTS log_dados(\
	                    cod_dados int not null,\
	                    data_log text not null,\
	                    operacao_realizada varchar not null\
                        );")
        
        banco.inserir("CREATE TABLE IF NOT EXISTS log_estatisticas(\
	                    cod_est int not null,\
	                    data_log text not null,\
	                    operacao_realizada varchar not null\
                        );")
        
        log("Tabelas de registro de logs criadas")
        
        
        log("Criando trigger function...")
        banco.inserir("CREATE OR REPLACE FUNCTION log_dados_func()\
                            RETURNS TRIGGER AS $$ BEGIN\
                                IF (TG_OP = 'INSERT') THEN INSERT INTO log_dados(cod_dados, data_log, operacao_realizada) VALUES (new.id, current_timestamp, 'Inserção');\
                                RETURN NEW;\
                                ELSIF (TG_OP = 'UPDATE') THEN INSERT INTO log_dados(cod_dados, data_log, operacao_realizada) VALUES (new.id, current_timestamp, 'Update. ' || new.id || ' foi alterado de: ' || OLD || 'para ' || new.* ||'.');\
                                RETURN NEW;\
                                ELSIF (TG_OP = 'DELETE') THEN INSERT INTO log_dados(cod_dados, data_log, operacao_realizada) VALUES (old.id, current_timestamp, 'Delete. ' || OLD || 'foi excluído.');\
                                RETURN OLD;\
                                END IF;\
                            RETURN NULL;\
                        END;\
                        $$ LANGUAGE 'plpgsql'")
        banco.inserir("CREATE OR REPLACE FUNCTION log_estatisticas_func()\
                            RETURNS TRIGGER AS $$ BEGIN\
                                IF (TG_OP = 'INSERT') THEN INSERT INTO log_estatisticas(cod_est, data_log, operacao_realizada) VALUES (new.num_bloco, current_timestamp, 'Inserção');\
                                RETURN NEW;\
                                ELSIF (TG_OP = 'UPDATE') THEN INSERT INTO log_estatisticas(cod_est, data_log, operacao_realizada) VALUES (new.num_bloco, current_timestamp, 'Update. ' || new.num_bloco || ' foi alterado de: ' || OLD || 'para ' || new.* ||'.');\
                                RETURN NEW;\
                                ELSIF (TG_OP = 'DELETE') THEN INSERT INTO log_estatisticas(cod_est, data_log, operacao_realizada) VALUES (old.num_bloco, current_timestamp, 'Delete. ' || OLD || 'foi excluído.');\
                                RETURN OLD;\
                                END IF;\
                            RETURN NULL;\
                        END;\
                        $$ LANGUAGE 'plpgsql'")
        log("Trigger function criadas")
        
        
        log("Criando os triggers...")
        banco.inserir("CREATE TRIGGER log_operacoes_dados\
                            AFTER INSERT OR UPDATE OR DELETE ON dados\
                                FOR EACH ROW EXECUTE PROCEDURE log_dados_func()")
        
        
        banco.inserir("CREATE TRIGGER log_operacoes_estatisticas\
                            AFTER INSERT OR UPDATE OR DELETE ON estatisticas\
                                FOR EACH ROW EXECUTE PROCEDURE log_estatisticas_func()")
        
        log("Triggers criados")
        
       
        
        log("Iniciando carga dos dados no banco")
        log("Recuperando variavel adiciona_index")
        
        log("Inserindo dados do arquivo dados1.csv na tabela dados...") 
        for i in dados1:
            banco.inserir("INSERT INTO dados(id, data, valor) VALUES ("+i[0]+",'"+i[1]+"',"+i[2]+")")
        log("Inserindo dados do arquivo dados2.csv na tabela dados...")
        for i in dados2:
            i[0] = int(i[0]) + adiciona_index
            i[0] = str(i[0])
            banco.inserir("INSERT INTO dados(id, data, valor) VALUES ("+i[0]+",'"+i[1]+"',"+i[2]+")")
              
        log("Fim do carregamento de dados")
        
        
      
        log("Ordenando as listas em ordem Cronológica")        
        lista_dados = banco.selecionar("Select * from dados order by data")
        log("Listas ordenadas")
        
        
        log("Separando a lista em blocos de 50...")     
        blocos = [lista_dados[x:x+50] for x in range(0, len(lista_dados), 50)]
        
        
          
        log("Iniciando os cálculos estatísticos")
        for i in range(len(blocos)):
            lista_valores = []
            for lista in blocos[i]:
                lista_valores.append(lista[2])
            
            log(f"Fazendo os cálculos estatísticos do {i+1}º bloco...")    
            media = np.mean(lista_valores)
            mediana = np.median(lista_valores)
            desvio_padrao = np.std(lista_valores)
            moda = st.mode(lista_valores)
            valor_max = np.max(lista_valores)
            valor_min = np.min(lista_valores)
            
            log(f"Encontrando data inicial e final do {i+1}º bloco...")
            data_inicial = str(blocos[i][0][1])
            if len(blocos[i]) < 50:
                data_final = str(blocos[i][22][1])
            else:
                data_final = str(blocos[i][49][1])
                
                
            log(f"inserindo valores do {i+1}º bloco na tabela...")
            banco.inserir(f"INSERT INTO estatisticas VALUES ({i}, {media}, {mediana}, {moda}, {desvio_padrao}, {valor_max}, {valor_min}, '{data_inicial}', '{data_final}')")
            log(f"Valores do {i+1}º bloco inseridos")
            print("-----------------------------------------------------------------")
              
           
        log("Dados inseridos")
        
        log("Fim do programa")
   
        
    except Exception as e :
        print(str(e))
        