import random
from colorama import Fore
from colorama import Style
from colorama import just_fix_windows_console
just_fix_windows_console()

#---------------------------------------------------------------------
#EFICIENCIA: linea 43
#---------------------------------------------------------------------

puntaje = 0
juegos_total = 0

p = {
        4: 'palabras4.txt',
        5: 'palabras5.txt',
        6: 'palabras6.txt',
        7: 'palabras7.txt',
        8: 'palabras8.txt'}

palabras4 = set(line.strip() for line in open(p[4], encoding="UTF8"))#O(M), M es el tamaño de todo el lemario
palabras5 = set(line.strip() for line in open(p[5], encoding="UTF8"))
palabras6 = set(line.strip() for line in open(p[6], encoding="UTF8"))
palabras7 = set(line.strip() for line in open(p[7], encoding="UTF8"))
palabras8 = set(line.strip() for line in open(p[8], encoding="UTF8"))

lista_lemario4 =tuple( [line.strip() for line in open(p[4], encoding="UTF8")])#O(M)
lista_lemario5 =tuple( [line.strip() for line in open(p[5], encoding="UTF8")])
lista_lemario6 =tuple( [line.strip() for line in open(p[6], encoding="UTF8")])
lista_lemario7 =tuple( [line.strip() for line in open(p[7], encoding="UTF8")])
lista_lemario8 =tuple( [line.strip() for line in open(p[8], encoding="UTF8")])

print("BIENVENIDO A WORDLE")
print("")
print("Las reglas son simples: adivina la palabra oculta en 6 intentos. Cada intento debe ser una palabra válida y si la palabra no existe el juego te avisará.")
print("Después de cada intento el color de las casillas cambia para mostrar qué tan cerca estás de acertar la palabra.")
print(f"{Fore.GREEN}*VERDE{Style.RESET_ALL} significa que la letra está en la palabra y en la posición CORRECTA.")
print(f"{Fore.YELLOW}*AMARILLO{Style.RESET_ALL} significa que la letra está presente en la palabra pero en la posición INCORRECTA")
print("*BLANCO significa que la letra NO está en la palabra.")
print("")

#M+N(X+H*X)=M+N(H*X)
#siendo X=8(el peor caso),H=6 si se pierden todas y N=100, seria un total de <<4800, lo cual es parecido al lemario actual


def juego1():#O(N)(                            N=numero de partidas
    
    dificultad = int(
        input("Ingrese el nivel de dificultad (número entero entre 4-8): "))
    
    if dificultad == 4:
        palabra_elegida = lista_lemario4[random.randint(0,len(lista_lemario4) -1)]  # O(1)
        set_seleccionado=palabras4
    elif dificultad == 5:
        palabra_elegida = lista_lemario5[random.randint(0,len(lista_lemario5) -1)]  # O(1)
        set_seleccionado=palabras5
    elif dificultad == 6:
        palabra_elegida = lista_lemario6[random.randint(0,len(lista_lemario6) -1)]  # O(1)
        set_seleccionado=palabras6
    elif dificultad == 7:
        palabra_elegida = lista_lemario7[random.randint(0,len(lista_lemario7) -1)]  # O(1)
        set_seleccionado=palabras7
    elif dificultad == 8:
        palabra_elegida = lista_lemario8[random.randint(0,len(lista_lemario8) -1)]  # O(1)
        set_seleccionado = palabras8

    list_palabra_elegida = list(palabra_elegida)#O(X)  x es el tamaño de la palabra

    
    def juego(set1, numero):
        intentos = 0
 
        
        while intentos < 6: #O(H) # H es el número de intento
            verde=[]
            amarillo=[]
            print("")
            print(f"Intento número {intentos+1}")
            print("Ingrese la palabra, todo en minúsculas y sin tilde:") 
            entrada = input()
            letras_palabra_elegida = {} # O(1)
            letras_palabra_insertada = {} # O(1)
            if entrada not in set1:#O(1)
                print("")
                print(
                    "Intento no válido, la palabra no existe en el español o no se encuentra en el lemario. Por favor ingrese otra palabra "
                )
            else:
                if entrada == palabra_elegida:
                    print(f"{Fore.GREEN}{palabra_elegida.upper()}{Style.RESET_ALL}")
                    print()
                    print("¡Ganaste!")
                    global puntaje
                    puntaje += 1
                    global juegos_total
                    juegos_total += 1
                    break
                else:
                    entrada = list(entrada)#O(X)
                    #list_palabra_elegida

                    # Crear un diccionario con el número de ocurrencias de cada letra de la palabra elegida
                    for p in palabra_elegida: #O(X)
                        letras_palabra_elegida[p] = letras_palabra_elegida.get(p, 0) + 1
                        
                    for p in entrada: #O(X)
                        letras_palabra_insertada[p] = letras_palabra_insertada.get(p, 0) + 1

                    for mm in range(dificultad):#O(X)
                        if entrada[mm]==list_palabra_elegida[mm]:#O(1)
                            verde.append("verde")#O(1)
                            letras_palabra_elegida[entrada[mm]] = letras_palabra_elegida.get(entrada[mm], 0) -1#(O(1))
                        else:
                            verde.append("_")


                            
                    for nn in range(dificultad):#O(X)
                        if entrada[nn] in letras_palabra_elegida:
                            if verde[nn]=="_":#O(1)
                                if letras_palabra_elegida[entrada[nn]]>0:#O(1)
                                    letras_palabra_elegida[entrada[nn]]=letras_palabra_elegida.get(entrada[nn], 0) -1#O(1)
                                    amarillo.append("amarillo")#O(1)
                                else:
                                    amarillo.append("_")#O(1)
                            else:
                                amarillo.append("_")#O(1)
                        else:
                            amarillo.append("_")#O(1)
                
                    for vv in range(dificultad):
                        if verde[vv]!="_":#O(1)
                            print(f'{Fore.GREEN}{entrada[vv].upper()}{Style.RESET_ALL}',end="")
                        elif amarillo[vv]!="_":#O(1)
                            print(f'{Fore.YELLOW}{entrada[vv].upper()}{Style.RESET_ALL}',end="")
                        else:
                            print(entrada[vv].upper(),end="")

                    intentos += 1

                    print("")
                    
        if intentos == 6:
            print("")
            print("!Perdiste!")
            print(f"La palabra correcta era: {Fore.RED}{palabra_elegida.upper()}{Style.RESET_ALL}")
            juegos_total+=1
    
    juego(set_seleccionado,dificultad)
    print("")
    
    repetir = input("¿Quieres jugar otra vez? (responda 'si' o 'no' por favor): ")
    print("")
    if repetir == "si":
        print("")
        juego1()
        
    else:
        print(f"Has ganado {puntaje} de {juegos_total} juegos")

juego1()

