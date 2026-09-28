from  disciplina import Disciplina
from aluno import Aluno

aluno1 = Aluno("joão", "123456", "Ciência da Computação")

python = Disciplina("Python", "Russi")
sers = Disciplina("Sers", "André")

aluno1.matricular(python)
aluno1.matricular(sers)

aluno1.add_nota(python, 9.5)
aluno1.add_nota(python, 7)
aluno1.add_nota(sers, 10)
aluno1.add_nota(sers, 5)

aluno1.exibir_boletim()