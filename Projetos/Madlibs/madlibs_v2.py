"""
    Completar lacunas aleatoriamente em textos ou parágrafos ou frases
"""


def main():
    substantivo = input("Substantivo: ")
    adjetivo1 = input("Adjetivo: ")
    adjetivo2 = input("Adjetivo: ")
    verbo1 = input("Verbo: ")
    verbo2 = input("Verbo: \n")

    madlib = f'''    De que são feitos os {substantivo}? 
    De pequenos desejos, vagarosas saudades, 
    silenciosas lembranças. Entre mágoas {adjetivo1}, 
    momentâneos lampejos: vagas felicidades, 
    {adjetivo2} esperanças. De loucuras, de crimes, 
    de pecados, de glórias
    do medo que {verbo1} todas essas mudanças.
    Dentro deles vivemos, dentro deles {verbo2},
    em duros desenlaces e em sinistras alianças...'''

    print(madlib)


if __name__ == '__main__':
    main()
