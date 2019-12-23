
import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randint(1,100)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil\n (2) Médio\n (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    for rodada in range(1,total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e tem agora {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu número é maior do que o número secreto!")
            elif(menor):
                print("Você errou! O seu número é menor do que o número secreto!")
            pontos_perdidos =  abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("O número secreto era {} e você tem agora {} pontos restantes de 1000".format(numero_secreto, pontos))

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()