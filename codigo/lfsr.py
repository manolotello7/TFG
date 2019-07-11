#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter

def datoslfsr(polinomio, semilla, tamanio, gradoDelPolinomio):
    gradoDelPolinomio = int(input('Introduce el grado del polinomio: '))
    i=0
    lista = []
    datos = []
    for i in range(0, gradoDelPolinomio+1):
        while True:
            coeficiente = input('Introduce el valor del coeficiente (uno ó cero): ')
            if(coeficiente == '0' or coeficiente == '1'):
                coeficiente = int(coeficiente)
                break
        print('(' +  str(coeficiente) + ')' + str('x') + '^' + str(gradoDelPolinomio-i))
        if (coeficiente == 1):
            lista.append(gradoDelPolinomio-i)
            polinomio = tuple(lista)
            print (polinomio)

    while True:
        semilla = str(input('Introduce el valor de la semilla (unos y ceros): '))
        if(len(semilla) == gradoDelPolinomio):
            break

    while True:
        tamanio = int(input('Introduce el tamaño de la secuencia: '))
        if(tamanio > gradoDelPolinomio):
            break
    datos.append(polinomio)
    datos.append(semilla)
    datos.append(tamanio)
    datos.append(gradoDelPolinomio)

    return datos

def lfsr(polinomio, semilla, tamanio, gradoDelPolinomio):
    polinomio = polinomio[:-1]  #Quita el menor elemento de la tupla
    for j in range(gradoDelPolinomio, tamanio):
        suma = 0
        for x in polinomio:
            suma = suma ^ int(semilla[j-x])
        semilla = semilla + str(suma)
    
    #Cuenta el numero de unos y ceros
    tamSemilla = Counter(semilla)
    print (tamSemilla)
    secuencia = semilla
    
    return secuencia


def lfsr2(polinomio, semilla, tamanio, gradoDelPolinomio):
    polinomio = polinomio[1:]  #Quita el mayor elemento de la tupla.
    for j in range(gradoDelPolinomio, tamanio):
        suma = 0               
        for x in polinomio:
            suma = suma ^ int(semilla[j-(gradoDelPolinomio - x)])
        semilla = semilla + str(suma)
    
    #Cuenta el numero de unos y ceros
    tamSemilla = Counter(semilla)
    print (tamSemilla)
    secuencia = semilla

    return secuencia