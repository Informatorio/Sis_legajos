#!/usr/bin/python3

import random

APELLIDOS = ["Martínez", "Radovancich", "Íbalo", "Harasiwka", "Gómez", "López", "García", "Geréz", "Zamora", "Duprat", "Encina", "Fernández"]
NOMBRES = ["Juan", "Gabriel", "Alejandro", "Pedro", "María", "Nazareno", "Román", "Vanesa", "Claudia", "Cecilia", "Elsa", "Ramón", "Gloria", "Darío", "Fernando", "Fernanda", "Claudio", "José"]
alumnos = []
legajoA = []
legajoB = []
legajo = []
nacimientos = []
dni = []
alumno = []

for i in APELLIDOS:
  for j in NOMBRES:
    for h in sorted(NOMBRES):
      temp = i + " " + h + " " + j
      alumnos.append(temp)

for i in alumnos:
  legajoA.append(random.randint(1000,9999))
  legajoB.append(random.randint(1000,9999))
  nacimientos.append(random.randint(1976, 1997))
  dni.append(random.randrange(25000000, 40000000))

legajoA.sort()
legajoB.sort()
nacimientos.sort()
dni.sort()

for i in range(len(legajoA)):
  temp = str(legajoA[i]) + "-" + str(legajoB[i])
  legajo.append(temp)

for i in range(len(alumnos)):
  alumno.append([legajo[i],nacimientos[i],dni[i],alumnos[i]])
  print(alumno[i])
