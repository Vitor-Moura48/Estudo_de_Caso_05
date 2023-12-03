
import smtplib
from collections import defaultdict

class LojaFitness:
    def __init__(self):
        self.produtos = []
        self.clientes = defaultdict(list)
        self.historico_vendas = []
        self.produtos_mais_vendidos = defaultdict(int)
        self.pontos_clientes = defaultdict(int)


# - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - 
  

#_____________________________________#
'''# Função  -  Cadastrar produtos'''
#-------------------------------------#

                        

def cadastrar_novo_produto(loja):
    while True:
        nome_do_produto = input("Digite o nome do produto:\n")
        quantidade_de_produto = input("Digite a quantidade do produto:\n")
        descricao_do_produto = input("Digite a descrição do produto:\n")
        preco_do_produto = input("Digite o preço do produto:\n")

        while True:
            print('1 - PP\n2 - P\n3 - M\n4 - G\n5 - GG')
            tamanho_do_produto = int(input("Digite o tamanho do produto:\n"))
            tamanhos_disponiveis = {1: 'PP', 2: 'P', 3: 'M', 4: 'G', 5: 'GG'}
            tamanho_do_produto = tamanhos_disponiveis.get(tamanho_do_produto)
            if tamanho_do_produto:
                break
            else:
                print("Erro, tente novamente:", '\n' * 5)

        while True:
            print('1 - Roupas de Treino Masculinas\n2 - Roupas de Treino Femininas\n'
                  '3 - Calçados de Treino Unissex\n4 - Acessórios de Treino')
            categoria_do_produto = int(input("Selecione a categoria do produto:\n"))
            categorias_disponiveis = {1: 'Masculinas', 2: 'Femininas', 3: 'Calçados de Treino Unissex', 4: 'Acessórios de Treino'}
            categoria_do_produto = categorias_disponiveis.get(categoria_do_produto)
            if categoria_do_produto:
                break
            else:
                print('Categoria não registrada. Tente novamente!')

        if any([nome_do_produto, quantidade_de_produto, descricao_do_produto, preco_do_produto, tamanho_do_produto]) == '':
            print('Algo deu erro. Tente novamente:\n')
        else:
            # Adicionando um link de imagem fixo como exemplo
            link_imagem = 'link_imagem_fixo'
            loja.cadastrar_produto(nome_do_produto, descricao_do_produto, preco_do_produto, tamanho_do_produto, link_imagem, categoria_do_produto)

        resposta = input("Deseja cadastrar um novo produto? (Digite 'sim' para continuar):\n")
        if resposta.lower() != 'sim':
            break

                                # Exemplo de uso
loja = LojaFitness()
cadastrar_novo_produto(loja)


# - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - 
 
#_______________________________________________________________#
'''# função  -  Visualizar,  comprar e Histórico de produtos'''
#---------------------------------------------------------------#

def comprar_e_armazenar(self, nome_do_cliente):
    print('\n' * 5)
    self.visualizar_produtos()

    try:
        id_selecionado = int(input('\nSelecione o produto que deseja comprar (digite o número do produto):\n'))
        produto_selecionado = self.produtos[id_selecionado - 1]  # Subtraindo 1 para converter para índice da lista
        self.vender_produto(nome_do_cliente, produto_selecionado)
        print(f"\nProduto '{produto_selecionado['Nome']}' vendido para {nome_do_cliente}!")
        
        # Armazenar histórico de vendas
        with open('historico_vendas.txt', 'a') as file:  # 'a' para abrir o arquivo em modo de adição (append)
            file.write(str({'Cliente': nome_do_cliente, 'Produto': produto_selecionado, 'Preço': produto_selecionado['Preço']}) + '\n')
    except (ValueError, IndexError):
        print("Opção inválida. Certifique-se de digitar o número correto do produto.")

                        

                                # Exemplo de uso

loja = LojaFitness()

# Nome do cliente 
nome_do_cliente = "Carlos"

# Chamando a função para comprar e armazenar histórico de vendas
loja.comprar_e_armazenar(nome_do_cliente)


# - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - 

#_________________________________________________#
'''# Função  -  Visualizar histórico de vendas'''
#-------------------------------------------------#

class LojaFitness:


    def visualizar_historico_vendas(self):
        try:
            with open('historico_vendas.txt', 'r') as file:
                historico = file.readlines()
                for venda in historico:
                    print(venda.strip())  # O 'strip()' remove espaços em branco 
        except FileNotFoundError:
            print("Histórico de vendas não encontrado.")

# Exemplo de uso
loja = LojaFitness()
loja.visualizar_historico_vendas()


# - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - 

#___________________________________#
'''# Função  -  Visualizar produtos'''
#-----------------------------------#

                        
def visualizar_produtos(self):
        for produto in self.produtos:
            print(produto)


                                # Exemplo de uso
loja.visualizar_produtos()


# - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - 


#___________________________________#
'''# Função  -   Avaliar produto'''
#-----------------------------------#


def avaliar_produto(self, produto):
    try:
        avaliacao = int(input('\nAvalie o produto que adquiriu de 1 a 10, sendo 10 a melhor avaliação:\n'))
        if (1 <= avaliacao <= 10):
            produto['Avaliacao'] = avaliacao
            print(f"Avaliação para {produto['Nome']}: {avaliacao}")
        else:
            print("Opção inválida. Certifique-se de digitar um número entre 1 e 10.")
    except ValueError:
        print("Opção inválida. Certifique-se de digitar um número inteiro entre 1 e 10.")

                                # Exemplo de uso
loja.avaliar_produto(loja.produtos[0], 4.5)


# - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - 



#_____________________________________________#
'''# Função  -   Trocar pontos por desconto'''
#---------------------------------------------#

class LojaFitness:
    def __init__(self):

        # Dicionário para armazenar pontos dos clientes
        self.pontos_clientes = {}

    # ... outras funções ...

    def trocar_pontos_por_desconto(self, cliente, pontos_para_trocar):
        # Verificar se existe o cliente no cadastro
        if cliente not in self.pontos_clientes:
            print(f"Cliente {cliente} não encontrado.")
            return

        pontos_atuais = self.pontos_clientes[cliente]

        if pontos_atuais < pontos_para_trocar:
            print(f"Cliente {cliente} não tem pontos suficientes para a troca.")
            return

        # Defina a taxa de troca -  1 ponto = 0,10 de desconto
        taxa_troca = 0.10
        valor_desconto = pontos_para_trocar * taxa_troca

        # Atualize os pontos do cliente
        self.pontos_clientes[cliente] -= pontos_para_trocar

        print(f"Troca de pontos bem-sucedida para o cliente {cliente}.\n Desconto de R${valor_desconto:.2f} aplicado.")




                            # Exemplo de uso
loja = LojaFitness()
loja.pontos_clientes = {'Carlos': 50, 'Jonas': 30, 'Gustavo': 20}# isso já vai estar no banco de dados


# Aqui vou precisar o nome do cliene e quantos pontos ele tem
cliente_para_trocar = 'Carlos'
pontos_para_trocar = 20

loja.trocar_pontos_por_desconto(cliente_para_trocar, pontos_para_trocar)

