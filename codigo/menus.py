#!/usr/bin/python
# -*- coding: utf-8 -*-

from guardarYleer import *
from lfsr import *
from BM import *
from test import *
from operdadores import *

def menu():
    print ("\nSelecciona una opción")
    print ("\t1 - Introducir Secuencia")
    print ("\t2 - Analizar Secuencia")
    print("\t! - Salir")

def menuIntroducirSecuencia():
    secuencia = ""

    print ("\nSelecciona una opción")
    print ("\t1 - Generar Secuencia")
    print ("\t2 - Introducir Secuencia")
    print ("\t3 - Combinar Secuencias")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        secuencia = menuGenerar()
    elif opcion == "2":
        secuencia = introduceSecuencia()
    elif opcion == '3':
        secuencia = menuCombinar()
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        secuencia = menuIntroducirSecuencia()

    return secuencia

def menuGenerar():
    polinomio = None
    semilla = None
    tamanio = None
    gradoDelPolinomio = None
    secuencia = ""

    print ("\nSeleccione una opción: ")
    print ("\t1 - LFSR")
    print ("\t2 - LFSR2")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        datos = datoslfsr(polinomio, semilla, tamanio, gradoDelPolinomio)
        secuencia = lfsr(datos[0], datos[1], datos[2], datos[3])
        guardarEnArchivo(secuencia)
        print('La secuencia es: ', secuencia)
    elif opcion == "2":
        datos = datoslfsr(polinomio, semilla, tamanio, gradoDelPolinomio)
        secuencia = lfsr2(datos[0], datos[1], datos[2], datos[3])
        guardarEnArchivo(secuencia)
        print('La secuencia es: ', secuencia)
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        secuencia = menuGenerar()

    return secuencia

def introduceSecuencia():
    print ("\nSeleccione una opción: ")
    print ("\t1 - Introduce la secuencia por teclado")
    print ("\t2 - Lee secuencia de un fichero")
    secuencia = ''

    opcion = input("Elija una opción: ")

    if opcion == '1':
        secuencia = str(input('Introduce la secuencia (unos y ceros): '))
        guardarEnArchivo(secuencia)
    elif opcion == '2':
        secuencia = leerDeArchivo(secuencia)
        #print(secuencia)
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        secuencia = introduceSecuencia()
    return secuencia

def menuAnalizarSecuencia():
    print ("\nSeleccione una opcion: ")
    print ("\t1 - Berlekamp-Massey")
    print ("\t2 - TestFrecuenciaMonobit")
    print ("\t3 - TestFrecuenciaBloque")
    print ("\t4 - TestRachas")
    print ("\t5 - TestComplejidadLineal")
    print ("\t6 - ContarRachas")

    secuencia = ""
    l = 0
    opcion = input("Elija una opción: ")

    if opcion == "1":
        secuencia = menuIntroducirSecuencia()
        l = berlekampMassey(secuencia)
        print('\nLa longitud mínima es: ', l)
    elif opcion == "2":
        secuencia = menuIntroducirSecuencia()
        resultado = frecuencyTest(secuencia)
        print('P-value =', resultado)
        if resultado >= 0.05:
            print('La secuencia es aceptada como aleatoria')
        else:
            print('La secuencia no es aceptada como aleatoria')
    elif opcion == '3':
        secuencia = menuIntroducirSecuencia()
        resultado = frecuencyTestBlock(secuencia)
        print('P-value =', resultado)
        if resultado >= 0.05:
            print('La secuencia es aceptada como aleatoria')
        else:
            print('La secuencia no es aceptada como aleatoria')
    elif opcion == '4':
        secuencia = menuIntroducirSecuencia()
        resultado = runsTest(secuencia)
        print('P-value =', resultado)
        if resultado >= 0.05:
            print('La secuencia es aceptada como aleatoria')
        else:
            print('La secuencia no es aceptada como aleatoria')
    elif opcion == '5':
        secuencia = menuIntroducirSecuencia()
        resultado = linear_complexity(secuencia)
        print('P-value =', resultado)
        if resultado >= 0.05:
            print('La secuencia es aceptada como aleatoria')
        else:
            print('La secuencia no es aceptada como aleatoria')
    elif opcion == '6':
        secuencia = menuIntroducirSecuencia()
        testRachas(secuencia)
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        secuencia = menuAnalizarSecuencia()

    return secuencia

def menuCombinar():
    print ("\nSeleccione una opcion: ")
    print ("\t1 - OperadorAND")
    print ("\t2 - OperadorOR")
    print ("\t3 - OperadorXOR")
    print ("\t4 - OperadorNAND")
    print ("\t5 - OperadorIMPLICA")
    print ("\t6 - OperadorNOT")

    secuencia = ""
    opcion = input("Elija una opción: ")

    if opcion == "1":
        secuencia = menuIntroducirSecuencia()
        secuencia2 = menuIntroducirSecuencia()
        resultado = operadorAND(secuencia, secuencia2)
        print("\nLa secuencia AND es: ", resultado)
        guardarEnArchivo(resultado)
    elif opcion == "2":
        secuencia = menuIntroducirSecuencia()
        secuencia2 = menuIntroducirSecuencia()
        resultado = operadorOR(secuencia, secuencia2)
        print("\nLa secuencia OR es: ", resultado)
        guardarEnArchivo(resultado)
    elif opcion == "3":
        secuencia = menuIntroducirSecuencia()
        secuencia2 = menuIntroducirSecuencia()
        resultado = operadorXOR(secuencia, secuencia2)
        print("\nLa secuencia XOR es: ", resultado)
        guardarEnArchivo(resultado)
    elif opcion == "4":
        secuencia = menuIntroducirSecuencia()
        secuencia2 = menuIntroducirSecuencia()
        resultado = operadorNAND(secuencia, secuencia2)
        print("\nLa secuencia NAND es: ", resultado)
        guardarEnArchivo(resultado)
    elif opcion == "5":
        secuencia = menuIntroducirSecuencia()
        secuencia2 = menuIntroducirSecuencia()
        resultado = operadorImplica(secuencia, secuencia2)
        print("\nLa secuencia IMPLICA es: ", resultado)
        guardarEnArchivo(resultado)
    elif opcion == "6":
        secuencia = menuIntroducirSecuencia()
        resultado = operadorNOT(secuencia)
        print("ªnLa secuencia NOT es: ", resultado)
        guardarEnArchivo(resultado)
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        
    return resultado