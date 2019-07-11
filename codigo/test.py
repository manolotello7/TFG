#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter
from scipy import integrate
from scipy import special
import math
import numpy
from BM import *

def frecuencyTest(secuencia):
    tamCadena = len(secuencia)
    Sn = 0
    for i in range(0, tamCadena):
        if(secuencia[i] == '0'):
            n = int(secuencia[i]) - 1
        else:
            n = secuencia[i]
        Sn += int(n)

    Sobs = abs(Sn)/math.sqrt(tamCadena)

    integral = integrate.romberg(lambda x: math.e**(-x**2), Sobs/math.sqrt(2), 4.5)
    Pvalue = (2.0/math.sqrt(math.pi))*integral

    return Pvalue


def frecuencyTestBlock(secuencia):
    M = 8500
    tamCadena = len(secuencia)
    inicio = 0
    fin = M
    Xobs = 0

    N = int(tamCadena / M)

    for i in range(N):
        cadena1 = secuencia[inicio:fin]
        contador = 0

        for elemento in cadena1:
            if elemento == '1':
                contador += 1
        pi = contador / M
        Xobs += pow(pi - 1/2, 2)

        inicio += M
        fin += M

    X2obs = 4 * M * Xobs
    Pvalue = special.gammaincc(N / 2, X2obs / 2)
    
    return Pvalue


def runsTest(secuencia):
    Pvalue = 0
    tamCadena = len(secuencia)
    contador = 0
    v_obs = 1

    for elemento in secuencia:
        if elemento == '1':
            contador += 1
    
    pi = contador / tamCadena

    tau = 2 / math.sqrt(tamCadena)
    if abs(pi - 1/2) < tau:
        for i in range(1, tamCadena):
            if secuencia[i] != secuencia[i - 1]:
                v_obs += 1
        numerador = abs(v_obs - 2 * tamCadena * pi * (1 - pi))
        denominador = 2 * math.sqrt(2 * tamCadena) * pi * (1 - pi)
        if denominador == 0.0:
            print('No se puede realizar el test')
        else:
            Pvalue = special.erfc(numerador / denominador)
    else:
        print('No se puede realizar el test')
    return Pvalue

def linear_complexity(secuencia):
    k = 6
    pi = [0.01047, 0.03125, 0.125, 0.5, 0.25, 0.0625, 0.020833]
    M = 40
    Pvalue = 0

    mu2 = (M / 3 + 2 / 9) / 2 ** M
    mu = M / 2 + (1 / 36) * (9 + (-1) ** (M + 1)) - mu2
    N = int(len(secuencia) / M)

    if N > 0:
        fin_bloque = M
        inicio_bloque = 0
        bloque = []
        for i in range(N):
            bloque.append(secuencia[inicio_bloque:fin_bloque])
            inicio_bloque += M
            fin_bloque += M

        L_BM = []
        for bloc in bloque:
            L_BM.append(berlekampMassey(bloc))
        
        t = []
        for l in L_BM:
            t.append((((-1) ** M) * (l - mu) + 2 / 9))
        
        v = []
        v0 = 0
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = 0
        v6 = 0

        for ti in t:
            if ti <= -2.5:
                v0 += 1
            elif ti > -2.5 and ti <= -1.5:
                v1 += 1
            elif ti > -1.5 and ti <= -0.5:
                v2 += 1
            elif ti > -0.5 and ti <= 0.5:
                v3 += 1
            elif ti > 0.5 and ti <= 1.5:
                v4 += 1
            elif ti > 1.5 and ti <= 2.5:
                v5 += 1
            elif ti > 2.5:
                v6 += 1
        
        v.append(v0)
        v.append(v1)
        v.append(v2)
        v.append(v3)
        v.append(v4)
        v.append(v5)
        v.append(v6)
        
        frac = []
        for j in range(7):
            frac.append(((v[j] - N * pi[j]) ** 2) / (N * pi[j]))
        
        Xobs = 0.0
        for i in range(k):
            Xobs += frac[i]
        Pvalue = special.gammaincc(k / 2, Xobs / 2)
        
    return Pvalue

def testRachas(secuencia):
    tamCadena = len(secuencia)
    secuencia1 = []
    secuencia2 = []
    secuenciaMod1 = []
    secuenciaMod2 = []
    secuenciaPeriodo = []
    listaRachaUnos = []
    listaRachaCeros = []
    contadorCeros = 0
    contadorUnos = 0

    for i in range(0, tamCadena):
        secuencia1.append(secuencia[i])
        secuencia2.append(secuencia[i])        

    contador = 0
    periodoTotal = 0
    
    periodo = 1
    secuenciaMod1 = secuencia1[:-1]
    secuenciaMod2 = secuencia2[1:]
    pos = 1
    mitad = tamCadena//2

    while secuenciaMod1 != secuenciaMod2 and (periodo <= mitad):
        secuenciaMod1 = secuenciaMod1[:-1]
        secuenciaMod2 = secuenciaMod2[1:]
        periodo += 1
        
    periodoTotal = periodo

    if periodoTotal > tamCadena/2:
        periodoTotal = 0

    for i in range(0, periodoTotal):
        secuenciaPeriodo.append(secuencia1[i])
    
    tamCadenaPeriodo = len(secuenciaPeriodo)

    if periodoTotal > 0:
        secPer = ''.join(str(e) for e in secuenciaPeriodo)
        print('La secuencia es: ', secPer)
        print('El periodo es: ', periodoTotal)
        for i in range(0, periodoTotal):
            if secuencia1[i] == '1':
                contadorUnos += 1
                if i == tamCadenaPeriodo-1:
                    listaRachaUnos.append(contadorUnos)
            else:
                if contadorUnos != 0:
                    listaRachaUnos.append(contadorUnos)
                contadorUnos = 0
        listaRachaUnos = sorted(listaRachaUnos) # Ordena la cadena de menor a mayor.
        contadorUnos = Counter(listaRachaUnos).most_common()
        print('Rachas de 1: ', contadorUnos)

        for i in range(0, periodoTotal):
            if secuenciaPeriodo[i] == '0':
                contadorCeros += 1
                if i == tamCadenaPeriodo-1:
                    listaRachaCeros.append(contadorCeros)
            else:
                if contadorCeros != 0:
                    listaRachaCeros.append(contadorCeros)
                contadorCeros = 0
        listaRachaCeros = sorted(listaRachaCeros) # Ordena la cadena de menor a mayor.
        contadorCeros = Counter(listaRachaCeros).most_common()
        print('Rachas de 0: ', contadorCeros)

    else: 
        print('La secuencia no tiene periodo')
        
        j = 0
        while (secuencia[j] == secuencia[-1]):
            secuencia = secuencia[-1] + secuencia
            secuencia = secuencia[:tamCadena]
            j = j+1
        print('La secuencia final es: ', secuencia)
        print('La secuencia no tiene periodo')

        for i in range(0, tamCadena):
            if secuencia[i] == '1':
                contadorUnos += 1
                if i == tamCadena-1:
                    listaRachaUnos.append(contadorUnos)
            else:
                if contadorUnos != 0:
                    listaRachaUnos.append(contadorUnos)
                contadorUnos = 0
        listaRachaUnos = sorted(listaRachaUnos) # Ordena la cadena de menor a mayor.
        contadorUnos = Counter(listaRachaUnos).most_common()
        print('Rachas de 1: ', contadorUnos)

        for i in range(0, tamCadena):
            if secuencia[i] == '0':
                contadorCeros += 1
                if i == tamCadena-1:
                    listaRachaCeros.append(contadorCeros)
            else:
                if contadorCeros != 0:
                    listaRachaCeros.append(contadorCeros)
                contadorCeros = 0
        listaRachaCeros = sorted(listaRachaCeros) # Ordena la cadena de menor a mayor.
        contadorCeros = Counter(listaRachaCeros).most_common()
        print('Rachas de 0: ', contadorCeros)