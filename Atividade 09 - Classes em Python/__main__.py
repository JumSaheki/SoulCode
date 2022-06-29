from atividade_09 import Curso

#Script criado para testar a atividade 09
if __name__ == "__main__":
    try:
        #instanciar um curso com valores errados
        soulcode = Curso("Sou Coe", "Engenho de dedos", "BooCamp", 365, 40000)

        #Teste dos métodos Get: printando valores errados:
        print(soulcode.get_instituicao_ensino())
        print(soulcode.get_nome())
        print(soulcode.get_formato())
        print(soulcode.get_duracao_semanas())
        print(soulcode.get_quantidade_alunos())
        
        #Teste dos métodos Set: alterando os valores para fazer a correção
        soulcode.set_instituicao_ensino("Soul Code")
        soulcode.set_nome("Engenharia de Dados")
        soulcode.set_formato("BootCamp")
        soulcode.set_duracao_semanas(12)
        soulcode.set_quantidade_alunos(50)
        
        #Verificação se os métodos Set fizeram a modificação com sucesso
        print("------------------------------------------")
        print(soulcode.get_instituicao_ensino())
        print(soulcode.get_nome())
        print(soulcode.get_formato())
        print(soulcode.get_duracao_semanas())
        print(soulcode.get_quantidade_alunos())
    except Exception as e:
        print(str(e))