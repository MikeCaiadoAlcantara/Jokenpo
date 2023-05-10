from random import randint
elementos = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
print("Vamos jogar Jokenpo!")
print('''Escolha uma das opções
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int((input("Qual sua jogada?")))
print("O computador jogou {}".format(elementos[computador]))
print("O jogador jogou {}".format(elementos[jogador]))