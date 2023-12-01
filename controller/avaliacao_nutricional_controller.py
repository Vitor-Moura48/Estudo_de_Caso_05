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
                                        ('3 - ', '3'),
                                        ('4 - ', '4')
                                        ('5 - ', '5'),
                                        ('6 - ', '6'),
                                        ('7 - ', '7'),
                                        ('8 - ', '8')
                                        ('9 - Sair do módulo', '9'),
                                        
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
                                inquirer.Text('preferencias', message='novas preferências alimentares'),
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
            
            pass

        elif opcao == '4':

            pass
            
        elif opcao == '5':
            
            pass

        elif opcao == '6':

            pass
            
        elif opcao == '7':
            
            pass

        elif opcao == '8':

            pass
    
        
        elif opcao == '9':
            print(f'{cor_mensagem_ok}Saindo do módulo...{Style.RESET_ALL}')
            break