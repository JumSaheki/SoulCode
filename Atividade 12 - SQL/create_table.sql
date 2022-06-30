CREATE TABLE IF NOT EXISTS aluno(
    num_aluno serial,
    num_curso integer,
    nome varchar(80),
    endereco varchar(200),
    cidade varchar(100),
    telefone varchar(15),
    CONSTRAINT aluno_pk PRIMARY KEY (num_aluno),
    CONSTRAINT aluno_fk FOREIGN KEY (num_curso) REFERENCES curso (num_curso)    
);

    
CREATE TABLE IF NOT EXISTS curso(
    num_curso serial,
    nome varchar(50),
    total_creditos integer,
    CONSTRAINT curso_pk PRIMARY KEY (num_curso)
);
INSERT INTO CURSO VALUES
    (1, 'Ciências da Computação', 175),
    (2, 'Matemática Pura', 175),
    (3, 'Matemática Aplicada', 175),
    (4, 'Estatística'. 175),
    (5, 'Engenharia da Computação', 200);

CREATE TABLE IF NOT EXISTS professor(
    num_prof serial,
    nome varchar(80),
    area_pesquisa varchar(100),
    CONSTRAINT professor_pk PRIMARY KEY (num_prof)
);
UPDATE professor SET nome = 'Ramon Travanti' WHERE num_prof = 1;
UPDATE professor SET nome = 'Marcos Salvador' WHERE num_prof = 2;
UPDATE professor SET nome = 'Abgair' WHERE num_prof = 3;

CREATE TABLE IF NOT EXISTS disciplina(
    num_disciplina serial,
    num_curso integer,
    nome varchar(100),
    quant_creditos integer,
    CONSTRAINT disciplina_pk PRIMARY KEY (num_disciplina),
    CONSTRAINT disciplina_fk1 FOREIGN KEY (num_curso) REFERENCES curso (num_curso),
);
UPDATE disciplina SET nome = 'Cálculo Numérico' WHERE num_disciplina = 1;
UPDATE disciplina SET nome = 'Engenharia de Software' WHERE num_disciplina = 2;
UPDATE disciplina SET nome = 'Banco de Dados' WHERE num_disciplina = 3;


CREATE TABLE IF NOT EXISTS aula(
    num_aluno integer,
    num_disciplina integer,
    num_prof integer,
    num_curso_aluno integer,
    num_curso_disciplina integer,
    semestre integer,
    ano integer,
    nota decimal(10,2),
    CONSTRAINT aula_pk PRIMARY KEY (num_aluno, num_disciplina, num_prof, semestre),
    CONSTRAINT aula_fk1 FOREIGN KEY (num_aluno) REFERENCES aluno (num_aluno),
    CONSTRAINT aula_fk2 FOREIGN KEY (num_disciplina) REFERENCES disciplina (num_disciplina),
    CONSTRAINT aula_fk3 FOREIGN KEY (num_prof) REFERENCES professor (num_prof),
    CONSTRAINT aula_fk4 FOREIGN KEY (num_curso_aluno) REFERENCES aluno (num_curso),
    CONSTRAINT aula_fk5 FOREIGN KEY (num_curso_disciplina) REFERENCES disciplina (num_curso),
    CONSTRAINT verifica_curso CHECK (num_curso_aluno = num_curso_disciplina)
);