CREATE TABLE TABELA (
	id_ serial,
	ano int,
	sigla_uf varchar(4),
	zona_urbana boolean,
	possui_agua_rede boolean,
	possui_iluminacao_eletrica boolean,
CONSTRAINT id_pk PRIMARY KEY (id_)
);

--TESTANDO OS DADOS
SELECT * FROM TABELA;
SELECT DISTINCT sigla_uf FROM TABELA ORDER BY sigla_uf;

--CONTANDO OS DADOS DE ILUMINACAO POR ESTADO
SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, sigla_uf  FROM TABELA WHERE possui_iluminacao_eletrica = TRUE GROUP BY sigla_uf ORDER BY sigla_uf;
SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, sigla_uf  FROM TABELA WHERE possui_iluminacao_eletrica = FALSE GROUP BY sigla_uf ORDER BY sigla_uf;
SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, sigla_uf  FROM TABELA GROUP BY sigla_uf ORDER BY sigla_uf;
SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, ano  FROM TABELA WHERE possui_iluminacao_eletrica = FALSE GROUP BY ano ORDER BY ano;


--CONTANDO OS DADOS DE AGUA POR ESTADO
SELECT COUNT(possui_agua_rede), sigla_uf AS agua FROM TABELA WHERE possui_agua_rede = TRUE GROUP BY sigla_uf ORDER BY sigla_uf;
SELECT COUNT(possui_agua_rede), sigla_uf AS agua FROM TABELA WHERE possui_agua_rede = FALSE GROUP BY sigla_uf ORDER BY sigla_uf;


--CONTANDO OS DADOS DE ILUMINACAO E DE AGUA POR ESTADO
SELECT COUNT(possui_iluminacao_eletrica), sigla_uf AS iluminacao_e_agua FROM TABELA WHERE possui_iluminacao_eletrica = TRUE AND possui_agua_rede = TRUE GROUP BY sigla_uf ORDER BY sigla_uf;
SELECT COUNT(possui_iluminacao_eletrica), sigla_uf AS iluminacao_e_agua FROM TABELA WHERE possui_iluminacao_eletrica = FALSE AND possui_agua_rede = FALSE GROUP BY sigla_uf ORDER BY sigla_uf;


--CRIANDO VIEWS PARA ILUMINACAO
CREATE VIEW ILUMINACAO AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, sigla_uf FROM TABELA WHERE possui_iluminacao_eletrica = FALSE GROUP BY sigla_uf ORDER BY sigla_uf;
CREATE VIEW ILUMINACAOTOTAL AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, sigla_uf FROM TABELA GROUP BY sigla_uf ORDER BY sigla_uf;
--VIEW TOP 3 PIORES ESTADOS POR ANO
CREATE VIEW ILUMINACAO_ANO_MA AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, ano FROM TABELA WHERE possui_iluminacao_eletrica = FALSE and sigla_uf = 'MA' GROUP BY ano ORDER BY ano;
CREATE VIEW ILUMINACAO_ANO_PI AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, ano FROM TABELA WHERE possui_iluminacao_eletrica = FALSE and sigla_uf = 'PI' GROUP BY ano ORDER BY ano;
CREATE VIEW ILUMINACAO_ANO_MT AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, ano FROM TABELA WHERE possui_iluminacao_eletrica = FALSE and sigla_uf = 'MT' GROUP BY ano ORDER BY ano;
CREATE VIEW ILUMINACAO_ANO_TOTAL_MA AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, ano FROM TABELA WHERE sigla_uf = 'MA' GROUP BY ano ORDER BY ano;
CREATE VIEW ILUMINACAO_ANO_TOTAL_PI AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, ano FROM TABELA WHERE sigla_uf = 'PI' GROUP BY ano ORDER BY ano;
CREATE VIEW ILUMINACAO_ANO_TOTAL_MT AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao, ano FROM TABELA WHERE sigla_uf = 'MT' GROUP BY ano ORDER BY ano;


--CRIANDO VIEWS PARA AGUA
CREATE VIEW AGUA AS SELECT COUNT(possui_agua_rede) AS agua, sigla_uf FROM TABELA WHERE possui_agua_rede = FALSE GROUP BY sigla_uf ORDER BY sigla_uf;
CREATE VIEW AGUATOTAL AS SELECT COUNT(possui_agua_rede) AS agua, sigla_uf FROM TABELA GROUP BY sigla_uf ORDER BY sigla_uf;
--VIEW TOP 3 PIORES ESTADOS POR ANO
CREATE VIEW AGUA_ANO_RO AS SELECT COUNT(possui_agua_rede) AS agua, ano FROM TABELA WHERE possui_agua_rede = FALSE and sigla_uf = 'RO' GROUP BY ano ORDER BY ano;
CREATE VIEW AGUA_ANO_MA AS SELECT COUNT(possui_agua_rede) AS agua, ano FROM TABELA WHERE possui_agua_rede = FALSE and sigla_uf = 'MA' GROUP BY ano ORDER BY ano;
CREATE VIEW AGUA_ANO_AC AS SELECT COUNT(possui_agua_rede) AS agua, ano FROM TABELA WHERE possui_agua_rede = FALSE and sigla_uf = 'AC' GROUP BY ano ORDER BY ano;
CREATE VIEW AGUA_ANO_TOTAL_RO AS SELECT COUNT(possui_agua_rede) AS agua, ano FROM TABELA where sigla_uf = 'RO' GROUP BY ano ORDER BY ano;
CREATE VIEW AGUA_ANO_TOTAL_MA AS SELECT COUNT(possui_agua_rede) AS agua, ano FROM TABELA where sigla_uf = 'MA' GROUP BY ano ORDER BY ano;
CREATE VIEW AGUA_ANO_TOTAL_AC AS SELECT COUNT(possui_agua_rede) AS agua, ano FROM TABELA where sigla_uf = 'AC' GROUP BY ano ORDER BY ano;


--CRIANDO VIEWS PARA AGUA E ILUMINACAO
CREATE VIEW AGUAEENERGIA AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao_e_agua, sigla_uf FROM TABELA WHERE possui_iluminacao_eletrica = FALSE AND possui_agua_rede = TRUE GROUP BY sigla_uf ORDER BY sigla_uf;
CREATE VIEW AGUAEENERGIATOTAL AS SELECT COUNT(possui_iluminacao_eletrica) AS iluminacao_e_agua, sigla_uf FROM TABELA GROUP BY sigla_uf ORDER BY sigla_uf;


--TESTANDO AS VIEWS
SELECT * FROM ILUMINACAO;
SELECT * FROM ILUMINACAOTOTAL;
SELECT * FROM ILUMINACAO_ANO_MA;
SELECT * FROM ILUMINACAO_ANO_MT;
SELECT * FROM ILUMINACAO_ANO_PI;
SELECT * FROM ILUMINACAO_ANO_TOTAL_MA;
SELECT * FROM ILUMINACAO_ANO_TOTAL_MT;
SELECT * FROM ILUMINACAO_ANO_TOTAL_PI;

SELECT * FROM AGUA;
SELECT * FROM AGUATOTAL;
SELECT * FROM AGUA_ANO_AC;
SELECT * FROM AGUA_ANO_MA;
SELECT * FROM AGUA_ANO_RO;
SELECT * FROM AGUA_ANO_TOTAL_AC;
SELECT * FROM AGUA_ANO_TOTAL_MA;
SELECT * FROM AGUA_ANO_TOTAL_RO;

SELECT * FROM AGUAEENERGIA;


--GERANDO INFORMAÇÕES PARA AS TABELAS
SELECT I.sigla_uf, ROUND( ((CAST (I.ILUMINACAO AS DECIMAL(10,2))) / (CAST (T.ILUMINACAO AS DECIMAL(10,2))) * 100), 2 ) as porcentagem FROM ILUMINACAO I, ILUMINACAOTOTAL T WHERE T.sigla_uf = I.sigla_uf order by porcentagem desc;
SELECT I.ano, ROUND( ((CAST (I.ILUMINACAO AS DECIMAL(10,2))) / (CAST (T.ILUMINACAO AS DECIMAL(10,2))) * 100), 2 ) as porcentagem FROM ILUMINACAO_ANO_MA I, ILUMINACAO_ANO_TOTAL_MA T WHERE T.ano = I.ano order by ano asc;
SELECT I.ano, ROUND( ((CAST (I.ILUMINACAO AS DECIMAL(10,2))) / (CAST (T.ILUMINACAO AS DECIMAL(10,2))) * 100), 2 ) as porcentagem FROM ILUMINACAO_ANO_PI I, ILUMINACAO_ANO_TOTAL_PI T WHERE T.ano = I.ano order by ano asc;
SELECT I.ano, ROUND( ((CAST (I.ILUMINACAO AS DECIMAL(10,2))) / (CAST (T.ILUMINACAO AS DECIMAL(10,2))) * 100), 2 ) as porcentagem FROM ILUMINACAO_ANO_MT I, ILUMINACAO_ANO_TOTAL_MT T WHERE T.ano = I.ano order by ano asc;


SELECT I.sigla_uf, ROUND( ((CAST (I.AGUA AS DECIMAL(10,2))) / (CAST (T.AGUA AS DECIMAL(10,2))) * 100), 2 ) as porcentagem FROM AGUA I, AGUATOTAL T WHERE T.sigla_uf = I.sigla_uf order by porcentagem desc;
SELECT I.ANO, ROUND( ((CAST (I.AGUA AS DECIMAL(10,2))) / (CAST (T.AGUA AS DECIMAL(10,2))) * 100), 2 ) as porcentagem FROM AGUA_ANO_RO I, AGUA_ANO_TOTAL_RO T WHERE T.ano = I.ano order by ano asc;
SELECT I.ANO, ROUND( ((CAST (I.AGUA AS DECIMAL(10,2))) / (CAST (T.AGUA AS DECIMAL(10,2))) * 100), 2 ) as porcentagem FROM AGUA_ANO_MA I, AGUA_ANO_TOTAL_MA T WHERE T.ano = I.ano order by ano asc;
SELECT I.ANO, ROUND( ((CAST (I.AGUA AS DECIMAL(10,2))) / (CAST (T.AGUA AS DECIMAL(10,2))) * 100), 2 ) as porcentagem FROM AGUA_ANO_AC I, AGUA_ANO_TOTAL_AC T WHERE T.ano = I.ano order by ano asc;


SELECT I.sigla_uf, ROUND( ((CAST (I.iluminacao_e_agua AS DECIMAL(10,2))) / (CAST (T.iluminacao_e_agua AS DECIMAL(10,2))) * 100), 2 ) FROM AGUAEENERGIA I, AGUAEENERGIATOTAL T WHERE T.sigla_uf = I.sigla_uf;
