'''
Documentação.

Classe atualizada e funcionando corretamente. 
Para utiliza-la, crie uma pasta chamada modules e coloque o nome do arquivo de produto.py

'''

class Produto:
  
    try:
        def __init__(self, produto_nome, tipo_produto, produto_preco, qte_estoque):
            self.produto_nome = produto_nome
            self.tipo_produt = tipo_produto
            self.produto_preco = produto_preco
            self.qte_estoque = qte_estoque

    except Exception as e:
            print(str(e))