import os
import csv

class CadastroAluno_Acompanhamento:
    def __init__(self):
        self.cadastro = "database/cadastro_alunos.csv"

        if os.path.isfile(self.cadastro):
            pass
        else:
           with open(self.cadastro,'a',newline='') as arquivo_csv:
               escritor = csv.writer(arquivo_csv,delimiter=';')
               escritor.writerow(['Nome','Historico_Medico','Idade','Peso','Altura','Metas_do_Aluno'])

    def cadastro_alunos(self):

        aluno = []
        print("Cadastro de alunos")
        nome = (input("Nome: "))
        aluno.append(nome)
        aluno.append(input("Histórico Médico(Se houver): "))
        aluno.append(int(input("idade: ")))
        aluno.append(float(input("Peso: ")))
        aluno.append(float(input("Altura: ")))
        aluno.append(input("Digite as metas de condicionamento do aluno (se houver):"))
        
        with open(self.cadastro,'a',newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv,delimiter=';')
            escritor.writerow(aluno)

    def avaliacao_periodica(self,nome):
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


                                               

            
