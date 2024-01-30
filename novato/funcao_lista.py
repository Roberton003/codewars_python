   # Importa o módulo random para gerar números aleatórios
import random

# Define a função gerar_codigos
def gerar_codigos():
    # Cria uma lista com as categorias de produtos
    categorias = ['Bebida Alcoolica', 'Bebida Não Alcoolica', 'Alimentos', 'Limpeza Geral', 'Frios']
    
    # Cria uma lista vazia para armazenar os códigos dos produtos
    produtos = []

    # Gera 30 códigos de produtos
    for i in range(30):
        # Escolhe uma categoria aleatória
        categoria = random.choice(categorias)
        
        # Gera um código para o produto
        codigo = f"{categoria[:3].upper()}{random.randint(100, 999)}"
        
        # Adiciona o código do produto à lista de produtos
        produtos.append((categoria, codigo))

    # Retorna a lista de produtos
    return produtos

# Define a função eh_da_catergoria
def eh_da_catergoria(produto, categoria):
    # Converte a categoria para maiúsculas e pega as três primeiras letras
    categoria = categoria.upper()[:3]
    
    # Verifica se o código do produto começa com as letras da categoria
    if produto[1].startswith(categoria):
        # Se sim, retorna True
        return True
    else:
        # Se não, retorna False
        return False

# Gera os códigos dos produtos
produtos = gerar_codigos()

# Para cada produto na lista de produtos
for produto in produtos:
    # Verifica se o produto é uma bebida alcoólica
    if eh_da_catergoria(produto, 'Bebida Alcoolica'):
        # Se sim, imprime o produto e a categoria
        print(produto, 'bebida alcoolica')
    # Verifica se o produto é uma bebida não alcoólica
    elif eh_da_catergoria(produto, 'Bebida não Alcoolica'):
        # Se sim, imprime o produto e a categoria
        print(produto, 'bebida não Alcoolica')

qtde_bebidas_alcoolicas = len([produto for produto in produtos if eh_da_catergoria(produto, 'Bebida Alcoolica')])
print(f"Quantidade de bebidas alcoólicas: {qtde_bebidas_alcoolicas}")