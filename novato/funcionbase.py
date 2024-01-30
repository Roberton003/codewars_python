

# Definição da função 'cadastrar'
def cadastrar():
    # Solicita ao usuário se deseja cadastrar um novo usuário
    cadastrar = input("Deseja cadastrar um novo usuário? (S/N) ")
        
    # Se a resposta for 'S' ou 's', prossegue com o cadastro
    if cadastrar.upper() == "S":
         # Solicita o nome do usuário
        nome = input("Digite o nome do usuário: ")
            
        # Solicita o email do usuário
        email = input("Digite o email do usuário: ")
            
        # Solicita a cidade do usuário
        cidade = input("Digite a cidade do usuário: ")
            
        # Retorna uma tupla contendo o nome, email e cidade do usuário
        return nome, email, cidade
    else:
        # Se a resposta não for 'S' ou 's', retorna False
        return False
        
# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Se o script estiver sendo executado diretamente, chama a função 'cadastrar' e imprime o resultado
    print(cadastrar())