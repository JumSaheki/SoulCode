
import pandas as pd
from pymongo import MongoClient
import sqlalchemy
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

if __name__ == "__main__":
    try:
        # print("Lendo arquivo csv")
        #Lendo o arquivo csv da fonte e transformando em dataframe
        df = pd.read_csv("https://storage.googleapis.com/dadosbrutossca/ocorrencias.csv",delimiter=";",encoding="utf-8")
        
        print("Acessando o mongo")
        #Parametrizando a conexão para o mongo atlas
        client = MongoClient("mongodb+srv://jumsaheki:TNh91tRlsPdDmKFS@cluster0.ap3gr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        
        print("Nomeando o database")
        #Definindo o nome do database
        db = client['soulcode']
        
        print("Nomeando a collection")
        #Definindo o nome da collection
        collection = db['ocorrencias']
        
        
        
        print("Transformando o DataFrame em um dicionário")
        df_dict = df.to_dict("records")
        
        print("Inserindo os dados no MongoDB")
        collection.insert_many(df_dict)
        
        print("Extraindo dados do Mongo para tratamento")
        df_mongo = pd.DataFrame(list(db.ocorrencias.find({}, {'_id': False})))
        
        
        
        print("Iniciando tratamento de dados do Dataframe")
        
        df_mongo["ocorrencia_latitude"] = df_mongo["ocorrencia_latitude"].str.replace('\\','', regex=True)
        df_mongo["ocorrencia_latitude"] = df_mongo["ocorrencia_latitude"].str.replace("15° 39’ 00”S",'-15.65')
        df_mongo["ocorrencia_latitude"] = df_mongo["ocorrencia_latitude"].str.replace('t','')
        df_mongo["ocorrencia_latitude"] = df_mongo["ocorrencia_latitude"].str.replace('°','')
        df_mongo["ocorrencia_latitude"] = df_mongo["ocorrencia_latitude"].fillna('NÃO INFORMADO')
        
        df_mongo["ocorrencia_longitude"] = df_mongo["ocorrencia_longitude"].str.replace('\\','', regex=True)
        df_mongo["ocorrencia_longitude"] = df_mongo["ocorrencia_longitude"].str.replace("056° 07’ 03” W",'-56.1175')
        df_mongo["ocorrencia_longitude"] = df_mongo["ocorrencia_longitude"].str.replace('t','')
        df_mongo["ocorrencia_longitude"] = df_mongo["ocorrencia_longitude"].str.replace('°','')
        df_mongo["ocorrencia_longitude"] = df_mongo["ocorrencia_longitude"].str.replace("longitude: -43.","-43",regex=True)
        df_mongo["ocorrencia_longitude"] = df_mongo["ocorrencia_longitude"].str.replace("longitude: -47.","-47",regex=True)
        df_mongo["ocorrencia_longitude"] = df_mongo["ocorrencia_longitude"].fillna('NÃO INFORMADO')
        
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].str.replace('093-IG/CENIPA/2014','IG-093/CENIPA/2014')
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].str.replace('158/CENIPA/2016','A-158/CENIPA/2016')
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].str.replace('A-161/CNIPA/2013','A-161/CENIPA/2013')
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].str.replace('A-188CENIPA2013','A-188/CENIPA/2013')
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].str.replace('A-213CENIPA2013','A-213/CENIPA/2013')
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].str.replace('A-531CENIPA2015','A-531/CENIPA/2015')
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].str.replace('IG - 155/CENIPA/2017','IG-155/CENIPA/2017')
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].str.replace('A038/CENIPA/2018','A-038/CENIPA/2018')
        df_mongo["divulgacao_relatorio_numero"] = df_mongo["divulgacao_relatorio_numero"].fillna('NÃO INFORMADO')
        
        
        df_mongo["ocorrencia_cidade"] = df_mongo["ocorrencia_cidade"].fillna('NÃO INFORMADO')
        
        
        df_mongo["investigacao_aeronave_liberada"] = df_mongo["investigacao_aeronave_liberada"].fillna('NÃO INFORMADO')
        df_mongo["investigacao_aeronave_liberada"] = df_mongo["investigacao_aeronave_liberada"].str.replace('NULL','NÃO INFORMADO')
        
        df_mongo["investigacao_status"] = df_mongo["investigacao_status"].fillna('NÃO INFORMADO')
        df_mongo["investigacao_status"] = df_mongo["investigacao_status"].str.replace('NULL','NÃO INFORMADO')
        
    
        df_mongo["divulgacao_relatorio_publicado"] = df_mongo["divulgacao_relatorio_publicado"].fillna('NÃO INFORMADO')
        
        
        df_mongo["total_recomendacoes"] = df_mongo["total_recomendacoes"].fillna('NÃO INFORMADO')
        
        
        df_mongo["total_aeronaves_envolvidas"] = df_mongo["total_aeronaves_envolvidas"].fillna('NÃO INFORMADO')
        
        
        df_mongo["ocorrencia_saida_pista"] = df_mongo["ocorrencia_saida_pista"].fillna('NÃO INFORMADO')
  
        
        # Convertendo as colunas de data e hora para o formato do tipo Data. No arquivo as datas e horas estão misturados com texto
        df_mongo['ocorrencia_dia'] = pd.to_datetime(df_mongo['ocorrencia_dia'], format='%d/%m/%Y').dt.date
        df_mongo['ocorrencia_hora'] = pd.to_datetime(df_mongo['ocorrencia_hora'], format='%H:%M:%S').dt.time
        
        
        #Gerando insights
        graf = df_mongo["investigacao_status"].value_counts()
        graf2 = df_mongo["investigacao_aeronave_liberada"].value_counts()
        graf3 = df_mongo["divulgacao_relatorio_publicado"].value_counts()
        graf.plot(kind='pie')
        plt.show()
        graf2.plot(kind='pie')
        plt.show()
        graf3.plot(kind='pie')
        plt.show()
        
        
        print("Criando a conexão com o DB postgres")
        engine = create_engine('postgresql://postgres:postgres@34.68.160.84:5432/soulcode')
        
        
        print("Inicio da carga de dados no DB")
        #fazendo a carga do dataframe para o db. Caso a tabela não exista ele cria uma com o nome selecionado
        df_mongo.to_sql('mongo',con=engine, if_exists='replace',index=False, dtype={
            'codigo_ocorrencia': sqlalchemy.types.VARCHAR(length=8),
            'codigo_ocorrencia1': sqlalchemy.types.VARCHAR(length=8),
            'codigo_ocorrencia2': sqlalchemy.types.VARCHAR(length=8),
            'codigo_ocorrencia3': sqlalchemy.types.VARCHAR(length=8),
            'codigo_ocorrencia4': sqlalchemy.types.VARCHAR(length=8),
            'ocorrencia_dia': sqlalchemy.types.Date(),
            'ocorrencia_hora': sqlalchemy.types.Time(),
            'divulgacao_dia_publicacao': sqlalchemy.types.Date()
        })
        print("Dados carregados")
        
        

    except Exception as e:
        print(str(e))