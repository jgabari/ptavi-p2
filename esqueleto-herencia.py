#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Persona():
  """Esto es un ejemplo de clase que hereda de ClaseMadre"""

  def __init__(self, nombre, dni):
    """Esto es el método iniciliazador"""
    self.nombre = nombre
    self.dni = dni

  def dame_nombre(self):
    return self.nombre

  def dame_dni(self):
    return self.dni

class Alumno(Persona):

  def __init__(self, nombre, dni, asignaturas):
    """Esto es el método iniciliazador"""
    self.nombre = nombre
    self.dni = dni
    self.asignaturas = asignaturas

  def asignaturas_pendientes(self):
    return ['PTAVI', 'Campos', 'Systems and Signals']

if __name__ == "__main__":
  objeto = Persona("pepe", 12312312) # Creo un objeto de la clase Clase
                         # y le paso el valor pepe para su
                         # atributo en la inicialización
  print(objeto.dame_nombre())
  objeto2 = Persona("maria", 1212)
  print(objeto2.dame_dni())
  vicente = Alumno("vicente", 5325423, ['PTAVI'])
  print(vicente.dame_nombre())
  print(vicente.asignaturas)