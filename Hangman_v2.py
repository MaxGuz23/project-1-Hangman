# Valores iniciales
from numpy import random

reinicio = 's'
while reinicio == 's':

    lista_de_palabras = ['alfabeto','noviembre','ironhack','murcielago','ferrocarril']
    letras_anteriores = []
    letras_adivinadas =[]
    letra_actual = []
    vidas = 3
    palabra = random.choice(lista_de_palabras)
    letras_palabra = []

    for letra in palabra:
        letras_palabra.append(letra)
    def pedir_letra():
        # guardar la letra que nos de el usuario
        letra_actual = input('Dame una letra ').lower()
        while letra_actual in letras_anteriores:
            #repite
            letra_actual = input('Dame otra letra ').lower()

        letras_anteriores.append(letra_actual)        
        return letra_actual

    def acertar_letra(letra_actual, vidas):
        if letra_actual in palabra:
            letras_adivinadas.append(letra_actual) # Sí adivinaste!
    #         vidas = vidas6
            return letras_adivinadas, vidas
        else:
            vidas = vidas - 1
            return letras_adivinadas, vidas



    def esconder_palabra(letras_adivinadas): # 'palabra' ---> '_ _ _ _ _ _ _'

        letra2 = []
        for letra in palabra:
            if letra not in letras_adivinadas:
                letra = '_ '
                letra2.append(letra)
        #         print(letra)
            else:
                letra2.append(letra+' ')
        #         print(letra2)

        return ''.join(letra2)

    while vidas > 0:
        letra_actual = pedir_letra()

        letras_adivinadas, vidas = acertar_letra(letra_actual, vidas)

        print(esconder_palabra(letras_adivinadas),' Te quedan',vidas,'vidas')

        if set(letras_adivinadas) == set(letras_palabra):
            print('\nGANASTEEEE!')
            break
    if vidas == 0:
        print('\nPerdiste :( ')
        
    reinicio = input('Deseas reiniciar? s = sí, n = no ')
