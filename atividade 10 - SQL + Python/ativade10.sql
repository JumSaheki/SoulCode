CREATE TABLE IF NOT EXISTS fornecedor(
	id_fornecedor serial,
	nome VARCHAR(100),
	cnpj VARCHAR(30),
	
	CONSTRAINT fornecedor_pk PRIMARY KEY (id_fornecedor)
);

CREATE TABLE IF NOT EXISTS produto(
	id_produto serial,
	id_fornecedor integer,
	descricao VARCHAR(330),
	preco decimal(10,2),
	quant_estoque integer,
	
	CONSTRAINT produto_pk PRIMARY KEY (id_produto),
	CONSTRAINT produto_fk FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (id_fornecedor)
);

CREATE TABLE IF NOT EXISTS vendedor(
	id_vendedor serial,
	nome VARCHAR(50),
	cpf VARCHAR(30),
	endereco VARCHAR(50),
	telefone VARCHAR(30),
	
	CONSTRAINT vendedor_pk PRIMARY KEY (id_vendedor)
);

CREATE TABLE IF NOT EXISTS vendas(
	id_venda serial,
	id_produto integer,
	id_vendedor integer,
	valor_total decimal(10,2),
	comissao decimal(10,2),
	
	CONSTRAINT vendas_pk PRIMARY KEY (id_venda),
	CONSTRAINT vendas_fk FOREIGN KEY (id_produto) REFERENCES produto (id_produto),
	CONSTRAINT vendas_fk2 FOREIGN KEY (id_vendedor) REFERENCES vendedor (id_vendedor)
	);

-- delete from produto
-- delete from vendedor
-- delete from fornecedor
-- delete from vendas

-- drop table vendas
-- drop table produto
-- drop table vendedor
-- drop table fornecedor



--select * from fornecedor f, produto p, vendedor vdr, vendas v WHERE f.id_fornecedor = p.id_produto and v.id_produto = p.id_produto and v.id_vendedor = vdr.id_vendedor