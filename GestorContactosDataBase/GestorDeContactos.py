
#Lianjuh

#Esta vez intentaré hacer lo mismo pero en vez de guardar en json, lo haré con una base de datos, nunca he trabajado con una de ellas
import json
import mysql.connector

#Creamos la conexión de la base de datos en mysql despoués de instalar la conexión en visual studio
def conectar():
    return mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "#######", #No pondré mi contraseña por motivos un poco obvios, esto es solo práctica
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
        6. Salir
        """
        print(menu)
    
    #Creamos la función para ingresar los datos y guardarlos en el json
    @staticmethod
    def IngresarDatos():
        conexion = conectar()
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
        sql = """INSERT INTO datos_personas (id_persona, nombre_persona, numero_telefono, correo_electronnico) VALUES (%s, %s, %s, %s)"""
        
        #Con esto insertamos los datos de los valores anteriormente pedidos en la base de datos
        valores = (codigo_persona, nombre_persona, numero_telefonico_persona, correo_persona)
        cursor.execute(sql, (valores))
        conexion.commit()
        
        print("Datos establecidos correctamente, (ojalá funcione)")
        cursor.close()
        conexion.close()
            
    #Mostrar datos en el menú, aunque ya lo hace al guardar datos
    @staticmethod
    def MostrarDatos(datos_gestion = None):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM datos_personas")
        
        personas = cursor.fetchall()
        if not personas:
            print("No hay usuarios registrados")
        else:
            for persona in personas:
                print(f"ID: {persona[0]} | Nombre: {persona[1]} | Teléfono: {persona[2]} | Correo: {persona[3]}")
                    
        cursor.close()
        conexion.close       
       
       
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
            
    #Intento desarrollar una función para que me ayude a buscar y actualizar
    @staticmethod
    def modificar_archivos():
        
        GestorArchivos.MostrarDatos()
        
        conexion = conectar()
        cursor = conexion.cursor()
        id_persona = input("Seleccione el ID del usuario al cual quiere modificar")
        
        #pedimos datos nuevos:
        print("porfavor digite el nuevo nombre del usuario")
        nuevo_nombre = input()
        
        print("porfavor digite el nuevo número del usuario")
        nuevo_numero = input()
        
        print("porfavor digite el nuevo correo del usuario")
        nuevo_correo = input()
        
        sql = """
        UPDATE datos_personas
        SET nombre_persona = %s, numero_telefono = %s, correo_electronnico = %s
        WHERE id_persona = %s
        """
        valores = (nuevo_nombre, nuevo_numero, nuevo_correo, id_persona)

        cursor.execute(sql, valores)
        conexion.commit()

        print("Registro cambiado exitosamente??")
        cursor.close()
        conexion.close()
        
    
    @staticmethod
    def borrar_datos():
        conexion = conectar()
        cursor = conexion.cursor()
        GestorArchivos.MostrarDatos()
        
        id_persona = input("porfavor inserte el id de la persona que desea eliminar")
        
        sql = """
        DELETE FROM datos_personas WHERE id_persona = %s
        """
        cursor.execute(sql, (id_persona,))
        conexion.commit()
        print("borrado exitosamente (ojalá)")
        
        cursor.close()
        conexion.close()
        

GestorArchivos.Menu()
