'''
Algoritmo criado pelo professor Felipe.
A classe Conector_postgres possui métodos para criar e manipular dados em bancos de dados PostgreSQL
'''

import psycopg2

class Conector_postgres:
    
    def __init__(self, host, db, user="postgres", password="postgres"):
        try:
            self.host = host
            self.db = db
            self.user = user
            self.password = password
        except Exception as e:
            print(str(e))
    
    #conecta ao banco de dados        
    def conectar(self):
        conn = psycopg2.connect( host=self.host, database=self.db, user=self.user, password=self.password)
        cursor = conn.cursor()
        return conn, cursor
    
    #desconecta ao banco de dados, utilize depois de cada operações de inserção e/ou de consulta 
    def desconectar (self, conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()
    
    #insere os dados no banco de dados através de uma query. Por boas práticas ele se desconecta do banco após inserir os dados    
    def inserir(self, query):
        conn, cursor = self.conectar()
        cursor.execute(query)
        self.desconectar(conn, cursor)
    
    #realiza uma consulta no banco de dados através de uma query e retorna para o usuário. por boas práticas ele se desconecta do banco após a consulta
    def selecionar(self, query):
        conn, cursor = self.conectar()
        cursor.execute(query)
        dados = cursor.fetchall()
        self.desconectar(conn, cursor)
        lista_dados = []
        for dado in dados:
            lista_dados.append(dado)
        return lista_dados
            
    
