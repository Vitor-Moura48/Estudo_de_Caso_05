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
                                        ('4 - Buscar Orientação Nutricional', '4')
                                        ('5 - ', '5'),
                                        ('6 - ', '6'),
                                        ('7 - Enviar Feedbacks', '7'),
                                        ('8 - Sair do módulo', '8'),
                                        
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
                                inquirer.Text('preferencias', message='Digite suas preferÊncias alimentares'),
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
                                inquirer.Text('data', message='Digite a data'),
                                inquirer.Text('descricao', message='Digite a descrição dos alimentos consumidos'),
                                inquirer.Text('caloria_total', message='Digite as calorias consumadas'),
                                inquirer.Text('consumo_agua', message='Digite a quantidade de água consumida (litros)'),
                                inquirer.Text('suplementos', message='Digite os suplementos utilizados')
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            identificador = respostas_registro['identificador']
            descricao = respostas_registro['descricao']
            caloria_total = float(respostas_registro['caloria_total'])
            consumo_agua = float(respostas_registro['consumo_agua'])
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
            
            pass

        elif opcao == '6':

            pass
            
        elif opcao == '7':
            
            perguntas_registro = [
                                    inquirer.Text('nome', message='Digite sua senha de identificação'),
                                    inquirer.Text('identificador', message='Digite sua senha de identificação'),
                                    inquirer.Text('feedback', message='Digite sua senha de identificação')
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            identificador = respostas_registro['identificador']
            feedback = respostas_registro['feedback']

            avaliacao_nutricional.orientacao_nutricional(nome, identificador, feedback)

        elif opcao == '8':
            print(f'{cor_mensagem_ok}Saindo do módulo...{Style.RESET_ALL}')
            break