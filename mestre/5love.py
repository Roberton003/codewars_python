# Importando a biblioteca random
import random

# Lista de linguagens do amor
LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]

class Partner:
    def __init__(self, main_lang):
        """
        Classe que representa um parceiro.
        
        Args:
            main_lang (str): A linguagem principal do parceiro.
        """
        self.main_lang = main_lang
        self.tests_left = 50

    def response(self, language):
        """
        Retorna a resposta do parceiro para uma determinada linguagem.
        
        Args:
            language (str): A linguagem para a qual o parceiro está respondendo.
        
        Returns:
            str: "positive" se a resposta for positiva, "neutral" caso contrário.
        """
        if self.tests_left > 0:
            self.tests_left -= 1
            return "positive" if language == self.main_lang else "neutral"
        else:
            return "neutral"

def love_language(partner, n_weeks):
    """
    Função que calcula a linguagem principal do parceiro após um determinado número de semanas.
    
    Args:
        partner (Partner): O objeto Partner representando o parceiro.
        n_weeks (int): O número de semanas.
    
    Returns:
        str: A linguagem principal do parceiro.
    """
    # Calculando o número de verificações por semana
    verificacoes_por_semana = max(1, min(7 // (n_weeks * len(LOVE_LANGUAGES)), 7))
    
    # Dicionário para armazenar as respostas do parceiro para cada linguagem
    responses = {language: 0 for language in LOVE_LANGUAGES}

    # Loop para simular as semanas
    for _ in range(n_weeks):
        # Loop para simular as verificações por semana
        for _ in range(verificacoes_por_semana):
            # Loop para percorrer as linguagens do amor
            for language in LOVE_LANGUAGES:
                # Obtendo a resposta do parceiro para a linguagem atual
                response = partner.response(language)
                if response == "positive":
                    # Incrementando o contador de respostas positivas para a linguagem atual
                    responses[language] += 1

    # Obtendo a linguagem principal com base nas respostas do parceiro
    main_language = max(responses, key=responses.get)
    return main_language

# Loop para simular 40 vezes
for _ in range(40):
    # Gerando um número aleatório de semanas
    n_weeks = random.randint(4, 9)
    
    # Criando um objeto Partner com uma linguagem aleatória
    partner = Partner(random.choice(LOVE_LANGUAGES))
    
    # Calculando a linguagem principal após o número de semanas
    main_language = love_language(partner, n_weeks)
    
    # Imprimindo a linguagem principal após o número de semanas
    print(f"Main language after {n_weeks} weeks: {main_language}")
