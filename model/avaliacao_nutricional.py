import pandas as pd
import os

class AvaliacaoNutricional:
    def __init__(self):
        self.caminho_perfil_nutricional = "database/perfil_nutricional.csv"
        self.caminho_registro_diario = "database/registro_diario.csv"

        if not os.path.exists(self.caminho_perfil_nutricional):
            perfil = pd.DataFrame(columns=['nome', 'identificador', 'habitos_alimentares', 'restricoes_alimentares', 'peso_objetivo', 'preferencias_alimentares'], dtype=str)
            perfil.to_csv(self.caminho_perfil_nutricional, index=False)

        if not os.path.exists(self.caminho_registro_diario):
            perfil = pd.DataFrame(columns=['nome', 'identificador', 'data', 'descricao_refeicoes', 'calorias_totais'])
            perfil.to_csv(self.caminho_registro_diario, index=False)

    # RF 17 e 18
    def cadastrar_perfil_nutricional(self, nome, identificador, habitos, restricoes, peso_objetivo, preferencias):

        # lê o arquivo
        perfil_nutricional = pd.read_csv(self.caminho_perfil_nutricional)

        # confere se o indentificador já existe, se não, adiciona no arquivo
        if perfil_nutricional.empty or not identificador in str(perfil_nutricional['identificador'].values):

            novo_perfil = pd.DataFrame({"nome": [nome], "identificador": [identificador], "habitos": [habitos], "restricoes": [restricoes], "peso_objetivo": [peso_objetivo], "preferencias": [preferencias]})
            novo_perfil.to_csv(self.caminho_perfil_nutricional, index=False, header=False, mode='a')

        else:
            print("\nIndentificador já existe!\n")

    def alterar_perfil_nutricional(self,  nome, identificador, habitos, restricoes, peso_objetivo, preferencias):

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

        else:
            print("Indentificador não encontrado!")
    
    def registro_dieta_diario(self, nome, identificador, data, descricao, caloria_total):
        
        # lê o arquivo
        registro = pd.read_csv(self.caminho_registro_diario)
    
        # confere se já existe algum registro daquele aluno naquele dia
        if registro.empty or registro.loc[(registro['identificador'].astype(str) == identificador) & (registro['data'] == data)].empty:

            # adiciona o novo registro no arquivo
            novo_registro = pd.DataFrame({"nome": [nome], "identificador": [identificador], "data": [data], "descricao": [descricao], "caloria_total": [caloria_total]})
            novo_registro.to_csv(self.caminho_registro_diario, index=False, header=False, mode='a')

            # faz uma analise da proporção peso/calorias
            peso = round((caloria_total - 550) / 15, 2)
            print(f"\nVocê ingeriu calorias para uma pessoa de {peso}kg\n")

        else:
            print("\nVocê já fez um registro hoje!\n")

    def orientacao_nutricional(self, identificador):
        
        # lê o arquivo
        perfil_nutricional = pd.read_csv(self.caminho_perfil_nutricional)

        # confere se o identificador está no arquivo
        if not perfil_nutricional.empty and identificador in str(perfil_nutricional['identificador'].values):

            # obtem as informações da pessoa especifica
            informacoes_aluno = perfil_nutricional.loc[perfil_nutricional['identificador'].astype(str) == identificador]

            # calcula as calorias recomentadas
            calorias_recomendadas = (int(informacoes_aluno['peso_objetivo'][0]) * 15) + 550

            # recomenda alimentos de acordo com as calorias recomendadas
            print(f"\nCalorias recomendadas: {calorias_recomendadas}")
            if calorias_recomendadas <= 1300:
                print("\nprocura ingerir alimentos como: frutas, legumes, proteinas: frango\n")
            elif calorias_recomendadas <= 1600:
                print("\nprocura ingerir alimentos como: grãos integrais, abacate, laticínios, proteinas: peixe, ovos\n")
            elif calorias_recomendadas <= 1900:
                print("\nProcura ingerir alimentos como: azeite de oliva, frutas secas, quinoa, proteinas: carne vermelha\n")
            elif calorias_recomendadas <= 2350:
                print("\nProcura ingerir alimentos como: amêndoas, massa, bacon, queijos mais gordurosos, proteina: salmão\n")
            else:
                print("\nSem muitas restrições...\n")
                
        else:
            print("\nIndentificador não encontrado!\n")

    def acompanhamento_consumo_agua_suplementos(self):
        pass

    def alerta_meta_nutricional(self):
        pass

    def integracao_aplicativo_rastreamento_alimentar(self):
        pass

    def feedback_comunicacao_nutriccionista(self):
        pass


teste = AvaliacaoNutricional()

teste.orientacao_nutricional('123')
teste.orientacao_nutricional('w352566')