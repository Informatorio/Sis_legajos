#!/usr/bin/python3

import random
import sqlite3
import os 
import string

def ingreso_datos():  
  LUGARES = ["DEPÓSITO 1","DEPÓSITO 2", "DEPÓSITO 3"]
  ARCHIVOS = [["1","10"],["2","8"],["3","8"],["4","8"],["5","8"],["6","8"],["7","8"],["8","8"],["9","5"]]

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
        temp = h + " " + j      
        # temp = i + ", " + h + " " + j      
        # tempo = temp.split(", ")
        alumnos.append([i,temp])
         
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
    alumno.append([legajo[i],dni[i],alumnos[i][0],alumnos[i][1]])
    # print(alumno[i])
    
  return alumno,LUGARES,ARCHIVOS

def conectar(ruta):
  #  Conectar a la base de datos
  conexion = sqlite3.connect(ruta)
  #  Seleccionar el cursor para realizar la consulta
  consulta = conexion.cursor()
  return (consulta,conexion)

def terminar_consulta(consulta):
  #  Terminar la consulta
  consulta.close()

def commit(conexion):
  #  Guardar los cambios en la base de datos
  conexion.commit()

def cerrar_conexion(conexion):
  #  Cerramos la conexión a la base de datos
  conexion.close()

def insertar_datos(alu,lug,archi):

  #INGRESO DE ALUMNOS
  for i in range(len(alu)):
    argumentos = (alu[i][0],alu[i][1],alu[i][2],alu[i][3])  
    sql = """
    INSERT INTO Alumnos_alumno(legajo, dni, apellido, nombre)
    VALUES (?,?,?,?)
     """
     #  Ejecutamos la consulta
    if (consulta.execute(sql, argumentos)): print("Alumno guardado con éxito.")
    else: print("Ha ocurrido un error al guardar el registro.")

  # INGRESO DE LUGARES
  for i in range(len(lugares)):
    argumentos = [lugares[i]]
    sql = """
    INSERT INTO Alumnos_lugar(descripcion)
    VALUES (?)
     """
     #  Ejecutamos la consulta
    if (consulta.execute(sql, argumentos)): print("Lugar guardado con éxito.")
    else: print("Ha ocurrido un error al guardar el registro.")

  # INGRESO DE ARCHIVOS 
  sql = "SELECT * FROM Alumnos_lugar"
  if (consulta.execute(sql)):
    sqlLugares = consulta.fetchall()
    x = 0
    for lugar in sqlLugares:
      # import ipdb; ipdb.set_trace()
      j = 0
      while x <= len(archi) and j < 3:
        argumentos = [archi[x][0],archi[x][1],lugar[0]]
        sql = """
        INSERT INTO Alumnos_archivo(numero,cajones,lugar_id)
        VALUES (?,?,?)
         """
        if (consulta.execute(sql, argumentos)): print("Archivo guardado con éxito.")
        else: print("Ha ocurrido un error al guardar el registro.")
        j = j + 1
        x = x + 1      
  else:
    print("Ha ocurrido un error, no hay registro.")

  # INGRESO DE LOCALIZACIÓN
  sql = "SELECT * FROM Alumnos_alumno"
  if (consulta.execute(sql)):
    sqlAlumnos = consulta.fetchall()

    for alumno in sqlAlumnos:
      alumno_id = alumno[0]
      sql = "SELECT * FROM Alumnos_archivo"
      if (consulta.execute(sql)):
        sqlArchivos = consulta.fetchall()
        archivo     = random.choice(sqlArchivos)
        archivo_id  = archivo[0]
        lugar_id    = archivo[3]
        archivo_cajones = archivo[2]
        cajon = random.randint(1,archivo_cajones)

        argumentos = [cajon,alumno_id,archivo_id,lugar_id]
        sql = """
        INSERT INTO Alumnos_localizacion(cajon,alumno_id,archivo_id,lugar_id)
        VALUES (?,?,?,?)
         """
        if (consulta.execute(sql, argumentos)): print("Localización guardada con éxito.")
        else: print("Ha ocurrido un error al guardar el registro.")


ruta = "C:\Sis_legajos\db.sqlite3" 

consulta,conexion = conectar(ruta)

commit(conexion)

alumno,lugares,archivos = ingreso_datos()
# ****** INSERTAR DATOS ******
insertar_datos(alumno,lugares,archivos)

terminar_consulta(consulta)
commit(conexion)
# ****************************
cerrar_conexion(conexion)
