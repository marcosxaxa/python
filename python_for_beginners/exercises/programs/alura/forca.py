import random


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for i in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        #get an input from user and remove all blank spaces
        chute = input("Chute uma letra: " ).strip().upper()
        
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            print("Você ainda tem {} tentativas".format(6-erros))
            erros += 1

        # if (erros == 6):
        #     break
        # if ("_" not in letras_acertadas):
        #     break
        # print(letras_acertadas)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu. :(")


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()