#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

with open('fichero') as csvfile:
    reader = csv.reader(csvfile)
    for linea in reader:
        operacion = linea[0]
        resultado = int(linea[1])
        if operacion == 'suma':
            for operando in linea[2:]:
                objeto = calcoohija.CalculadoraHija(resultado, int(operando))
                resultado = objeto.suma()
        elif operacion == 'resta':
            for operando in linea[2:]:
                objeto = calcoohija.CalculadoraHija(resultado, int(operando))
                resultado = objeto.resta()
        elif operacion == 'multiplica':
            for operando in linea[2:]:
                objeto = calcoohija.CalculadoraHija(resultado, int(operando))
                resultado = objeto.multiplica()
        elif operacion == 'divide':
            for operando in linea[2:]:
                objeto = calcoohija.CalculadoraHija(resultado, int(operando))
                resultado = objeto.divide()
        else:
            sys.exit("Error: introduzca suma, resta, multiplica o divide")
        print(resultado)
