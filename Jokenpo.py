from random import randint
from time import sleep
elementos = ("pedra", "papel", "tesoura")
computador = randint(0, 2)
print("Vamos jogar Jokenpo!")
sleep(1)
print('''Escolha uma das opções
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int((input("Qual sua jogada?")))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("_" * 25)
print("O computador jogou {}".format(elementos[computador]))
print("O jogador jogou {}".format(elementos[jogador]))
print("_" * 25)

if computador == 0:  #PEDRA
	if jogador == 0:
		print("Empatou!")
	elif jogador == 1:
		print("O jogador venceu!")
	elif jogador == 2:
		print("O computador venceu")
	else:
		print("Jogada inválida!")

elif computador == 1:  #PAPEL
	if jogador == 0:
		print("O computador venceu!")
	elif jogador == 1:
		print("Empatou")
	elif jogador == 2:
		print("O jogador venceu!")
	else:
		print("Jogada inválida!")

elif computador == 2:  #TESOURA
	if jogador == 0:
		print("O jogador venceu!")
	elif jogador == 1:
		print("O computador venceu!")
	elif jogador == 2:
		print("Empatou!")
	else:
		print("Jogada inválida!")