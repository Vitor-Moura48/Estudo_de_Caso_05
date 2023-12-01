import inquirer
from model.avaliacao_nutricional import AvaliacaoNutricional
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED
cor_mensagem_ok = Fore.GREEN

monitoramento_producao = AvaliacaoNutricional()
while True:
    perguntas = [
                inquirer.List('opcao',
                            message='Selecione o que deseja fazer',
                            choices=[
                                    ('1 - ', '1'),
                                    ('2 - ', '2'),
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

        pass

    elif opcao == '2':

        pass
        
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