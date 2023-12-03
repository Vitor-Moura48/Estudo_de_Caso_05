import inquirer
from model.avaliacao_nutricional import AvaliacaoNutricional
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED
cor_mensagem_ok = Fore.GREEN

avaliacao_nutricional = AvaliacaoNutricional()

def run():
    while True:
        perguntas = [
                    inquirer.List('opcao',
                                message='Selecione o que deseja fazer',
                                choices=[
                                        ('1 - Cadastrar Perfil Nutricional', '1'),
                                        ('2 - Alterar Pefil Nutricional', '2'),
                                        ('3 - Fazer Registro de Dieta Diario', '3'),
                                        ('4 - Buscar Orientação Nutricional', '4'),
                                        ('5 - Buscar Informações sobre alimentos', '5'),
                                        ('6 - Enviar Feedbacks', '6'),
                                        ('7 - Sair do módulo', '7')
                                        ]
                                )
                    ]
        respostas = inquirer.prompt(perguntas)

        # Verifica se as respostas são nulas
        if respostas is None:
            raise KeyboardInterrupt
        
        opcao = respostas['opcao']

        # Aqui temos uma estrutura de decisão para cada opção do menu
        if opcao == '1':

            perguntas_registro = [
                                inquirer.Text('nome', message='Digite o nome'),
                                inquirer.Text('identificador', message='Digite uma senha de identificação'),
                                inquirer.Text('habitos', message='Digite seus habitos alimentares'),
                                inquirer.Text('restricoes', message='Digite suas restrições alimentares'),
                                inquirer.Text('peso_objetivo', message='Digite seu pesso objetivo'),
                                inquirer.Text('preferencias', message='Digite suas preferências alimentares'),
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            identificador = respostas_registro['identificador']
            habitos = respostas_registro['habitos']
            restricoes = respostas_registro['restricoes']
            peso_objetivo = respostas_registro['peso_objetivo']
            preferencias = respostas_registro['preferencias']

            avaliacao_nutricional.cadastrar_perfil_nutricional(nome, identificador, habitos, restricoes, peso_objetivo, preferencias)

        elif opcao == '2':

            perguntas_registro = [
                                inquirer.Text('identificador', message='Digite sua senha de identificação'),
                                inquirer.Text('nome', message='novo nome'),
                                inquirer.Text('habitos', message='novos habitos alimentares'),
                                inquirer.Text('restricoes', message='novas restrições alimentares'),
                                inquirer.Text('peso_objetivo', message='novo pesso objetivo'),
                                inquirer.Text('preferencias', message='novas preferências alimentares')
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            identificador = respostas_registro['identificador']
            habitos = respostas_registro['habitos']
            restricoes = respostas_registro['restricoes']
            peso_objetivo = respostas_registro['peso_objetivo']
            preferencias = respostas_registro['preferencias']

            avaliacao_nutricional.alterar_perfil_nutricional(nome, identificador, habitos, restricoes, peso_objetivo, preferencias)

            
        elif opcao == '3':
            
            perguntas_registro = [
                                inquirer.Text('nome', message='Digite o nome'),
                                inquirer.Text('identificador', message='Digite sua senha de identificação'),
                                inquirer.Text('descricao', message='Digite a descrição dos alimentos consumidos'),
                                inquirer.Text('caloria_total', message='Digite as calorias consumadas'),
                                inquirer.Text('consumo_agua', message='Digite a quantidade de água consumida (litros)'),
                                inquirer.Text('suplementos', message='Digite os suplementos utilizados')
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            identificador = respostas_registro['identificador']
            descricao = respostas_registro['descricao']

            try:
                caloria_total = float(respostas_registro['caloria_total'])
                consumo_agua = float(respostas_registro['consumo_agua'])
            except:
                print(f"\n{cor_mensagem_erro}Digite valores adequados!{Style.RESET_ALL}\n")
                break

            suplementos = respostas_registro['suplementos']

            avaliacao_nutricional.registro_dieta_diario(nome, identificador, descricao, caloria_total, consumo_agua, suplementos)

        elif opcao == '4':

            perguntas_registro = [
                                    inquirer.Text('identificador', message='Digite sua senha de identificação')
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            identificador = respostas_registro['identificador']

            avaliacao_nutricional.orientacao_nutricional(identificador)
            
        elif opcao == '5':
            
            perguntas_registro = [
                                    inquirer.Text('busca', message='Digite o alimento que deseja')
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            busca = respostas_registro['busca']

            avaliacao_nutricional.rastreamento_alimentar(busca)

        elif opcao == '6':
            
            perguntas_registro = [
                                    inquirer.Text('nome', message='Digite seu nome'),
                                    inquirer.Text('identificador', message='Digite sua senha de identificação'),
                                    inquirer.Text('feedback', message='Digite seu feedback')
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            identificador = respostas_registro['identificador']
            feedback = respostas_registro['feedback']

            avaliacao_nutricional.feedback_comunicacao_nutricionista(nome, identificador, feedback)

        elif opcao == '8':
            print(f'{cor_mensagem_ok}Saindo do módulo...{Style.RESET_ALL}')
            break