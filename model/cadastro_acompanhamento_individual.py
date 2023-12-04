import os
import csv
from datetime import datetime

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
        
        with open(self.cadastro,'a') as arquivo_csv:
            escritor = csv.writer(arquivo_csv,delimiter=';')
            escritor.writerow(aluno)

    def avaliacao_periodica(self,nome):
        lista_avaliacao_aluno = []

        if not os.path.isfile(f"database/avaliacao_alunos/{nome}.csv"):
            with open(f'database/avaliacao_alunos/{nome}.csv','a',newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv)
                escritor.writerow(['Nome','Data','Teste_Fisico','Peso','Desempenho_Fisico'])   

        print("Avaliação do aluno")
        lista_avaliacao_aluno.append(nome)
        lista_avaliacao_aluno.append(input("Digite a data da avaliação: "))
        lista_avaliacao_aluno.append(input("Digite o resultado do teste físico (se houver): "))
        lista_avaliacao_aluno.append(input("Digite a medição de peso (se houver): "))
        lista_avaliacao_aluno.append(input("Digite a análise de desempenho em exercícios (se houver): "))
        
        if os.path.isfile(f"database/avaliacao_alunos/{nome}.csv"):              
            with open(f'database/avaliacao_alunos/{nome}.csv','a',newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv)
                escritor.writerow(lista_avaliacao_aluno)                                    
            
    def relatorios(self,nome):
        if os.path.isfile(f"database/avaliacao_alunos/{nome}.csv"):
            count = 0
            with open(f"database/avaliacao_alunos/{nome}.csv","r") as arquivo_relatorios:
                leitor = csv.reader(arquivo_relatorios)
                next(leitor)
                for avaliacao in leitor:
                    if avaliacao[0] == nome:
                        count += 1
                        if count == 5:
                            if os.path.isfile(f"database/relatorio_alunos/{nome}.csv"):
                                with open(f"database/relatorio_alunos/{nome}.csv",'a',newline='') as arquivo_relatorio_nome:
                                    escritor = csv.writer(arquivo_relatorio_nome)
                                    escritor.writerow(avaliacao)
                            else:
                                with open(f"database/relatorio_alunos/{nome}.csv",'a',newline='') as arquivo_relatorio_nome:
                                    escritor = csv.writer(arquivo_relatorio_nome)
                                    escritor.writerow(['Nome','Data','Teste_Fisico','Peso','Desempenho_Fisico'])
        else:
            print('Aluno não está cadastrado! Cadastre-o')

    def historico(self,nome):
        with open(f"database/avaliacao_alunos/{nome}.csv",'r') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            for avaliacao in leitor:
                if avaliacao[0] == nome:
                    if not os.path.isfile(f"database/historico_alunos/{nome}.csv"):
                        with open(f"database/historico_alunos/{nome}.txt",'w') as arquivo_txt:
                            arquivo_txt.write(f'{avaliacao[2]} -- {avaliacao[4]}')
                    else:
                        with open(f"database/historico_alunos/{nome}.txt",'a') as arquivo_txt:
                            arquivo_txt.write(f'\n{avaliacao[2]} -- {avaliacao[4]}')    
    
    def alerta(self,nome):
        resposta = (input(f'O aluno {nome} veio hoje? [S/N]').upper().strip()[0])
        
        if resposta == 'N':
            with open(f'database/avaliacao_alunos/{nome}.csv','a',newline='') as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([f'Aluno {nome} esteve pendente hoje!'])
        else:
            pass
    
    def personalizar(self,nome):
        with open(f"database/avaliacao_alunos/{nome}.csv",'r') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            print(f'==treino de {nome}==')
            for avaliacao in leitor:
                print(f'\n{avaliacao[2]} -- {avaliacao[4]}')
            
            continuar_n = (input("Deseja ajustar o treino? [S/N]").upper().strip()[0])
            
            
            if continuar_n == 'S':
                treino = input('Digite o treino do aluno:')
                if not os.path.isfile(f"database/treino_personalizado/{nome}.txt"):
                    with open(f'database/treino_personalizado/{nome}.txt','w') as arquivo_txt:
                        arquivo_txt.write(treino)
                else:
                    
                    with open(f'database/treino_personalizado/{nome}.txt','w') as arquivo_txt:
                        arquivo_txt.write(treino)
                    print('Treino ajustado')

            elif continuar_n == 'N':
                return print('Treino visto')      

 
gr = CadastroAluno_Acompanhamento()
gr.alerta('Rafael')
