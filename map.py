#Imports de las librerías que vamos a usar
import random
import time

#Array con las opciones de movimiento posibles (actualmente 8)
decisions = ['N', 'E', 'S', 'W', 'NE', 'NW', 'SE', 'SW']

#Matriz del mapa, se establece weight y height y se rellena con tierra '_'. Se establece el punto actual del personaje mediante 'O'
w, h = 9, 9
matrix = [['_' for x in range(w)] for y in range(h)]
matrix[8][4] = 'O'
#npcx y npcy son las variables que indican la posición actual del personaje, metax y metay es la meta
npcx = 8
npcy = 4
metax = 0
metay = 0

#Función para mover el personaje. Se pasa como parámetro la dirección en la que se mueve, y esta función se encarga de cambiar 'O', npcx y npcy
def move(eleccion):
    global npcx
    global npcy
    global matrix
    matrix[npcx][npcy] = '_'
    if eleccion == 'N':
        npcx = npcx - 1
    if eleccion == 'E':
        npcy = npcy + 1
    if eleccion == 'S':
        npcx = npcx + 1
    if eleccion == 'W':
        npcy = npcy - 1
    if eleccion == 'NE':
        npcx = npcx - 1
        npcy = npcy + 1
    if eleccion == 'NW':
        npcx = npcx - 1
        npcy = npcy - 1
    if eleccion == 'SE':
        npcx = npcx + 1
        npcy = npcy + 1
    if eleccion == 'SW':
        npcx = npcx + 1
        npcy = npcy - 1
    matrix[npcx][npcy] = 'O'

#Bucle principal de ejecución, se ejecuta indefinidamente (cancela la ejecución con CTRL X o CTRL C, no recuerdo ahora). En el futuro esto nos servirá para
#aprender después de terminar cada ejecución. Se guardará cierta información sobre el comportamiento de cada run, según la cual los futuros runs serán
#teóricamente mas eficientes
while True:
    movimientos = 0

    #Este bucle termina cuando el personaje llega a la meta
    while(matrix[metax][metay] == '_'):

        bucle = 1

        #Aquí se escoge aleatoriamente una dirección en la que moverse y se comprueba si el personaje se va a salir del mapa. Esto se puede cambiar para
        #hacer que muera al salirse o whatever. Sería otro punto de aprendizaje
        while bucle:

            
            index = random.randint(0,len(decisions)-1)

            eleccion = decisions[index]
            if (eleccion == 'N' or eleccion == 'NE' or eleccion =='NW') and npcx == 0:
                bucle = 1
            elif (eleccion == 'S' or eleccion == 'SE' or eleccion =='SW') and npcx == 8:
                bucle = 1
            elif (eleccion == 'E' or eleccion == 'NE' or eleccion =='SE') and npcy == 8:
                bucle = 1
            elif (eleccion == 'W' or eleccion == 'NW' or eleccion =='SW') and npcy == 0:
                bucle = 1
            else:
                bucle = 0

        #Se imprime la matriz actual
        for x in range(w):
            for y in range(h):
                print (matrix[x][y], end='')
            print() #Esto es un salto de línea nada más, para separar las filas

        print()
        print()
        print(eleccion)
        #Se realiza el movimiento en la dirección escogida
        move(eleccion)
        movimientos += 1
        input()

    #Al llegar a la meta, termina una ejecución del bucle y se muestra el número de movimientos que tardó
    print('Done! Number of movements: ' + str(movimientos))
    input() #Dale a enter para seguir con las ejecuciones
