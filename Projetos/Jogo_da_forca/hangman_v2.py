import random


def gerar_palavra():
    with open('Lista-de-Palavras.txt') as palavras:

        lst_palavras = [registro.strip() for registro in palavras]

    while True:
        palavra_desafio = random.choice(lst_palavras)
        if "-" not in palavra_desafio and " " not in palavra_desafio:
            break

    return palavra_desafio.lower()


def main():

    desafio = gerar_palavra()
    palavra_user = ["_" for _ in range(0, len(desafio))]
    palavra_formada_str = ''.join(palavra_user)
    letras_escolhidas = []
    vidas = 10

    print(
        f'\nBem vindo ao Jodo Da Forca!!\nA palavra desafio tem {len(desafio)} letras.\nVocê tem {vidas} vidas\nObs: Pressione 0 a qualquer momento para desistir')

    while True:
        # recebendo letra do usuario e verificando se ela ja foi usada e guardando
        while True:
            tentativa = input("Letra: ")
            if tentativa not in letras_escolhidas:
                letras_escolhidas.append(tentativa)
                break
            else:
                print(
                    f'Letra já selecionada.\n Letras ja escolhidas: {letras_escolhidas}\nTente outra\n')

        print("Letras já usadas: ", letras_escolhidas)

        vidas = vidas - 1 if letras_escolhidas[-1] not in desafio else vidas

        for i in range(0, len(desafio)):
            if letras_escolhidas[-1] == desafio[i]:
                palavra_user[i] = letras_escolhidas[-1]
                palavra_formada_str = ''.join(palavra_user)

        if vidas < 4 and vidas > 0:
            print(f'Últimas chances: Você tem {vidas} vida(s)')
        elif vidas == 0:
            print(f'Você perdeu :(\nA palavra era {desafio}')
            break
        elif "_" not in palavra_formada_str:
            print(f'Você acertou a palavra {desafio}')
            break
        elif letras_escolhidas[-1] == '0':
            print(
                f'Poxa! Que pena que você desistiu. Vai conseguir na próxima ;) \nA palavra era {desafio}')
            break

        print("Tentativa:", palavra_formada_str)


if __name__ == '__main__':
    main()
    print("\nMe diverti bastante. Até a próxima!")
