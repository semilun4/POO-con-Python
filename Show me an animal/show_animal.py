# Programa show me an animal.
# De la mentoria Introduccion a Poo
from black import main
import animales

#print(animales.bird)

menu = {
    '1': '1. Gato',
    '2': '2. Perro',
    '3': '3. Ave',
    '4': '4. Python',
    '0': '0. Exit'
}

class Animal:
    def __init__(self,type):
        self.type = type

    def mostrar_animal(self):
        #getattr toma los atributos de un obj que no esta definido
        animal_ascii = getattr(animales, self.type)
        return animal_ascii

if __name__ == '__main__':
    for option in menu:
        print(menu.get(option))

    while True:    
        seleccion = int(input('Ingresa una opcion: '))
        if seleccion == 0:
            print('Adiós :D')
            break 
        elif str(seleccion) in menu:
            menu_value = menu.get(str(seleccion))
            animal_type= (menu_value.split(' ')[1])
            animal = Animal(animal_type)
            dibujo = animal.mostrar_animal()
            print(dibujo)
        else: 
            print('Opcion invalida')
