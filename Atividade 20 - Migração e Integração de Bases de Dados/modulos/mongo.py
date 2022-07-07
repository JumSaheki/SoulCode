def get_mongo_access():
    '''
    Função que retorna as informações de acesso para um banco de dados Mongo Atlas utilizado para a realização de exercício da SoulCode
    '''
    try:
        connection_string = 'mongodb+srv://jumsaheki:TNh91tRlsPdDmKFS@cluster0.ap3gr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        db = 'soulcode'
        collection = 'atv20_bruto'
        return connection_string, db, collection        
    except Exception as e:
        print(str(e))