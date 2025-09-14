from datetime import date, timedelta, datetime
import random
import smtplib
from email.mime.text import MIMEText

def crear_tarea (A, HORAS, MINUTOS, Z, C, D):
    texto_agregar = A
    try:
        fecha_actual = date.today()
        ahora = datetime.now()
        fecha_fin = ahora + timedelta(days=Z, hours=HORAS, minutes=MINUTOS)
        diferencia = fecha_fin - ahora

        if diferencia.total_seconds() > 0:
            dias = diferencia.days
            horas_restantes, resto_segundos = divmod(diferencia.seconds, 3600)
            minutos_restantes, _ = divmod(resto_segundos, 60)
            contador = f"{dias}d {horas_restantes}h {minutos_restantes}m restantes"
            estado = "En progreso"  

    except ValueError:
        print("no se puede")
        return

    categoria = D

    try:
        with open("tareas.txt", "r") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        lineas = []

    ramdon = random.randint(1,5000)

    if lineas:
        ultimo_id = int(lineas[-1].split("ID: ")[1].split(",")[0])
    else:
        ultimo_id = 0
    nuevo_id = ultimo_id + ramdon
    if nuevo_id == ultimo_id:
        return nuevo_id

    nueva = (
        f"ID: {nuevo_id}, Nombre: {texto_agregar}, fecha actual: {fecha_actual}, "
        f"vence: {contador}, estado: {estado},"
        f" prioridad: {C}, categoria: {categoria}\n"
    )
    lineas.append(nueva)

    lineas.sort(key=lambda x: int(x.split("prioridad: ")[1].split(",")[0]))

    with open("tareas.txt", "w", encoding="utf-8") as f:
        f.writelines(lineas)

    print (
        f"Nombre: {texto_agregar},"
        f" fecha actual: {fecha_actual},"
        f" vence: {fecha_fin.date()},"
        f" dias hasta vencimiento: {diferencia.days},"
        f" prioridad: {C},"
        f" categoria: {categoria} \n"
    )

    return A, Z, C, D, MINUTOS, HORAS


def leer_tareas():
    try:
        with open('tareas.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("No hay tareas.")
        

def cambiar(A, B, C):
   return A.replace(B, C)


def actualizar_tarea(A):
    with open("tareas.txt", 'r', encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    id_buscar = A.strip()
    linea_encontrada = False

    for i, linea in enumerate(lineas):
        if linea.strip().startswith(f"ID: {id_buscar}"):
            print("Linea encontrada:", linea.strip())
            linea_encontrada = True
            while True:

             palabra = input("¿Que campo quiere cambiar? (Nombre, vence, prioridad, categoria): ").strip()

             partes = linea.strip().split(", ")
             campo_encontrado = False
             for j, parte in enumerate(partes):
                 if parte.lower().startswith(palabra.lower()):
                     clave = parte.split(":")[0]
                     if clave == "vence":
                         nuevo_valor = input("¿Que valor desea poner? YYYY-MM-DD: ").strip()
                         try:
                             fecha_actual = date.today()
                             fecha_futura = date.fromisoformat(nuevo_valor)
                             diferencia = fecha_futura - fecha_actual
                             if diferencia.days < -1:
                                 print("La fecha ingresada ya paso.")
                                 return None
                             else:      
                              print(f"Dias hasta vencimiento: {diferencia.days} dias")
                             nuevo_valor = str(fecha_futura)
                         except ValueError:
                             print("Formato de fecha incorrecto. usa AAAA-MM-DD.")
                             return None
                     elif clave == "fecha actual":
                         print("No se puede cambiar la fecha actual.")
                         return None
                     elif clave == "ID":
                         print("No se puede cambiar el ID.")
                         return None
                     else:
                         nuevo_valor = input(f"Coloque el/la {palabra}: ").strip()
                     partes[j] = f"{clave}: {nuevo_valor}"
                     campo_encontrado = True
                     break
             if campo_encontrado:
                 lineas[i] = ", ".join(partes) + "\n"
                 print("Linea modificada:", lineas[i].strip())
             else:
                 print("Campo no encontrado en la línea.")
             break

    if not linea_encontrada:
        print("ID no encontrado")
        return None

    with open("tareas.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)

    return lineas

def eliminar_tarea(A):
 
 A = A.strip()
 try:
    with open("tareas.txt", 'r', encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    lineas_actualizadas = [linea for linea in lineas if not linea.strip().startswith(f"ID: {A}")]

    if len(lineas) == len(lineas_actualizadas):
        print("ID no encontrado.")
        print("\n")
        return None

    with open("tareas.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas_actualizadas)

    print(f"Tarea con ID {A} eliminada exitosamente.")
    print("\n")
    return lineas_actualizadas
 
 except FileNotFoundError:
     print("ERROR")
     return None



    
def inicio_de_seccion (remitente_email, contrasena_email, destinatario_email):
    contenido_txt = "No se pudo cargar el contenido de las tareas."
    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:
            contenido_txt = archivo.read()
    except FileNotFoundError:
        contenido_txt = "Error"
    except Exception as e:
        contenido_txt = f"Error en: {e}"

    ahora = datetime.now()
    fecha_hora_actual = ahora.strftime("%Y-%m-%d %H:%M:%S")

    asunto = f"Reporte de Tareas - {fecha_hora_actual}"
    cuerpo_email = f"""
    KELOKE MIO,

    Aqui tan tus tareas:

    {fecha_hora_actual}

    --- Contenido de Tareas ---
    {contenido_txt}
    --- Fin del contenido ---
    """

    msg = MIMEText(cuerpo_email)
    msg["Asunto: "] = asunto
    msg["De"] = remitente_email
    msg["To"] = destinatario_email

    servidor_smtp = None
    try:
        servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
        servidor_smtp.starttls()
        servidor_smtp.login(remitente_email, contrasena_email)
        servidor_smtp.sendmail(remitente_email, destinatario_email, msg.as_string())
        return True, "¡Correo enviado exitosamente!"

    except smtplib.SMTPAuthenticationError:
        return False, "Error de autenticación: Verifica tu correo y contraseña. Para Gmail, es posible que necesites una contrasena de aplicacion: si tienes la verificación en dos pasos activada."
    except smtplib.SMTPException as e:
        return False, f"Error SMTP al enviar el correo: {e}. Asegurate de que tu conexion a internet funciona y que el servidor SMTP es correcto."
    except Exception as e:
        return False, f"Error inesperado al enviar el correo: {e}"
    finally:
        if servidor_smtp:
            servidor_smtp.quit()





def marcar_tarea_como_terminada(id_buscar):
    with open("tareas.txt", 'r', encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    id_buscar = str(id_buscar).strip()
    linea_encontrada = False
    
    for i, linea in enumerate(lineas):
        if linea.strip().startswith(f"ID: {id_buscar}"):
            print(f"Linea encontrada para marcar como terminada: {linea.strip()}")

            linea_encontrada = True
            
            partes = linea.strip().split(", ")
            partes_filtradas = []

            for parte in partes:
                if parte.lower().startswith("estado:"):
                    partes_filtradas.append("estado: Terminada")
                elif parte.lower().startswith("ID:"):
                    partes_filtradas.append(parte)
                elif parte.lower().startswith("Nombre:"):
                    partes_filtradas.append(parte)
                elif parte.lower().startswith("prioridad:"):
                    partes_filtradas.append("prioridad: 10")
                elif parte.lower().startswith("vence:"):
                    partes_filtradas.append("vence: vencida")
                else:
                    partes_filtradas.append(parte)

            lineas[i] = ", ".join(partes_filtradas) + "\n"
            print(f"Tarea marcada como terminada: {lineas[i].strip()}")
            break

    if not linea_encontrada:
        print(f"ID '{id_buscar}' no encontrado.")
        return None

    try:
        with open("tareas.txt", "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)
        print("Archivo tareas.txt actualizado.")
    except Exception as e:
        print(f"Error en: {e}")
        return None

    return lineas