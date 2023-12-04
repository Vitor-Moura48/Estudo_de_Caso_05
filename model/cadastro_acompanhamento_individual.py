class CadastroAluno_Acompanhamento:
    def __init__(self):
        self.lista_alunos = []

    def cadastro_alunos(self):

        while True:
            aluno = []
            i = i + 1
            print("Cadastro de alunos")
            print(f"Aluno {i}")
            aluno.append(input("Nome: "))
            aluno.append(input("Histórico Médico(Se houver): "))
            aluno.append(int(input("idade: ")))
            aluno.append(float(input("Peso: ")))
            aluno.append(float(input("Altura: ")))
            aluno.append(input("Digite as metas de condicionamento do aluno (se houver):"))
            self.lista_alunos.append(aluno[:])
            resp = ("Continuar o cadastro? [S/N] ").upper().strip()[0]
            if resp == "N":
                break
    
    def avaliacao_periodica(self):
        lista_avaliacao = []
        lista_avaliacao_aluno = []
        print("Avaliação")
        while True:
            i = i +1
            print(f"Avaliação do aluno {i}")
            lista_avaliacao_aluno.append(input("Digite a data da avaliação: "))
            lista_avaliacao_aluno.append(input("Digite o resultado do teste físico (se houver): "))
            lista_avaliacao_aluno.append(input("Digite a medição de peso (se houver): "))
            lista_avaliacao_aluno.append(input("Digite a análise de desempenho em exercícios (se houver): "))
            lista_avaliacao.append(lista_avaliacao_aluno[:])
            resp = input("Quer ir para o próximo paciente? [S/N] ").upper().strip()[0]
            if resp == "N":
                break