'''           Módulo 2 - Mod Fitness       '''

'email.feiki.feikiiii@gmail.com'
'emailfeiki'
###################################################################################################

#   Cadastro de produtos
#   Descrição / Preço / Tamanho / Imagens







###################################################################################################


#   registrar historico de compra
#   Preferência de estilo / cores favoritas / tamanhos
#   de acordo a cada compra o perfil é atualizado




###################################################################################################


#   promoções persnalizadas com base no histórico de compras e preferência
#   receber notificações automáticas quando há promocões

#   Lista de desejos

#   notificar quando o item que estiver na lista de desejos estiverem na promoção

#   Aviso de novos produtos com base na coleçãonas preferência de estilo

#   integrar com o sistema de pagamento
#   visualizae e pagar direto do sistema


#   Status de entrega do pedido em tempo real

#   programa de fidelidade, acumular pontos a cada compra podendo gerar descontos ou brindes
#   cadastrar brindes

#   avaliar produtos

#   gestão de estoque, evitar vendas de produtos fora de estoque... 
#   vizualização precisa do iventário



'''                     Primeiro fazer as funções:            '''

# Cadastrar produtos (descrição, preço, imagem, tamanho) - avisar quanto tiver novo produto
# Avaliar produtos
# Comprar produtos - Remover produto do iventário - Adicionar pontos
# Salvar produto nos favoritos
# Gastar pontos - converter em desconto ou trocar em brindes - apagar pontos
# Visualizar estoque (estilo tabela pandas)

# Promoção - avisar se o item estiver na lista de desejo ou se já tiver comprado produtos de mesma caracteeristicas - avisar só por email (falso)

# Perfil de compra do aluno - histórico de compra - classe ou lista de preferencias a medida que for comprando irá atualizando


import smtplib
from collections import defaultdict

class LojaFitness:
    def __init__(self):
        self.produtos = []
        self.clientes = defaultdict(list)
        self.historico_vendas = []
        self.produtos_mais_vendidos = defaultdict(int)
        self.pontos_clientes = defaultdict(int)

    def cadastrar_produto(self, nome, descricao, preco, tamanho, imagem, categoria):
        produto = {'Nome': nome, 'Descrição': descricao, 'Preço': preco, 'Tamanho': tamanho, 'Imagem': imagem, 'Categoria': categoria}
        self.produtos.append(produto)
        self.verificar_compras_recentes(produto)

    def visualizar_produtos(self):
        for produto in self.produtos:
            print(produto)

    def vender_produto(self, cliente, produto):
        if produto in self.produtos:
            self.historico_vendas.append({'Cliente': cliente, 'Produto': produto, 'Preço': produto['Preço']})
            self.produtos_mais_vendidos[produto['Nome']] += 1
            self.pontos_clientes[cliente] += 10 #Aqui é onde fica os pontos das compras
            print(f"Venda realizada para {cliente}.")
        else:
            print("Produto não encontrado.")

    def avaliar_produto(self, produto, avaliacao):
        produto['Avaliacao'] = avaliacao
        print(f"Avaliação para {produto['Nome']}: {avaliacao}")

    def armazenar_historico_vendas(self):
        with open('historico_vendas.txt', 'w') as file:
            for venda in self.historico_vendas:
                file.write(str(venda) + '\n')

    def verificar_compras_recentes(self, produto):
        for cliente, compras in self.clientes.items():
            for compra in compras:
                if compra['Categoria'] == produto['Categoria'] and compra['Tamanho'] == produto['Tamanho']:
                    print(f"Cliente {cliente} comprou recentemente um produto similar. Pode estar interessado.")

    def atribuir_pontos(self, cliente, pontos):
        self.pontos_clientes[cliente] += pontos

    def trocar_pontos_por_desconto(self, cliente, pontos):
        desconto = min(pontos, self.pontos_clientes[cliente])
        self.pontos_clientes[cliente] -= desconto
        return desconto

    def enviar_email_promocao(self):
        produtos_promocionais = [produto for produto, quantidade in sorted(self.produtos_mais_vendidos.items(), key=lambda x: x[1], reverse=True)[:3]]
        mensagem = f"Olá! Você é um cliente especial e merece um desconto. Produtos em promoção: {', '.join(produtos_promocionais)}"
        self.enviar_email(cliente, "Oferta Especial", mensagem)

    def enviar_email(self, destinatario, assunto, mensagem):
        # Lógica para enviar e-mail. Aqui, é necessário configurar o servidor SMTP.
        pass

    def exibir_status_entrega(self, cep):
        # Lógica para determinar o status de entrega com base no CEP.
        pass

# Exemplo de uso:
loja = LojaFitness()

# Cadastrar produtos
loja.cadastrar_produto("Camiseta DryFit Pro", "Camiseta masculina de alta performance", 79.90, 'M', 'link_imagem_camiseta', 'Roupas de Treino Masculinas')
loja.cadastrar_produto("Top DryFlex", "Top feminino confeccionado com tecido DryFlex", 69.90, 'P', 'link_imagem_top', 'Roupas de Treino Femininas')

# Visualizar produtos
loja.visualizar_produtos()

# Vender produto
loja.vender_produto("ClienteA", loja.produtos[0])

# Avaliar produto
loja.avaliar_produto(loja.produtos[0], 4.5)

# Armazenar histórico de vendas
loja.armazenar_historico_vendas()

# Verificar compras recentes
loja.verificar_compras_recentes(loja.produtos[0])

# Atribuir pontos
loja.atribuir_pontos("ClienteA", 20)

# Trocar pontos por desconto
desconto = loja.trocar_pontos_por_desconto("ClienteA", 10)
print(f"Desconto aplicado: {desconto}")

# Enviar e-mail de promoção
loja.enviar_email_promocao()

# Exibir status de entrega
loja.exibir_status_entrega("12345")

