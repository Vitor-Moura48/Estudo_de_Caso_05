import inquirer
from model.cadastro_acompanhamento_individual import *

ger = CadastroAluno_Acompanhamento()
def run():
   while True:
    perguntas = [
        inquirer.List('opcao',
                      message="Escolha uma opção",
                      choices=[
                            ('1 - Cadastrar Alunos', '1'),
                            ('2 - Chat entre Professor e Aluno', '2'),
                            ('3 - Avaliação ', '3'),
                            ('4 - Personalização Treino', '4'),
                            ('5 - Aluno compareceu ou não', '5'),
                            ('6 - Sair','6')
                      ])]

    
    respostas = inquirer.prompt(perguntas)

    opcao = respostas['opcao']

    if opcao == '1':
        ger.cadastro_alunos()    
    elif opcao == '2':
        resp = int(input("Você é:\n[ 1 ] Professor\n[ 2 ] Aluno\n"))
        if resp == 1:
            nome = input('Digite seu nome: ')
            resp1 = input("Digite o nome do aluno que irá receber a mensagem: ")
            prof = Professor(nome)
            conteudo = input("Escreva sua mensagem: ")
            prof.enviar_mensagem_aluno(resp1, conteudo)
        elif resp == 2:
            resp1 = input("Digite o seu nome: ")
            alu = Aluno(resp1)
            conteudo = input("Conteudo da mensagem: ")
            alu.enviar_mensagem_professor(conteudo)
    elif opcao == '3':
        nome = input("Qual o nome do aluno? ")
        ger.avaliacao_periodica(nome)
        ger.historico(nome)
        ger.relatorios(nome)
    elif opcao == '4':
        nome = input("Qual o nome do aluno? ")
        ger.personalizar(nome)
    elif opcao == '5':
        nome = input("Qual o nome do aluno? ")
        ger.alerta(nome)
    elif opcao == '6':
        break
    else:
        print("Opção inválida. Tente novamente.") 
