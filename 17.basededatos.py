import mysql.connector
opcionBaseDeDatos = 2
if opcionBaseDeDatos == 1 :
    #Forma local
    host="localhost"
    user="root" # root
    passwd="" # ""
    port = 3306
    database='mini-siiau'
    
elif opcionBaseDeDatos == 2 :
    #Forma remota
    host="142.44.163.242"
    user="Alumno12"
    passwd="AlumnoPython1@."
    port = 4000
    database='mini-siiau'

try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        port=port,
        database=database)
    cursor = conexion.cursor()
    cursor.execute("Select * from Maestro")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
except mysql.connector.Error as err:
	print("Ocurrió un error al conectar: ", err)
 
 