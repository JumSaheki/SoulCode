-- 1. Crie uma trigger que quando alterada a senha do professor, crie um
-- registro na tabela log informando que essa modificação aconteceu
-- informando o nome do professor;

CREATE OR REPLACE FUNCTION update_senha_professor()
	RETURNS TRIGGER AS $senha_prof$
		BEGIN
			IF (new.senha <> old.senha) THEN 
				INSERT INTO log VALUES('O professor ' || old.nome || ' mudou a senha.');
				RETURN NEW;
			END IF;
			RETURN NULL;
	END;
$senha_prof$ LANGUAGE plpgsql;

CREATE TRIGGER update_senha_professor AFTER
	UPDATE ON professor
		FOR EACH ROW
			EXECUTE PROCEDURE update_senha_professor();



--------------------------------------------------------------
--------------------------------------------------------------

-- 2. Crie uma trigger que quando alterado o status do aluno, crie um registro na
-- tabela log informando que essa modificação aconteceu informando o nome
-- do aluno;

CREATE TRIGGER status_aluno AFTER
    UPDATE ON aluno
        FOR EACH ROW
            EXECUTE PROCEDURE update_status_aluno()

CREATE OR REPLACE FUNCTION update_status_aluno()
	RETURNS TRIGGER AS $status_aluno$
		BEGIN
			IF (new.status <> old.status) THEN 
                INSERT INTO log(descricao) VALUES('O aluno ' || old.nome || ' mudou seu status para ' || new.status || '.');
            RETURN NEW;
            END IF;
        RETURN NULL;
    END;
$status_aluno$ LANGUAGE plpgsql;


-----------------------------------------------------
-----------------------------------------------------

-- 3. Crie uma trigger que quando for adicionado a uma turma, crie um registro 
-- na tabela log informando que essa adição aconteceu informando o nome 
-- da turma;

CREATE OR REPLACE FUNCTION  insert_nome_turma()
    RETURNS TRIGGER AS $nome_turma$
        BEGIN
            IF(TG_OP = 'INSERT') THEN
                INSERT INTO log VALUES ('INSERT realizado. A turma ' || new.nome || ' foi adicionada.');
            END IF;
        RETURN NEW;
    END;
$nome_turma$ LANGUAGE plpgsql;

CREATE TRIGGER nome_turma AFTER
INSERT ON turma FOR EACH ROW
EXECUTE PROCEDURE insert_nome_turma()

--------------------------------------------------
-- 4. Crie uma trigger que quando uma nota for adicionada na tabela nota, crie 
-- um registro na tabela log informando a nota e o codaluno que recebeu a 
-- nota;

CREATE OR REPLACE FUNCTION insert_nota_aluno()
RETURNS TRIGGER AS $$
    BEGIN
        IF (TG_OP = 'INSERT') THEN 
            INSERT INTO log VALUES ('INSERT realizado. O aluno ' || new.cod_aluno || ' tirou as notas ' || new.nota_1semestre || ' e ' || new.nota_2semestre || '.');
        END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_nota_aluno AFTER
INSERT ON nota FOR EACH ROW
EXECUTE PROCEDURE insert_nota_aluno();

-- 5. Crie um a trigger que quando for adicionado algum aluno na tabela 
-- turma_aluno, adicione +1 aluno em quantidadealunos na tabela turma;

CREATE OR REPLACE FUNCTION adiciona_quantidade_aluno()
RETURNS TRIGGER AS $$
    BEGIN 
        IF (TG_OP = 'INSERT') THEN
            UPDATE turma SET quant_aluno = quant_aluno + 1 
            WHERE cod_turma = new.cod_turma_aluno;
        END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER adiciona_quantidade_aluno
AFTER INSERT ON turma_aluno FOR EACH ROW
EXECUTE PROCEDURE adiciona_quantidade_aluno();

-- 6. Crie uma trigger que quando for adicionado algum professor na tabela 
-- disciplina, adicione +1 disciplina em quantdisciplina na tabela professor;


CREATE OR REPLACE FUNCTION adiciona_quantidade_professor()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        UPDATE professor  SET quant_disciplina = quant_disciplina + 1 
            WHERE cod_prof = NEW.cod_prof;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER adiciona_quantidade_professor
AFTER INSERT ON disciplina FOR EACH ROW
EXECUTE PROCEDURE adiciona_quantidade_professor();


-- 7. Crie uma trigger que quando for adicionado ou alterado uma nota, altere o 
-- campo nota final segundo o padrão n1+n2/2;

CREATE OR REPLACE FUNCTION altera_nota_media()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        UPDATE nota SET nota_final = (nota_1semestre + nota_2semestre)/2 WHERE cod_nota = new.cod_nota;
    END IF;
    IF (TG_OP = 'UPDATE') THEN
        UPDATE nota SET nota_final = (new.nota_1semestre + new.nota_2semestre)/2 WHERE cod_nota = new.cod_nota;
    END IF;
    RETURN new;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER altera_nota_media
AFTER INSERT OR UPDATE ON nota 
FOR EACH ROW WHEN (pg_trigger_depth() = 0)
EXECUTE PROCEDURE altera_nota_media();


-- 8. Crie uma trigger que quando for adicionado a nota final do aluno, crie um 
-- registro na tabela log informando a disciplina, código do aluno e a nota 
-- final

CREATE OR REPLACE FUNCTION log_nota_final()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'UPDATE' AND old.nota_final <> new.nota_final) THEN
        INSERT ON log VALUES ('UPDATE na tabela nota realizado a nota do aluno de código  ' || new.cod_aluno || ' na disciplina ' || new.cod_disc || ' foi atualizado para ' || new.nota_final || '.');
    END IF;
    IF (TG_OP = 'INSERT') THEN
        INSERT ON log VALUES ('INSERT na tabela nota realizado ');
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_nota_final
AFTER INSERT OR UPDATE ON nota FOR EACH ROW
EXECUTE PROCEDURE log_nota_final()