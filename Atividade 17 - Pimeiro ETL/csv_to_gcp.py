import pandas as pd
from sqlalchemy import create_engine

if __name__ == "__main__":
    try:
        
        print("Criando a engine com os dados do DB")
        #o engine utiliza a biblioteca sqlalchemy para guardar as informações do banco de dados: 
        #   create_engine(tipo_de_db // nome_do_usuário : senha_do_db @ endereço:porta/ nome_do_db), 
        # a funçao cria um objeto que conversa com tipo de banco de dados indicado (ex: mysql, postgres, oracle, sql server etc, e passa os parâmetros de acesso)
        engine = create_engine('postgresql://postgres:xk5fMiHn74FDBw_@34.68.160.84:5432/soulcode')
        
        #utilizando o pandas para carregar o arquivo csv
        #A fonte original dos dados se encontra em https://basedosdados.org/dataset/br-ibge-pnad
        print("Carregando os dados do arquivo .csv para um dataframe")
        df  = pd.read_csv("C:\\Users\\jumsa\\Documents\\Jum\\SoulCode\\Workspace\\Atividades\\atividade17\\microdados_compatibilizados_domicilio.csv")

        # print("Iniciando tratamento de dados do Dataframe")
        #removendo as colunas que não serão utilizadas
        # df = df.drop(['id_regiao', 'id_uf', 'id_domicilio', 'regiao_metropolitana', 'conversor_moeda', 'renda_mensal_domiciliar_compativel_1992_deflacionado', 'aluguel_deflacionado', 'prestacao_deflacionado', 'peso_amostral', 'total_pessoas', 'total_pessoas_10_mais' ,'especie_domicilio', 'tipo_domicilio', 'possui_tv', 'renda_mensal_domiciliar_compativel_1992', 'aluguel', 'prestacao', 'deflator', 'tipo_parede', 'tipo_cobertura', 'tipo_esgoto', 'possui_sanitario', 'posse_domicilio', 'possui_filtro', 'possui_fogao', 'possui_geladeira', 'possui_radio', 'lixo_coletado', 'quantidade_comodos', 'quantidade_dormitorios', 'possui_sanitario_exclusivo', 'tipo_zona_domicilio','renda_mensal_domiciliar','renda_domicilio_deflacionado'], axis=1)

        #substituindo os valores das colunas de 0 para False e 1 para True
        rep_df = df.replace({1.0:True,0:False})
        
        #removendo as linhas vazias
        new_df = rep_df.fillna('Nulo', inplace = True)
        print("Fim do tratamento de dados")
        
        print("Inicio da carga de dados no DB")
        #fazendo a carga do dataframe para o db. Caso a tabela não exista ele cria uma
        #a utilização da biblioteca sqlachemy permite que a função to_sql() converse com os DBs suportados
        new_df.to_sql('tabela3',con=engine, if_exists='append', index_label = 'id_domicilio')
        
        print("Fim da carga de dados")

    except Exception as e:
        print(str(e))    