#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except IndexError:
        sys.exit("Error: introduce 3 argumentos")

    objeto = Calculadora(operando1, operando2)
    if sys.argv[2] == "suma":
        print(objeto.suma())
    elif sys.argv[2] == "resta":
        print(objeto.resta())
    else:
        sys.exit("Error: introduzca suma o resta")
