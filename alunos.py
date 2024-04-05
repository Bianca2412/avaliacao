class alunos:
    def __init__(self,matricula, nome, sexo ,idade):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
if __name__ == "__main__":
    aluno1 = alunos("134", "joão", "m", "17")
    aluno2 = alunos("135", "maria", "f", "18")
    aluno3 = alunos("136", "mel", "f", "19")
    print(aluno1.matricula, aluno1.nome, aluno1.sexo, aluno1.idade)
    print(aluno2.matricula, aluno2.nome, aluno2.sexo, aluno2.idade)
    print(aluno3.matricula, aluno3.nome, aluno3.sexo, aluno3.idade)