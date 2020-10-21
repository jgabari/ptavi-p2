#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


fich = open(sys.argv[1])
lineas = fich.readlines()
for linea in lineas:
    lista = linea.split(',')
    operacion = lista[0]
    resultado = int(lista[1])
    if operacion == "suma":
        for operando in lista[2:]:
            objeto = calcoohija.CalculadoraHija(resultado, int(operando))
            resultado = objeto.suma()
    elif operacion == "resta":
        for operando in lista[2:]:
            objeto = calcoohija.CalculadoraHija(resultado, int(operando))
            resultado = objeto.resta()
    elif operacion == "multiplica":
        for operando in lista[2:]:
            objeto = calcoohija.CalculadoraHija(resultado, int(operando))
            resultado = objeto.multiplica()
    elif operacion == "divide":
        for operando in lista[2:]:
            objeto = calcoohija.CalculadoraHija(resultado, int(operando))
            resultado = objeto.divide()
    else:
        sys.exit("Error: introduzca suma, resta, multiplica o divide")
    print(resultado)

fich.close()
