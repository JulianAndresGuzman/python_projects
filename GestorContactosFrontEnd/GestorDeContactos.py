
#Lianjuh

#Esta vez intentaré hacer lo mismo pero en vez de guardar en json, lo haré con una base de datos, nunca he trabajado con una de ellas



import json
import mysql.connector

#Creamos la conexión de la base de datos en mysql despoués de instalar la conexión en visual studio
conexion = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "julian592",
    database = "gestion_contactos"

)

class GestorArchivos:
    
    @staticmethod
    #Creamos la función para mostrar el menú
    def MostrarMenu():
        menu = """
        1. Ingresar Datos
        2. Borrar Datos
        3. Mostrar Datos
        4. Editar datos
        5. Formatear todos los datos
        6. Salir
        """
        print(menu)
    
    #Creamos la función para ingresar los datos y guardarlos en el json
    @staticmethod
    def IngresarDatos():
        
        cursor = conexion.cursor()
        print("Ingresa el codigo Para la persona:")
        codigo_persona = input()
        
        print("Ingresa el nombre de la persona:")
        nombre_persona = input()
        
        print("Ingresa el número télefonico de la persona:")
        numero_telefonico_persona = input()
        
        print("Ingresa el correo électrónico de la persona:")
        correo_persona = input()
        
        #Creamos la variable string para poner el código que pondremos en el sql, o algo así entendí más o menos        
        sql = """INSERT INTO datos_personas (nombre_persona, numero_telefono, correo_electronnico) VALUES (%s, %s, %s)"""
        
        #Con esto insertamos los datos de los valores anteriormente pedidos en la base de datos
        valores = (codigo_persona, nombre_persona, numero_telefonico_persona, correo_persona)
        cursor.execute(sql, valores)
        conexion.commit
        
        print("Datos establecidos correctamente, (ojalá funcione)")
        
        with open("gestion_basica.json", "r") as datos_json:
            datos_gestion = json.load(datos_json)
        
        if datos_json is not None:
            for persona in datos_gestion["personas"]:
                if datos_nuevos["codigo"] == persona["codigo"]:
                    print("NO SE PUEDE REGISTRAR, YA EXISTE DICHO CODIGO")
                    return
                else:
                    print("no se encontró nada, es posible guardar")
            
    #Mostrar datos en el menú, aunque ya lo hace al guardar datos
    @staticmethod
    def MostrarDatos(datos_gestion = None):
       cursor = conexion.cursor()
       cursor.execute("SELECT * FROM datos_personas")
       
       
       
       
       
       
    #La lógica principal del menú        
    @staticmethod
    def Menu():
        while True:
            GestorArchivos.MostrarMenu()
            try:
                print("Porfavor seleccione una opción")
                seleccion = int(input())
            except ValueError:
                print("porfavor seleccione un número valido")
                continue
            
            if seleccion == 1:
                GestorArchivos.IngresarDatos()
            if seleccion ==2:
                GestorArchivos.borrar_datos()
            elif seleccion == 3:
                GestorArchivos.MostrarDatos()
            elif seleccion == 4:
                GestorArchivos.modificar_archivos()
            elif seleccion == 5:
                GestorArchivos.formatear_datos()
            elif seleccion == 6:
                print("Saliendo del programa...")
                break
    
    @staticmethod
    #Para formatear absolutamente todos los datos, tanto en la variable como el json
    def formatear_datos():
        print("¿Estás seguro de querer borrar todos los datos?")
        print("si/no")
        confirmacion = input()
        
        if confirmacion.lower() in ["si", "yes", "y", "s"]:
            GestorArchivos.datos_persona = {
                "personas" : []
            }
            with open("gestion_basica.json", "w") as datos_json:
                json.dump(GestorArchivos.datos_persona, datos_json, indent=4)
                print("Datos borrados exitosamente")
        
        else:
            print("operacion Cancelada")
        
    #Parece que no carga los archivos antes de ser guardados nuevamente??
    #Ya se solucionó, parece que simplemente se debió crear esta función antes de escribir otro archivo
    @staticmethod
    def cargar_archivos():
            try:
                with open("gestion_basica.json", "r") as datos_json:
                    GestorArchivos.datos_persona = json.load(datos_json)
            except FileNotFoundError:
                GestorArchivos.datos_persona = {
                    "personas" : []
                }
            except json.JSONDecodeError:
                GestorArchivos.datos_persona = {
                    "personas" : []
                }
    
    
    #Intento desarrollar una función para que me ayude a buscar y actualizar
    @staticmethod
    def modificar_archivos(datos_gestion = None):
        
        if datos_gestion is None:
            try:
                with open("gestion_basica.json", "r") as datos_json:
                    datos_gestion = json.load(datos_json)
            except FileNotFoundError:
                print("No se ha podido cargar")
                return
            except json.JSONDecodeError:
                print("No se ha podido cargar el archivo")
                return
            
        if datos_gestion["personas"] is None:
                return
        for persona in datos_gestion["personas"]:
            print(f"Id:", persona["codigo"], " Nombre:", persona["nombre"], " Correo electrónico:", persona["correo_electronico"], " Numero telefonico:", persona["numero_telefonico"])
            
        print("Selecciona la id, de dato que quieras cambiar:")
        dato_seleccionado = int(input())
        for persona in datos_gestion["personas"]:
            if dato_seleccionado == int(persona["codigo"]):
                
                
                print("Ingresa el nombre de la persona:")
                persona["nombre"] = input()
                    
                print("Ingresa el número télefonico de la persona:")
                persona["numero_telefonico"] = input()
                    
                print("Ingresa el correo électrónico de la persona:")
                persona["correo_electronico"] = input()
                    
                try:
                    with open("gestion_basica.json", "w") as datos_json:
                        json.dump(datos_gestion, datos_json)
                except:
                    print("error, no se pudo guardar correctamente")
                    return
                    
            else:
                print("No se encontró")
    
    @staticmethod
    def borrar_datos(datos_gestion = None):
        
        if datos_gestion is None:
            try:
                with open("gestion_basica.json", "r") as datos_json:
                    datos_gestion = json.load(datos_json)
            except FileNotFoundError:
                print("No se ha podido cargar")
                return
            except json.JSONDecodeError:
                print("No se ha podido cargar el archivo")
                return
            
        if datos_gestion["personas"] is None:
                return
        for persona in datos_gestion["personas"]:
            print(f"Id:", persona["codigo"], " Nombre:", persona["nombre"], " Correo electrónico:", persona["correo_electronico"], " Numero telefonico:", persona["numero_telefonico"])
            
        print("Selecciona la id, de dato que quieras eliminar:")
        dato_seleccionado = int(input())
        for i, persona in enumerate(datos_gestion["personas"]):
            if dato_seleccionado == int(persona["codigo"]):
                del datos_gestion["personas"][i]
                
                with open("gestion_basica.json", "w") as datos_json:
                    json.dump(datos_gestion, datos_json)
                
GestorArchivos.cargar_archivos()    
GestorArchivos.Menu()
