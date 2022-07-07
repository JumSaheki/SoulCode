from pymongo import MongoClient
import pandas as pd 

'''
programa utilizado para inserir arquivo .csv em um banco de dados Mongo db Atlas
'''

print('lendo csv')
df = pd.read_csv('C:\\Users\\jumsa\\Documents\\Jum\\SoulCode\\Workspace\Atividades\\atividade20_\\Sistema_B_NoSQL.csv',sep=',', encoding='utf-8')

print(df)
print('criando conexão com mongo')
client = MongoClient("mongodb+srv://jumsaheki:TNh91tRlsPdDmKFS@cluster0.ap3gr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client['soulcode']

collection = db['atv20_bruto']

print('to dict')
df_dict = df.to_dict("records")

collection.insert_many(df_dict)
print('fim')