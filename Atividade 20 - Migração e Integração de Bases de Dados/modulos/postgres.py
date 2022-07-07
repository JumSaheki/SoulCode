import psycopg2

class Conector_postgres:
    
    def __init__(self, host="127.0.0.1", db="postgres", user="postgres", password="postgres"):
        '''
        Configurações de acesso para um banco de dados postgres para a atividade 20 da SoulCode, iniciado em 20/05/2022
        '''
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
    
    def to_dataframe(self, query, columns_names):
        conn, cursor = self.conectar()
        cursor.execute(query)
        dados = cursor.fetchall()
        self.desconectar(conn, cursor)
        df = pd.DataFrame(dados, columns=columns_names)

def get_postgres_access():
    '''
    Função que retorna as informações de acesso para um banco de dados postgres utilizado para a realização de exercício da SoulCode
    O banco de dados está na nuvem e hospedado através do Heroku
    '''
    try:
        host = 'ec2-34-231-177-125.compute-1.amazonaws.com'
        database = 'd49ks53d6gehj9'
        user = 'iuykjkhonponce'
        password = '2349e85480c583ac2712c6339defafe103f201dd0713c6ff02057ce460d279ee'
        return host, database, user, password
    except Exception as e:
        print(str(e))


    