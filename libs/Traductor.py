# coding=utf-8
"""
Traducto de palabras realizado con Python
"""

# Importamos la libreria request
import requests

class Traductor:

    traducido = '' # texto traducido
    a_traducir = '' #texto a traducir
    error = '' #mensaje error

    def Traduccion(self, source = '', target = '', text = ''):
        # params:
        # source: idioma origen
        # target: idioma destino
        # text: texto a traducir
        self.error = ''
        self.traducido = ''
        parametros = {'sl': source, 'tl': target, 'q': text}
        cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
        url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
        response = requests.post(url, data=parametros, headers=cabeceras)
        if response.status_code == 200:
            for x in response.json()['sentences']:
                self.traducido = x['trans']
        else:
            self.error = "Ocurrió un error"

        return self.traducido