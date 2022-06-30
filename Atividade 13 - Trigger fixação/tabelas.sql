CREATE TABLE disciplina (
	cod_disc integer,
	nome varchar(45),
	cod_prof integer,
	CONSTRAINT disciplina_pk PRIMARY KEY (cod_disc),
	CONSTRAINT disciplina_fk FOREIGN KEY (cod_prof) REFERENCES professor (cod_prof)
);

CREATE TABLE turma(
	cod_turma integer,
	nome varchar(45),
	quant_aluno integer,
	CONSTRAINT turma_pk PRIMARY KEY (cod_turma)
);


CREATE TABLE aluno(
	cod_aluno integer,
	nome varchar(45),
	cpf varchar(45),
	senha varchar(45),
	status varchar(45),
	CONSTRAINT aluno_pk PRIMARY KEY (cod_aluno)
);


CREATE TABLE turma_aluno(
	cod_turma_aluno integer,
	cod_aluno integer,
	cod_turma integer,
	CONSTRAINT turma_aluno_pk PRIMARY KEY (cod_turma_aluno, cod_aluno, cod_turma),
	CONSTRAINT turma_aluno_fk1 FOREIGN KEY (cod_aluno) REFERENCES aluno (cod_aluno),
	CONSTRAINT turma_aluno_fk2 FOREIGN KEY (cod_turma) REFERENCES turma (cod_turma)
);


CREATE TABLE nota(
	cod_nota integer,
	cod_disc integer,
	cod_aluno integer,
	nota_1semestre decimal(10,2),
	nota_2semestre decimal(10,2),
	nota_final decimal(10,2),
	CONSTRAINT nota_pk PRIMARY KEY (cod_nota),
	CONSTRAINT nota_fk1 FOREIGN KEY (cod_aluno) REFERENCES aluno (cod_aluno),
	CONSTRAINT nota_fk2 FOREIGN KEY (cod_disc) REFERENCES disciplina (cod_disc)
);


CREATE TABLE log(
	descricao varchar(200)
);

CREATE TABLE professor(
	cod_prof serial,
	nome varchar(45),
	cpf varchar(45),
	senha varchar(45),
	quant_disciplina integer,
	CONSTRAINT professor_pk PRIMARY KEY (cod_prof)
);


