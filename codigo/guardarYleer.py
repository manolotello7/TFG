#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

def guardarEnArchivo(secuencia):
    guardar = input("Quieres guardar la secuencia en un archivo? (s, n): \n")
    fecha = datetime.now()
    archivo = 0
    if guardar == "s":
        archivo = open(str(fecha) + ".txt","w")
        archivo.write(secuencia)
        archivo.close()
    return archivo

def leerDeArchivo(secuencia):
    leer = input("Nombre del archivo donde está la secuencia: \n")
    archivo = 0
    archivo = open(leer)
    secuencia = archivo.read()
    archivo.close()
    return secuencia