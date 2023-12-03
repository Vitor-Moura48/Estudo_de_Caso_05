import pandas as pd
import os
from datetime import datetime

from colorama import init, Fore, Style
init()
cor_mensagem_erro = Fore.RED
cor_mensagem_ok = Fore.GREEN

import smtplib # para enviar emails

# para api
import requests

class AvaliacaoNutricional:

    def __init__(self):
        self.caminho_perfil_nutricional = "database/perfil_nutricional.csv"
        self.caminho_registro_diario = "database/registro_diario.csv"
        self.caminho_feedbacks = "database/feedbacks.csv"

        if not os.path.exists(self.caminho_perfil_nutricional):
            perfil = pd.DataFrame(columns=['nome', 'identificador', 'habitos_alimentares', 'restricoes_alimentares', 'peso_objetivo', 'preferencias_alimentares'], dtype=str)
            perfil.to_csv(self.caminho_perfil_nutricional, index=False)

        if not os.path.exists(self.caminho_registro_diario):
            perfil = pd.DataFrame(columns=['nome', 'identificador', 'data', 'descricao_refeicoes', 'calorias_totais', 'consumo_agua', 'suplementos'])
            perfil.to_csv(self.caminho_registro_diario, index=False)
        
        if not os.path.exists(self.caminho_feedbacks):
            perfil = pd.DataFrame(columns=['nome', 'identificador', 'data', 'feedback'])
            perfil.to_csv(self.caminho_feedbacks, index=False)


    # RF 17 e 18
    def cadastrar_perfil_nutricional(self, nome, identificador, habitos, restricoes, peso_objetivo, preferencias):

        # lê o arquivo
        perfil_nutricional = pd.read_csv(self.caminho_perfil_nutricional)

        # confere se o indentificador já existe, se não, adiciona no arquivo
        if perfil_nutricional.empty or not identificador in str(perfil_nutricional['identificador'].values):

            novo_perfil = pd.DataFrame({"nome": [nome], "identificador": [identificador], "habitos": [habitos], "restricoes": [restricoes], "peso_objetivo": [peso_objetivo], "preferencias": [preferencias]})
            novo_perfil.to_csv(self.caminho_perfil_nutricional, index=False, header=False, mode='a')

            print(f"\n{cor_mensagem_ok}Perfil adicionado...{Style.RESET_ALL}\n")

        else:
            print(f"\n{cor_mensagem_erro}Indentificador já existe!{Style.RESET_ALL}\n")


    def alterar_perfil_nutricional(self, nome, identificador, habitos, restricoes, peso_objetivo, preferencias):

        # lê o arquivo
        perfil_nutricional = pd.read_csv(self.caminho_perfil_nutricional)
        
        # confere se o indentificador já existe, se não, adiciona no arquivo
        if not perfil_nutricional.empty and identificador in str(perfil_nutricional['identificador'].values):

            # busca o indice no arquivo a partir do identificador
            indice = perfil_nutricional[(perfil_nutricional["identificador"].astype(str) == identificador)].index[0]
            
            # troca as informaçoes
            perfil_nutricional.loc[indice, ['nome']] = [nome]
            perfil_nutricional.loc[indice, ['habitos_alimentares']] = [habitos]
            perfil_nutricional.loc[indice, ['restricoes_alimentares']] = [restricoes]
            perfil_nutricional.loc[indice, ['peso_objetivo']] = [peso_objetivo]
            perfil_nutricional.loc[indice, ['preferencias_alimentares']] = [preferencias]

            # atualiza o arquivo
            perfil_nutricional.to_csv(self.caminho_perfil_nutricional, index=False)

            print(f"\n{cor_mensagem_ok}Perfil alterado...{Style.RESET_ALL}\n")

        else:
            print(f"\n{cor_mensagem_erro}Indentificador não encontrado!{Style.RESET_ALL}\n")

    
    # RF 19 e 21
    def registro_dieta_diario(self, nome, identificador, descricao, caloria_total, consumo_agua, suplementos):
        
        # lê o arquivo
        registro = pd.read_csv(self.caminho_registro_diario)

        # Obtém a data de hoje
        data = str(datetime.now().date())
    
        # confere se já existe algum registro daquele aluno naquele dia
        if registro.empty or registro.loc[(registro['identificador'].astype(str) == identificador) & (registro['data'] == data)].empty:

            # adiciona o novo registro no arquivo
            novo_registro = pd.DataFrame({
                                            "nome": [nome],
                                            "identificador": [identificador],
                                            "data": [data], 
                                            "descricao": [descricao], 
                                            "caloria_total": [caloria_total], 
                                            "consumo_agua": [consumo_agua], 
                                            "suplementos": [suplementos]
                                        })
            novo_registro.to_csv(self.caminho_registro_diario, index=False, header=False, mode='a')

            # faz uma analise da proporção peso/calorias
            peso = round((caloria_total - 550) / 15, 2)
            print(f"\n{cor_mensagem_ok}Você ingeriu calorias para uma pessoa de {peso}kg{Style.RESET_ALL}\n")

            # alerta caso o consumo de água não esteja completo
            if consumo_agua < 2:
                print(f"{cor_mensagem_erro}Alerta! Necessário consumo de água: {2 - consumo_agua}L{Style.RESET_ALL}\n")
            
            print(f"{cor_mensagem_ok}Registrado com sucesso...{Style.RESET_ALL}\n")
            
            # chama uma função para verificar se o consumo de calorias está adequado
            self.alerta_meta_nutricional(identificador, caloria_total)

        else:
            print(f"\n{cor_mensagem_erro}Você já fez um registro hoje!{Style.RESET_ALL}\n")


    def orientacao_nutricional(self, identificador):
        
        # lê o arquivo
        perfil_nutricional = pd.read_csv(self.caminho_perfil_nutricional)

        # confere se o identificador está no arquivo
        if not perfil_nutricional.empty and identificador in str(perfil_nutricional['identificador'].values):

            # obtem as informações da pessoa especifica
            informacoes_aluno = perfil_nutricional.loc[perfil_nutricional['identificador'].astype(str) == identificador]

            # calcula as calorias recomentadas
            calorias_recomendadas = (int(informacoes_aluno['peso_objetivo'].iloc[0]) * 15) + 550

            # recomenda alimentos de acordo com as calorias recomendadas
            print(f"\n{cor_mensagem_ok}Calorias recomendadas: {calorias_recomendadas}")

            if calorias_recomendadas <= 1300:
                print("\nprocura ingerir alimentos como: frutas, legumes, proteinas: frango\n")
            elif calorias_recomendadas <= 1600:
                print("\nprocura ingerir alimentos como: grãos integrais, abacate, laticínios, proteinas: peixe, ovos\n")
            elif calorias_recomendadas <= 1900:
                print("\nProcura ingerir alimentos como: azeite de oliva, frutas secas, quinoa, proteinas: carne vermelha\n")
            elif calorias_recomendadas <= 2350:
                print("\nProcura ingerir alimentos como: amêndoas, massa, bacon, queijos mais gordurosos, proteinas: salmão\n")
            else:
                print(f"\nSem muitas restrições...{Style.RESET_ALL}\n")
                
        else:
            print(f"\n{cor_mensagem_erro}Indentificador não encontrado!{Style.RESET_ALL}\n")


    def alerta_meta_nutricional(self, identificador, caloria_total):
        
        # lê o arquivo
        perfil_nutricional = pd.read_csv(self.caminho_perfil_nutricional)

        # confere se o identificador está no arquivo
        if not perfil_nutricional.empty and identificador in str(perfil_nutricional['identificador'].values):

            # obtem as informações da pessoa especifica
            informacoes_aluno = perfil_nutricional.loc[perfil_nutricional['identificador'].astype(str) == identificador]

            # calcula as calorias recomentadas
            calorias_recomendadas = (int(informacoes_aluno['peso_objetivo'][0]) * 15) + 550

            # define uma mensagem com base nas calorias que o aluno deve consumir e oq ele consumiu
            if (caloria_total >= calorias_recomendadas * 0.9) and (caloria_total <= calorias_recomendadas * 1.1): # se estiver com 10% de margem +/-
                mensagem = "Você está consumindo uma quantidade adequada de calorias, continue assim!"
            if caloria_total < calorias_recomendadas * 0.9: 
                mensagem = "Você está consumindo poucas calorias..."
            else:
                mensagem = "Você está consumindo muitas calorias!"

            # tenta enviar um email para o aluno com informações sobre seu desempenho
            try:

                # encia um email com a mensagem (ainda incompleto)
                endereco = 'smtp.gmail.com'
                porta = 587
                servidor = smtplib.SMTP(endereco, porta)

                servidor.starttls()
                servidor.login('estudo.caso.05@gmail.com', '192837a5')

                de = 'algum_email.7@gmail.com'
                para = 'estudo.caso.05@gmail.com'
                assunto = 'Estudo de Caso 05'
                corpo_do_email = f'Assunto: {assunto}\n\n{mensagem}'

                servidor.sendmail(de, para, corpo_do_email)
                servidor.quit()

            except:
                print(f"\n{cor_mensagem_erro}Não foi possível estabelecer uma conexão com email{Style.RESET_ALL}\n")
    
        else:
            print(f"\n{cor_mensagem_erro}Indentificador não encontrado!{Style.RESET_ALL}\n")
        

    # busca o alimento e informa quantas calorias ele tem a partir de uma api
    def rastreamento_alimentar(self, busca):
        
        api = requests.get(f"https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={busca}")
        dados = api.json()

        if dados != []:
            print()
            for dado in dados:
                print(f"{dado['descricao']}: {cor_mensagem_ok}{dado['calorias']}{Style.RESET_ALL}")
            print()
        else:
            print(f"\n{cor_mensagem_erro}Nenhum prato encontrado...{Style.RESET_ALL}\n")


    def feedback_comunicacao_nutricionista(self, nome, identificador, feedback):

        # lê o arquivos
        perfil_nutricional = pd.read_csv(self.caminho_perfil_nutricional)
        arquivo_feedbacks = pd.read_csv(self.caminho_feedbacks)

        # Obtém a data de hoje
        data = str(datetime.now().date())

        if not perfil_nutricional.empty and identificador in str(perfil_nutricional['identificador'].values):

            # confere se o aluno já enviou algum feedback hoje
            if arquivo_feedbacks.empty or arquivo_feedbacks.loc[(arquivo_feedbacks['identificador'].astype(str) == identificador) & (arquivo_feedbacks['data'] == data)].empty:

                # adiciona o novo feedback
                novo_feedback = pd.DataFrame({"nome": [nome], "identificador": [identificador], "data": [data], "feedback": [feedback]})
                novo_feedback.to_csv(self.caminho_feedbacks, index=False, header=False, mode='a')

                print(f"\n{cor_mensagem_ok}Feedback enviado...{Style.RESET_ALL}\n")

            else:
                print(f"\n{cor_mensagem_erro}Feedback já registrado hoje!{Style.RESET_ALL}\n")

        else:
            print(f"\n{cor_mensagem_erro}Perfil não encontrado!{Style.RESET_ALL}\n")

teste = AvaliacaoNutricional()

#teste.alerta_meta_nutricional('123', 1000)
