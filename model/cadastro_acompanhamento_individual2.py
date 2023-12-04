from cadastro_acompanhamento_individual import *

gr = CadastroAluno_Acompanhamento()

def relatorios(self,nome):
    if os.path.isfile(f"database/avaliacao_alunos/{nome}.csv"):
        count = 0
        with open(f"database/avaliacao_alunos/{nome}.csv", "r") as arquivo_relatorios:
            leitor = csv.reader(arquivo_relatorios)
            next(leitor)
            for avaliacao in leitor:
                if avaliacao[0] == nome:
                    count += 1
                    if count == 5:
                        if os.path.isfile(f"database/relatorio_alunos/{nome}.csv"):
                            with open(f"database/relatorio_alunos/{nome}.csv", "a") as arquivo_relatorio_nome:
                                escritor = csv.writer(arquivo_relatorio_nome)
                                escritor.writerow(avaliacao)
                        else:
                            with open(f"database/relatorio_alunos/{nome}.csv", "a", newline='') as arquivo_relatorio_nome:
                                escritor = csv.writer(arquivo_relatorio_nome)
                                escritor.writerow(['Nome','Data','Teste_Fisico','Peso','Desempenho_Fisico'])
