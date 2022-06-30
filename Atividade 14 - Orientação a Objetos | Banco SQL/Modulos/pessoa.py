'''
Documentação.

Classe atualizada e funcionando corretamente. 
Para utiliza-la, crie uma pasta chamada modules e coloque o nome do arquivo de pessoa.py

'''
class Cliente:
    try:    
        def __init__(self, cliente_nome, cliente_cpf, cliente_telefone):
            self.cliente_nome = cliente_nome
            self.cliente_cpf = cliente_cpf
            self.cliente_telefone =  cliente_telefone
    except Exception as e:
            print(str(e))