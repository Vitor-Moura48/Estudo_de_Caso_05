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

class Mensagem:
    def __init__(self, remetente, destinatario, conteudo):
        self.remetente = remetente
        self.destinatario = destinatario
        self.conteudo = conteudo
        self.data = datetime.now()
        
    def salvar_mensagem(self):
        data_formatada = self.data.strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"{self.remetente}_{self.destinatario}_{data_formatada}.txt"

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"De: {self.remetente}\n")
            arquivo.write(f"Para: {self.destinatario}\n")
            arquivo.write(f"Data: {self.data}\n")
            arquivo.write(f"Conteúdo: {self.conteudo}\n")

        print(f"Mensagem salva em {nome_arquivo}")

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_professores = ['João', 'Pedro', 'Caio', 'Amaral']

    def enviar_mensagem_professor(self, conteudo):
        print("Escolha o professor destinatário:")
        for i, professor in enumerate(self.lista_de_professores, start=1):
            print(f"{i}. {professor}")

        try:
            opcao = int(input("Digite o número do professor destinatário: "))
            professor_destino = self.lista_de_professores[opcao - 1]
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")
            return

        mensagem = Mensagem(self.nome, professor_destino, conteudo)
        print(f"Mensagem enviada para {professor_destino}: {conteudo}")
        return mensagem


class Professor:
    def __init__(self, nome):
        self.nome = nome

    def enviar_mensagem_aluno(self, aluno_destino, conteudo):
        print('Mensagem enviada')
        
    def receber_mensagem(self,aluno,conteudo):
        print(f"Mensagem recebida de {aluno} em {Mensagem(self.data)}: {conteudo}")
