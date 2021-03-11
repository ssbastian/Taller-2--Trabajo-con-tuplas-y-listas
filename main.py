"""
@author: juan sebastian sanchez pizo

"""
import os


def imprimir():
    print('\n\n\n\n-----------Lista de contactos---------')
    print('\t1...Adicionar contactos')
    print('\t2...Eliminar contacto')
    print('\t3...Listar contactos')
    print('\t4...Buscar Contacto')
    print('\t5...Modificar nombre contacto')
    print('\t6...Modificar o eliminar numero de telefono')
    print('\t7...Salir')
    return int(input('Digite su Opcion..'))


lista_contactos = list()
op = 0
while (op < 7):
    op = imprimir()

    if (op == 1):  # agregar contacto
        nombre_contacto = input('Digite nombre de contacto :')
        numero_contacto = input('Digite Numero de contacto :')
        dato_contacto = False
        posicion = 0

        for c in lista_contactos:
            if (list(c)[0] == nombre_contacto):
                print("El Contacto ya esta registrado desea agregar otro numero")
                num = int(input('-> Digite 1 si desea agregar otro numero al contacto:'))  # recibir otro numero
                if (num == 1):
                    dato_contacto = True
                    posicion = lista_contactos.index(c)

        if (dato_contacto):  # contacto existente
            aux = list(lista_contactos[posicion])
            aux.append(numero_contacto)
            lista_contactos[posicion] = tuple(aux)
            print("Contacto agregado exitosamente")
        else:  # contacto nuevo
            datos_contacto = nombre_contacto, numero_contacto
            lista_contactos.append(datos_contacto)

    if (op == 2):  # eliminar contacto
        if (len(lista_contactos) == 0):  # validar que halla contactor regis....
            print("___PRIMERO DEBE REGISTRAR LOS CONTACTOS_______")
            continue
        nombre_eliminar = input('Digite nombre de contacto :')
        for n in lista_contactos:
            if (list(n)[0] == nombre_eliminar):  # La función List convierte una tupla a una lista
                lista_contactos.remove(n)
            else:
                print('Contacto no encontrado ')
    if (op == 3):  # mostrar contacto
        print(' -------- Lista de contactos -------')
        for c in lista_contactos:
            nombre = list(c)[0]
            print('Nombre : {}'.format(nombre))
            print(' ---- Numeros : ', list(c[1:]))

    if (op == 4):
        encuentra = False
        posicionX = 0

        if (len(lista_contactos) == 0):  # validar que halla contactor regis....
            print("___PRIMERO DEBE REGISTRAR LOS CONTACTOS_______")
            continue

        print('\n\n\n\n')
        print('\t1. Buscar por nombre')
        print('\t2. Buscar por numero')
        print('\t0. volver ')
        num = int(input('-> Digite el numero: '))  # recibir otro numero
        if (num == 1):
            buscar = input('Digite nombre de contacto :')  # buscar por nombre
            for n in lista_contactos:
                if (list(n)[0] == buscar):  # La función List convierte una tupla a una lista
                    encuentra = True
                    posicionX = lista_contactos.index(n)
        elif (num == 2):
            buscar = input('Digite numero de contacto a buscar :')  # Buscar por numero
            for n in lista_contactos:
                for i in range(len(lista_contactos)):

                    if (list(n)[i+1] == int(buscar)):  # La función List convierte una tupla a una lista
                        encuentra = True
                        posicionX = lista_contactos.index(n)

        if (encuentra):
            print('contacto encontrado:  {} Numero {}'.format(lista_contactos[posicionX][0], lista_contactos[posicionX][1]))
        else:
            print('Contacto no Existe')

    if (op == 5):
        dato_contacto = False
        posicion = 0 #para guardar indice
        nombre_contacto = input('Digite nombre de contacto :')

        for c in lista_contactos:
            if (list(c)[0] == nombre_contacto):
                dato_contacto = True
                posicion = lista_contactos.index(c)

        if (dato_contacto):  # contacto existente
            nombre_contacto = input('Digite el nuevo nombre de contacto :')
            aux = list(lista_contactos[posicion])
            aux.pop(0)
            aux.insert(0, nombre_contacto)
            lista_contactos[posicion] = tuple(aux)
            print("Contacto modificado exitosamente")
        else:
            print("contacto no encontrado ")

    if (op == 6):
        dato_contacto = False
        posicion = 0 #para guardar indice
        nombre_contacto = input('Digite el nombre del contacto :')

        for c in lista_contactos:
            if (list(c)[0] == nombre_contacto):
                dato_contacto = True
                posicion = lista_contactos.index(c)

        if (dato_contacto):  # contacto existente
            aux = list(lista_contactos[posicion])
            print (aux[1:])
            num = 0
            while (num < 1 or num>=len(aux)): #validar que la pos no sea 0 ni mayor al tamanio de la lista
                num = int(input('\ndigite la posicion del numero a modificar o eliminar ')) #posicion seleccionar numero
            print ('\n\tEl numero que usted selecciono es "{}" exitosamente: '.format(aux[1]))
            print('\t1. Modificar ')
            print('\t2. Eliminar ')

            while (op < 1 or op > 2):
                op = int(input('Por favor digite una de las dos opciones.. (modificar o eliminar)'))
            aux.pop(num)
            if(op==1):
                numero_contacto = input('Digite el nuevo numero de contacto:')
                aux.insert(num, numero_contacto)
                print('Modificcion exitosa')
            else:
                if(len(aux)>2):
                    print('Eliminacion exitosa')
                else:
                    aux.insert(num, numero_contacto)
                    print('--no es posible eliminar el numero ya que el contacto solo cuenta con un solo numero')
            lista_contactos[posicion] = tuple(aux)
        else:
            print("contacto no encontrado ")

"""
    1..Permitir agregar numeros a un determinado contacto
    2..Eliminar o modificar un determinado numero de un contacto
    3..eliminar todo el contacto
    4..Modificar el nombre del contacto
    5..Poder buscar un contacto por su numero
    6..Complemetar los metodos diciendo si los datos existen o no

    """