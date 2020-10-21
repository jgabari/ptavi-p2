#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def multiplica(self):
        return self.operando1 * self.operando2

    def divide(self):
        try:
            return self.operando1 / self.operando2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except IndexError:
        sys.exit("Error: introduce 3 argumentos")

    objeto = CalculadoraHija(operando1, operando2)
    if sys.argv[2] == "suma":
        print(objeto.suma())
    elif sys.argv[2] == "resta":
        print(objeto.resta())
    elif sys.argv[2] == "multiplica":
        print(objeto.multiplica())
    elif sys.argv[2] == "divide":
        print(objeto.divide())
    else:
        sys.exit("Error: introduzca suma o resta")
