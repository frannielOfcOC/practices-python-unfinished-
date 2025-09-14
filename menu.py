from funciones import crear_tarea
from datetime import date
from funciones import leer_tareas
from funciones import actualizar_tarea
from prueba import tiempo
from funciones import eliminar_tarea
from funciones import inicio_de_seccion
from funciones import marcar_tarea_como_terminada

print ("-----Menu de inicio-----")
print ("")
print ("OPCIONES")
print ("")
print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")


while True:

  menu= input ("Seleccione el numero de la opcion que desea elegir: ")


  if menu == "1":
    print("\n")
    print("---------------------------------")
    print("\n")
    nombre_tarea = input ("ingresa una descripción para la tarea: ")

    fecha_actual =  date.today()
    print (f"fecha actual: {fecha_actual}")
    try:
      dias = int(input("dias: "))
      horas = int(input("horas: "))
      minutos = int(input("minutos: "))
      prioridad_tarea = int (input ("prioridad de menor a mayor (1-10): "))
    except ValueError:
      print("debe ingresar un numero")
      print("\n")
      print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")
      continue 

    area_tarea = input ("area: ")

    tiempo()
    print("---------------------------------")
    print("\n")

    logica = crear_tarea(A= nombre_tarea, Z= dias, MINUTOS= minutos, HORAS= horas, C= prioridad_tarea, D= area_tarea)
    print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")

  elif menu == "2":
    print("\n")
    print("---------------------------------")
    logica = leer_tareas()
    print("---------------------------------")
    print("\n")
    print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")



  elif menu == "3":
    print("---------------------------------")
    leer_tareas()
    print("---------------------------------")
    print("\n")
    id_ = input ("coloque el id de la tarea que quiere cambiar: ")
    logica = actualizar_tarea(A= id_)
    print("\n")
    print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")
    print("\n")

  elif menu == "4":
    print ("\n")
    leer_tareas()
    print ("\n")
    tarea = input("que tarea desea eliminar: ")
    eliminar = eliminar_tarea(A= tarea)
    print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")
    print("\n")

  elif menu == "5":
    break

  elif menu == "6":
    print("\n")
    gmail_user = input("Ingrese su correo de gmail: ")
    gmail_password = input("Ingrese su contraseña de gmail: ")
    gmail_destinatario = input("Ingrese el correo del destinatario: ")
    correo = inicio_de_seccion(gmail_user, gmail_password, gmail_destinatario)
    for correos in correo:
     print(correos)
    print("\n")
    print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")

  elif menu == "7":
   print("\n")
   print("---------------------------------")
   leer_tareas()
   print("---------------------------------")
   print("\n")
   id_ = input ("coloque el id de la tarea que quiere marcar como terminada: ")
   print("\n")
   logica = marcar_tarea_como_terminada(id_buscar= id_)
   print("\n")
   print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")
   print("\n")


  else:
   print("\n")
   print("opcion incorrecta")
   print("\n")
   print (" 1: Crear Tarea \n", "2: Leer Tares \n", "3: Actualizar Tarea \n", "4: Eliminar Tarea \n", "5: Salir \n", "6: Enviar reporte de tareas por email \n", "7: Marcar tarea como terminada \n")