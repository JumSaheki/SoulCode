import pandas as pd
from modulos.postgres import Conector_postgres

if __name__ == "__main__":
    try:
        banco = Conector_postgres('127.0.0.1', 'atividade17')
        df  = pd.read_csv("C:\\Users\\jumsa\\Documents\\Jum\\SoulCode\\Workspace\\Atividades\\Atvidade17\\microdados_compatibilizados_domicilio.csv")
      
        df = df.drop(['id_regiao', 'id_uf', 'id_domicilio', 'regiao_metropolitana', 'conversor_moeda', 'renda_mensal_domiciliar_compativel_1992_deflacionado', 'aluguel_deflacionado', 'prestacao_deflacionado', 'peso_amostral', 'total_pessoas', 'total_pessoas_10_mais' ,'especie_domicilio', 'tipo_domicilio', 'possui_tv', 'renda_mensal_domiciliar_compativel_1992', 'aluguel', 'prestacao', 'deflator', 'tipo_parede', 'tipo_cobertura', 'tipo_esgoto', 'possui_sanitario', 'posse_domicilio', 'possui_filtro', 'possui_fogao', 'possui_geladeira', 'possui_radio', 'lixo_coletado', 'quantidade_comodos', 'quantidade_dormitorios', 'possui_sanitario_exclusivo', 'tipo_zona_domicilio','renda_mensal_domiciliar','renda_domicilio_deflacionado'], axis=1)
        
        rep_df = df.replace({1.0:True,0:False})
        new_df = rep_df.dropna()
        print(new_df)
        
        new_df.to_csv(r'C:\\Users\\jumsa\\Documents\\Jum\\SoulCode\\Workspace\\Atividades\\Atvidade17\\atividade17_full.csv', index = True)
        
        # lista = new_df.values.tolist()
       
        # for i in range(len(lista)):
        #     banco.inserir(f"INSERT INTO TABELA VALUES ({i},'{lista[i][0]}','{lista[i][1]}','{lista[i][2]}','{lista[i][3]}','{lista[i][4]}')")
        
        
        # l = [1982, 'AC', True, True, True, 40200.0, 2297.0]
        # banco.inserir(f"INSERT INTO TABELA VALUES (2,'{l[0]}','{l[1]}','{l[2]}','{l[3]}','{l[4]}','{l[5]}','{l[6]}')")

        print('fim')
    except Exception as e:
        print(str(e))    
        
# CREATE TABLE TABELA (
# 	id_ serial,
# 	ano integer,
# 	sigla_uf varchar(4),
# 	zona_urbana boolean,
# 	possui_agua_rede boolean,
# 	possui_iluminacao_eletrica boolean,
# CONSTRAINT id_pk PRIMARY KEY (id_)
# );






