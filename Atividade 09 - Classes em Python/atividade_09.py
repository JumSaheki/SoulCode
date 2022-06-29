class Curso:
    #Método construtor com 5 atributos
    def __init__(self, instituicao_ensino, nome, formato, duracao_semanas:int, quantidade_alunos:int):
        try:
            #1 - Nome da instituição, pode ser uma escola, faculdade, universidade etc
            self.instituicao_ensino = instituicao_ensino
            
            #2 - Qual é o nome, exemplo: Engenharia de dados
            self.nome = nome
            
            #3 - Exemplo de formato: EAD, presencial, híbrido, bootcamp, workshop
            self.formato = formato
            
            #4 - Quantas semanas o curso dura
            self.duracao_semanas = duracao_semanas
            
            #5 - Numero de alunos que o curso tem
            self.quantidade_alunos = quantidade_alunos
        except Exception as e:
            print(str(e))
            
            
    #métodos Get        
    def get_instituicao_ensino(self):
        try:
            return self.instituicao_ensino
        except Exception as e:
            print(str(e))
            
    def get_nome(self):
        try:
            return self.nome
        except Exception as e:
            print(str(e))
            
    def get_formato(self):
        try:
            return self.formato
        except Exception as e:
            print(str(e))
            
    def get_duracao_semanas(self):
        try:
            return self.duracao_semanas
        except Exception as e:
            print(str(e))
            
    def get_quantidade_alunos(self):
        try:
            return self.quantidade_alunos
        except Exception as e:
            print(str(e))
            
            
    #métodos Set        
    def set_instituicao_ensino(self, instituicao_ensino):
        try:
            self.instituicao_ensino = instituicao_ensino   
        except Exception as e:
            print(str(e))
            
    def set_nome(self, nome):
        try:
            self.nome = nome   
        except Exception as e:
            print(str(e))
            
    def set_formato(self, formato):
        try:
            self.formato = formato   
        except Exception as e:
            print(str(e))
            
    def set_duracao_semanas(self, duracao_semanas:int):
        try:
            self.duracao_semanas = duracao_semanas   
        except Exception as e:
            print(str(e))
            
    def set_quantidade_alunos(self, quantidade_alunos:int):
        try:
            self.quantidade_alunos = quantidade_alunos
        except Exception as e:
            print(str(e))
