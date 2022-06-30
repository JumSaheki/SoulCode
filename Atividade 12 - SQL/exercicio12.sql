--5. Quais os nomes das disciplinas do curso de Ciência da Computação.

select d.nome from disciplina D, curso C 
    where c.num_curso = d.num_curso 
        and c.nome = 'Ciências da Computação';


--6. Quais os nomes dos cursos que possuem no curriculum a disciplina Cálculo Numérico

select c.nome from disciplina D, curso C 
    where c.num_curso = d.num_curso 
        and d.nome = 'Cálculo Numérico';


--7. Quais os nomes das disciplinas que o aluno Marcos João Casanova cursou no 1º semestre de 1998.

select d.nome as disciplina from disciplina d, aluno al, aula a 
	where a.num_disciplina = d.num_disciplina 
		and al.num_aluno = a.num_aluno 
		and al.nome = 'Marcos João Casanova'
		and a.semestre = 1
		and a.ano = 1998;


--8. Quais os nomes de disciplinas que o aluno Ailton Castro foi reprovado. 

select d.nome as disciplina from disciplina d, aluno al, aula a 
	where a.num_disciplina = d.num_disciplina 
		and al.num_aluno = a.num_aluno 
		and al.nome = 'Ailton Castro'
		and a.nota < 7;


--9. Quais os nomes de alunos reprovados na disciplina de Cálculo Numérico no 1º semestre de 1998.

select al.nome as aluno from disciplina d, aluno al, aula a 
	where a.num_disciplina = d.num_disciplina 
		and al.num_aluno = a.num_aluno 
		and d.nome = 'Cálculo Numérico'
		and a.nota < 7
		and a.semestre = 1
		and a.ano = 1998;


--10. Quais os nomes das disciplinas ministradas pelo prof. Ramon Travanti.

SELECT d.nome as disciplina from disciplina d, professor p, aula a
	WHERE a.num_prof = p.num_prof
		AND a.num_disciplina = d.num_disciplina
		AND p.nome = 'Ramon Travanti';



--11. Quais os nomes professores que já ministraram aula de Banco de Dados. 

SELECT p.nome as disciplina from disciplina d, professor p, aula a
	WHERE a.num_prof = p.num_prof
		and a.num_disciplina = d.num_disciplina
		AND d.nome = 'Banco de Dados';


--12. Qual a maior e a menor nota na disciplina de Cálculo Numérico no 1º semestre de 1998. 

SELECT MAX(a.nota) as max, MIN(a.nota) as min FROM disciplina d, aula a
	WHERE d.num_disciplina = a.num_disciplina
	AND d.nome = 'Cálculo Numérico'
	AND a.semestre = 1
	AND a.ano = 1998;


--13. Qual o nome do aluno e nota que obteve maior nota na disciplina de Engenharia de Software no 1º 
semestre de 1998. 

SELECT al.nome, a.nota from aula a, aluno al, disciplina d
				WHERE a.num_aluno = al. num_aluno
					AND d.num_disciplina = a.num_disciplina
					AND d.nome = 'Engenharia de Software'
					AND a.semestre = 1
					AND a.ano = 1998
					AND a.nota = (SELECT max(nota) FROM aula a, disciplina d, aluno al 
									WHERE a.num_disciplina = d.num_disciplina
										AND al.num_aluno = a.num_aluno
										AND d.nome = 'Engenharia de Software'
										AND a.semestre = 1
										AND a.ano = 1998);


--14. Quais nomes de alunos, nome de disciplina e nome de professores que cursaram o 1º semestre de 
1998 em ordem de aluno.

SELECT al.nome AS aluno, d.nome AS disciplina, p.nome AS professor FROM disciplina d, aluno al, aula a, professor p 
	WHERE a.num_disciplina = d.num_disciplina 
		AND al.num_aluno = a.num_aluno 
		AND p.num_prof = a.num_prof
		AND a.semestre = 1
		AND a.ano = 1998
		ORDER BY al.nome;


--15. Quais nomes de alunos, nome de disciplina e notas do 1º semestre de 1998 no curso de Ciência da 
Computação. 

SELECT al.nome AS aluno, d.nome AS disciplina, a.nota FROM disciplina d, curso c, aluno al, aula a
	WHERE d.num_curso = c.num_curso
		AND al.num_curso = c.num_curso	
		AND d.num_disciplina = a.num_disciplina
		AND c.nome = 'Ciências da Computação'
		AND a.semestre = 1
		AND a.ano = 1998;


--16. Qual a média de notas do professor Marcos Salvador. 

SELECT avg(a.nota) FROM aula a, professor p
	WHERE a.num_prof = p.num_prof
		AND p.nome = 'Marcos Salvador';



--17. Quais nomes de alunos, nomes de disciplinas e notas que tiveram nota entre 5.0 e 7.0 em ordem de 
disciplina. 

SELECT al.nome, d.nome, a.nota FROM aluno al, disciplina d, aula a
	WHERE a.num_aluno = al.num_aluno
		AND a.num_disciplina = d.num_disciplina
		AND a.nota > 5
		AND a.nota < 7
		ORDER BY d.nome;



--18. Qual a média de notas da disciplina Cálculo Numérico no 1º semestre de 1998. 

SELECT avg(a.nota) FROM aula a, disciplina D
	WHERE a.num_disciplina = d. num_disciplina
		AND d.nome = 'Cálculo Numérico'
		AND a.semestre = 1
		AND a.ano = 1998;


--19. Quantos alunos o professor Abgair teve no 1º semestre de 1998. 

SELECT count(distinct a.num_aluno) FROM aula a, professor p
	WHERE a.num_prof = p.num_prof
	AND p.nome = 'Abgair'
	AND a.semestre = 1
	AND a.ano = 1998;


--20. Qual a média de notas do aluno Edvaldo Carlos Silva. 

SELECT avg(a.nota) FROM aula a, aluno al 
	WHERE a.num_aluno = al.num_aluno
		AND al.nome = 'Edvaldo Carlos Silva';


--21. Quais as médias por nome de disciplina de todos os cursos do 1º semestre de 1998 em ordem de disciplina. 

SELECT d.nome, avg(a.nota) FROM aula a, disciplina d 
	WHERE a.num_disciplina = d.num_disciplina
		AND a.semestre = 1
		AND a.ano = 1998
		GROUP BY d.nome
		ORDER BY d.nome;


--22. Quais as médias das notas por nome de professor no 1º semestre de 1998. 

SELECT p.nome, avg(a.nota) FROM aula a, professor p 
	WHERE a.num_prof = p.num_prof
	AND a.semestre = 1
	AND a.ano = 1998
	GROUP BY p.nome;

--23. Qual a média por disciplina no 1º semestre de 1998 do curso do Ciência da Computação 

SELECT d.nome, AVG(a.nota) FROM aula a, disciplina d, curso c 
	WHERE a.num_disciplina = d.num_disciplina
		AND d.num_curso = c.num_curso
		AND c.nome = 'Ciências da Computação'
		AND a.ano = 1998
		AND a.semestre = 1
		GROUP BY d.nome;


--24. Qual foi quantidade de créditos concluídos (somente as disciplinas aprovadas) do aluno Edvaldo Carlos 
Silva. 

SELECT sum(d.quant_creditos) FROM aula a, disciplina d, aluno al 
	WHERE a.num_disciplina = d.num_disciplina
		AND a.num_aluno = al.num_aluno	
		AND al.nome = 'Edvaldo Carlos Silva'
		AND a.nota >= 7;


--25. Quais nomes de alunos e quantidade de créditos que já completaram 70 créditos (somente os 
aprovados na disciplina). 

SELECT al.nome, sum(d.quant_creditos) FROM aula a, disciplina d, aluno al
	WHERE a.num_disciplina = d.num_disciplina
		AND a.num_aluno = al.num_aluno
		AND a.nota >= 7
		GROUP BY al.nome HAVING sum(d.quant_creditos) >= 70;
		

--26. Quais nomes de alunos, nome de disciplina e nome de professores que cursaram o 1º semestre de 
1998 e pertencem ao curso de ciência da Computação que possuem nota superior à 8.0.

SELECT al.nome, d.nome, p.nome FROM aluno al, aula a, professor p, disciplina d
	WHERE a.num_aluno = a.num_aluno
		AND a.num_disciplina = d.num_disciplina
		AND a.num_prof = p.num_prof
		AND a.ano = 1998
		AND a.semestre =1
		AND a.nota > 8;

--27. Qual a disciplina com nota mais baixa em qualquer época

SELECT d.nome FROM aula a, disciplina d 
	WHERE a.num_disciplina = d.num_disciplina
		AND a.nota = (SELECT MIN(nota) FROM aula);
		


--28. Qual a disciplina com média de nota mais alta em qualquer época

SELECT d.nome FROM aula a, disciplina d 
	WHERE a.num_disciplina = d.num_disciplina 
		GROUP BY d.nome
			ORDER BY avg(a.nota) desc
				LIMIT 1;

--29. Quais alunos já concluiram o curso de Ciência da Computação?

SELECT al.nome FROM aluno al, aula a, disciplina d, curso c 
	WHERE al.num_aluno = a.num_aluno
		AND a.num_disciplina = d.num_disciplina
		AND al.num_curso = c.num_curso
		AND c.nome = 'Ciências da Computação'
		AND a.nota >= 7
			GROUP BY al.nome 
			HAVING SUM(d.quant_creditos) >= (SELECT total_creditos FROM curso 
											 WHERE nome = 'Ciências da Computação');


--30. Ordene as disciplinas por quantidade de reprovações

SELECT d.nome, count(a.num_disciplina) FROM disciplina d, aula a 
	WHERE d.num_disciplina = a.num_disciplina
		AND a.nota < 7
		GROUP BY d.nome
		ORDER BY count(a.num_disciplina) DESC;
		