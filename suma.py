from concurrent.futures import BrokenExecutor


import numpy as np

array = []
contador = 0
while contador <= 1000:
    num = int(input('Ingresa un número para el array: '))
    opc = int(input('¿Desea agregar más? \n 1: Sí \n 2: No \n'))
    array.append(num)
    suma = np.sum(array)
    if opc == 2:
        print('La suma del array es: ', suma)
        break
    elif opc != 1:
        print('Opción inválida, se sumará el arreglo')
        break
    contador+=1
