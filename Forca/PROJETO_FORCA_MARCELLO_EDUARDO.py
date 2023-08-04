import random
import easygui

# Leitura das palavras do arquivo
with open("Forca.txt") as f:
    palavras = [palavra.strip() for palavra in f.readlines()]

# Boneco da forca
boneco = [
    """
    +---+
        |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """
]

# Dicionário de dificuldades
dificuldades_boneco = {
    "Normal": [2, 3, 4, 5, 6, 7],
    "Tormento": [3, 5, 6, 7],
    "Inferno": [5, 7],
    "Nightmare": [7]
}


# Função para selecionar palavra aleatória
def get_palavra():
    return random.choice(palavras)


# Função para obter a dificuldade do jogo
def get_dificuldade():
    escolhas = ["Normal", "Tormento", "Inferno", "Nightmare"]
    escolha = easygui.choicebox("Selecione a dificuldade:", "Jogo da Forca", escolhas)
    if escolha:
        return escolha, dificuldades_boneco[escolha]


# Loop externo para jogar novamente ou sair
while True:
    palavra = get_palavra().upper()
    dificuldade, bonecos_dificuldade = get_dificuldade()
    tentativas_restantes = len(bonecos_dificuldade)
    letras_adivinhadas = set()
    while tentativas_restantes > 0:
        # Montagem da palavra oculta
        palavra_oculta = "".join([letra if letra in letras_adivinhadas else " _" for letra in palavra])

        if "_" not in palavra_oculta:
            easygui.msgbox(f"Você venceu! A palavra era '{palavra}'!", "Jogo da Forca")
            break

        # Exibição da interface gráfica
        mensagem = f"Palavra: {palavra_oculta}\n\nTentativas restantes: {tentativas_restantes}\n\nLetras já utilizadas: {' '.join(letras_adivinhadas)}\n\n{boneco[bonecos_dificuldade[-tentativas_restantes]]}"
        palpite = easygui.enterbox(mensagem, "Jogo da Forca")

        # Verificação da letra digitada pelo usuário
        if palpite and palpite.isalpha():
            palpite = palpite.upper()
            if palpite in letras_adivinhadas:
                easygui.msgbox("Você já utilizou esta letra antes!", "Jogo da Forca")
            elif palpite in palavra:
                letras_adivinhadas.add(palpite)
                if set(palavra) == letras_adivinhadas:
                    easygui.msgbox(f"Você venceu! A palavra era '{palavra}'!", "Jogo da Forca")
                    break
            else:
                letras_adivinhadas.add(palpite)
                tentativas_restantes -= 1
        else:
            if palpite:
                easygui.msgbox("Digite apenas uma letra!", "Jogo da Forca")

    if tentativas_restantes == 0:
        easygui.msgbox(f"{boneco[0]}\nVocê perdeu! A palavra era '{palavra}'", "Jogo da Forca")

    # Pergunta se o usuário deseja jogar novamente ou sair
    escolha = easygui.ynbox("Deseja jogar novamente?", "Jogo da Forca", ("Sim", "Não"))
    if not escolha:
        break
