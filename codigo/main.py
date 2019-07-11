#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from menus import *

def main():
    opcion = 0
    resultado = 0
    while True:
        menu()
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            secuencia = menuIntroducirSecuencia()
            #print('EL CALCULO ES: ', secuencia)
        elif opcion == "2":
            secuencia = menuAnalizarSecuencia()
        elif opcion == "!":
            sys.exit()
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


if __name__ == "__main__":
    main()