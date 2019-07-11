#!/usr/bin/python
# -*- coding: utf-8 -*-

def operadorAND(secuencia, secuencia2):
    resultado = []
    tamSecuencia1 = len(secuencia)
    for i in range(0, tamSecuencia1):
        opAnd = int(secuencia[i]) and int(secuencia2[i])
        resultado.append(opAnd)
    resultado = ''.join(str(e) for e in resultado)
    return resultado

def operadorOR(secuencia, secuencia2):
    resultado = []
    tamSecuencia1 = len(secuencia)
    for i in range(0, tamSecuencia1):
        opOr = int(secuencia[i]) or int(secuencia2[i])
        resultado.append(opOr)
    resultado = ''.join(str(e) for e in resultado)
    return resultado

def operadorXOR(secuencia, secuencia2):
    resultado = []
    tamSecuencia1 = len(secuencia)
    for i in range(0, tamSecuencia1):
        opXor = int(secuencia[i]) ^ int(secuencia2[i])
        resultado.append(opXor)
    resultado = ''.join(str(e) for e in resultado)
    return resultado

def operadorNAND(secuencia, secuencia2):
    resultado = []
    tamSecuencia1 = len(secuencia)
    for i in range(0, tamSecuencia1):
        if (secuencia[i] == '1') and (secuencia2[i] == '1'):
            resultado.append(0)
        if (secuencia[i] == '1') and (secuencia2[i] == '0'):
            resultado.append(1)
        if (secuencia[i] == '0') and (secuencia2[i] == '1'):
            resultado.append(1)
        if (secuencia[i] == '0') and (secuencia2[i] == '0'):
            resultado.append(1)
    resultado = ''.join(str(e) for e in resultado)
    return resultado

def operadorImplica(secuencia, secuencia2):
    resultado = []
    tamSecuencia1 = len(secuencia)
    for i in range(0, tamSecuencia1):
        if (secuencia[i] == '1') and (secuencia2[i] == '1'):
            resultado.append(1)
        if (secuencia[i] == '1') and (secuencia2[i] == '0'):
            resultado.append(0)
        if (secuencia[i] == '0') and (secuencia2[i] == '1'):
            resultado.append(1)
        if (secuencia[i] == '0') and (secuencia2[i] == '0'):
            resultado.append(1)
    resultado = ''.join(str(e) for e in resultado)
    return resultado

def operadorNOT(secuencia):
    resultado = []
    tamSecuencia1 = len(secuencia)
    for i in range(0, tamSecuencia1):
        opNot1 = ~ int(secuencia[i])%2
        resultado.append(opNot1)
    resultado = ''.join(str(e) for e in resultado)
    return resultado
