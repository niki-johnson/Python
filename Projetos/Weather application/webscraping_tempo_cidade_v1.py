"""Displays the current weather conditions and forecast 
for a user's location.
"""

from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def encontrar_tempo(nome_cidade):
    nome_cidade = nome_cidade.replace(' ', '+')

    try:
        res = requests.get(
            f'https://www.google.com/search?q={nome_cidade}&oq={nome_cidade}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        print("Carregando...")

        soup = BeautifulSoup(res.text, 'html.parser')
        lugar = soup.select('#wob_loc')[0].get_text().strip()
        hora = soup.select('#wob_dts')[0].get_text().strip()
        info = soup.select('#wob_dc')[0].get_text().strip()
        temperatura = soup.select('#wob_tm')[0].get_text().strip()

        print("Lugar:", lugar)
        print("Temperatura:", temperatura, 'ºC')
        print("Hora:", hora)
        print("Descrição tempo:", info)
    except:
        print("Por favor, entre com um nome de cidade válido")


if __name__ == '__main__':
    nome_cidade = input('Informe o nome da cidade: ')
    nome_cidade = nome_cidade + 'tempo'
    encontrar_tempo(nome_cidade)
