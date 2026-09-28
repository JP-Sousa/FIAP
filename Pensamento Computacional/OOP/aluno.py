from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplinas = {}

    def matricular(self, disciplina: Disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
        self.notas_por_disciplinas.setdefault(disciplina.nome, [])

    def add_nota(self, disciplina: Disciplina, nota: float):
        self.notas_por_disciplinas[disciplina.nome].append(nota)

    def media_disciplina(self, disciplina: Disciplina) -> float:
        notas = self.notas_por_disciplinas.get(disciplina.nome, [])

        if not notas:
            return 0.0

        return sum(notas) / len(notas)

    def media_geral(self) -> float:
        medias_disciplinas = []

        for disciplina in self.disciplinas:
           medias_disciplinas.append(self.media_disciplina(disciplina))

        return sum(medias_disciplinas) / len(medias_disciplinas)

    def exibir_boletim(self):
        print(f"\nAluno: {self.nome} | Matrículas: {self.matricula}") 
        print(f"Curso: {self.curso}")

        if not self.disciplinas:
            print("Sem disciplina matriculada")
            return

        for d in self.disciplinas:
            notas = self.notas_por_disciplinas.get(d.nome, [])
            media_d = self.media_disciplina(d)

            d.exibir_infos()
            print(f"notas do aluno em: {d.nome}: {notas}")
            print(f"medias do aluno em: {d.nome} : {media_d}")

        print(f"média geral: {self.media_geral()}")