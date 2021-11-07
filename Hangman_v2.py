# Valores iniciales
# Valores iniciales
from numpy import random

reiniciar = 's'
while reiniciar == 's':
    lista_de_palabras = ['alfabeto','noviembre','ironhack','murcielago','ferrocarril']
    letras_anteriores = []
    letras_adivinadas =[]
    letra_actual = []
    vidas = 7
    palabra = random.choice(lista_de_palabras)
    letras_palabra = []



    for letra in palabra:
        letras_palabra.append(letra)

#     def reiniciar():
#         jugar_otravez = []
#         jugar_otravez = input('Reiniciar juego s = Si, n = No')

#         while jugar_otravez not in ['s', 'n']:
#             jugar_otravez = input('Reiniciar juego s = Si, n = No')

#         if jugar_otravez == "s":
#             palabra = random.choice(lista_de_palabras)
#             vidas = 3
#             for letra in palabra:
#                 letras_palabra.append(letra)

#             while vidas > 0:
#                 letra_actual = pedir_letra()

#                 letras_adivinadas, vidas = acertar_letra(letra_actual, vidas)

#                 print(esconder_palabra(letras_adivinadas),' Te quedan',vidas,'vidas')

#                 if set(letras_adivinadas) == set(letras_palabra):
#                     print('\nGANASTEEEE!\n')
#                     break

#                 if vidas == 0:
#                     print('\nPerdiste :( \n')
#                     break

#             reiniciar()

#         elif jugar_otravez == "n":
#             print("Gracias por jugar")
#             exit()
#         else:
#             jugar_otravez = input('Respuesta incorrecta. Reiniciar juego s = Si, n = No')     

    def pedir_letra():
        # guardar la letra que nos de el usuario
        letra_actual = input('Dame una letra ').lower()
        while letra_actual in letras_anteriores:
            #repite
            letra_actual = input('Dame otra letra').lower()

        letras_anteriores.append(letra_actual)        
        return letra_actual

    def acertar_letra(letra_actual, vidas):
        if letra_actual in palabra:
            letras_adivinadas.append(letra_actual) # Sí adivinaste!
    #         vidas = vidas6
            return letras_adivinadas, vidas
        else:
            vidas = vidas - 1
            if vidas == 6:
                print("  _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Letra erronea. " + str(vidas) + " intentos restantes\n")
            elif vidas == 5:
                print("_____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
                print("Letra erronea. " + str(vidas) + " intentos restantes\n")
            elif vidas == 4:
                print("  _____ \n"
                      "  |    | \n"
                      "  |    |\n"
                      "  |    | \n"
                      "  |    O \n"
                      "  |   / \n"
                      "__|__\n")
                print("Letra erronea. " + str(vidas) + " intentos restantes\n")
        return letras_adivinadas, vidas

    def esconder_palabra(letras_adivinadas): # 'palabra' ---> '_ _ _ _ _ _ _'

        letra2 = []
        for letra in palabra:
            if letra not in letras_adivinadas:
                letra = '_ '
                letra2.append(letra)
            else:
                letra2.append(letra+' ')

        return ''.join(letra2)    

    while vidas > 0:
        letra_actual = pedir_letra()

        letras_adivinadas, vidas = acertar_letra(letra_actual, vidas)

        print(esconder_palabra(letras_adivinadas),' Te quedan',vidas,'vidas')

        if set(letras_adivinadas) == set(letras_palabra):
            print('\nGANASTEEEE!\n')
            break

    if vidas == 0:
        print('\nPerdiste :( \n')
        
    reiniciar = input('Reiniciar juego s = Si, n = No')
    
# letras_anteriores = []
# letras_adivinadas = []
# letra_actual = []
# vidas += 3
# letras_palabra = []
# palabra = random.choice(lista_de_palabras)
# # reiniciar()
