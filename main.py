from tkinter import *
from tkinter import filedialog, Tk
import os


def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo LFP",
        initialdir = "./",
        filetypes = (
            ("Archivos LFP", "*.lfp"),
            ("Todos los archivos","*.*")
        )
    )

    if archivo is None:
        print("Error de lectura")
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print("Lectura Exitosa")
        return texto

def analizador(entrada):

    curso = ''
    datosEst = ''
    parametro = ''

    aux = ''
    estado = 'curso'
    posicion = 1

    for i in entrada:
        if estado == 'curso':
            if i == '=':
                estado = 'datosEst'
                curso = aux
                aux = ''
            else:
                aux += i

            posicion += 1

        if estado == 'datosEst':
            if i == '{' or i == '}' or i== '<' or i== '>':
                estado = 'parametro'
                datosEst = aux
                aux = ''
            else:
                aux += i

            posicion += 1
        if estado == 'parametro':
            if(posicion == len(entrada)):
                aux += i
                parametro = aux
                aux = ''
            else:
                aux += i

            posicion += 1

        else:
            return  None
    return [curso,datosEst,parametro]





def menu():
    print('\n------------------------------------------------------------------------')
    print('Bienvenido al programa, por favor eliga una de las siguientes opciones')
    print('\n1. Cargar archivo de entrada')
    print('2. Mostrar reporte en consola')
    print('3. Exportar reporte')
    print('4. Salir')
    opcion = input('Ingrese su opcion: ')
    return opcion


if __name__=='__main__':
    clear = lambda: os.system('cls')

    #txt = abrir()

    ciclo = True
    while (ciclo):

        opcion = menu()

        if opcion == "1":
            print('\nCargando archivo de entrada')

            txt = abrir()
            if txt is not None:
                if txt == '':
                    print("Archivo vacio")
                else:
                    print(txt)
                    print(analizador(txt))

            else:
                print("Vuelva a intentarlo por favor")


        elif opcion == "2":
            print('Mostrar reporte en consola')
            print(analizador(txt))


        elif opcion == "3":
            print('Exportar reporte')

        elif opcion == "4":
            print('\nProgrma Finalizado')
            input()
            ciclo = False

        else:
            print("Opcion no valida")
            clear()
