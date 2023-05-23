"""Displays the current weather conditions and forecast 
for a user's location.
"""

import requests
import datetime


def buscar_tempo(API_key, nome_cidade, country_code):

    try:
        response = requests.get(
            f'http://api.openweathermap.org/geo/1.0/direct?q={nome_cidade},{country_code}&appid={API_key}')

        print('Carregando...')
        res = response.json()
        lat, lon = res[0]['lat'], res[0]['lon']
        responde_tempo = requests.get(
            f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={API_key}')

        res_tempo = responde_tempo.json()
        lugar = res_tempo['timezone']
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        info = res_tempo['current']['weather'][0]['description']
        temperatura = res_tempo['current']['temp'] - 273.15
        sensacao_termica = res_tempo['current']['feels_like'] - 273.15

        print(f'Lugar: {lugar}')
        print("Hora:", hora)
        print(f'Temperatura: {temperatura:.2f}ºC')
        print(f"Sensação térmica: {sensacao_termica:.2f}ºC")
        print("Descrição tempo:", info)

    except:
        print('Por favor, digite uma cidade válida')


if __name__ == '__main__':

    api_key = '0ea1de193679b14a6c9b0ae362f50dc0'
    nome_cidade = input('Informe o nome da cidade: ')
    country_code = 'BR'
    buscar_tempo(api_key, nome_cidade, country_code)
