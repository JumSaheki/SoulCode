'''
Documentação.

Classe atualizada e funcionando corretamente. 
Para utiliza-la, crie uma pasta chamada modules e coloque o nome do arquivo de funcionario.py

'''

class Funcionario:
    try:    
        def __init__(self, funcio_nome, funcio_telefone):
            self.func_nome = funcio_nome
            self.func_telefone = funcio_telefone
    except Exception as e:
            print(str(e))