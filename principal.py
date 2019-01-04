from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.mimodelo import Equipo

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
for d in lista:
    # print(d)
    e = Equipo(d[0], d[1], d[2], d[3])
    print(e)
    m2.agregar_informacion(e)

m.cerrar_archivo()
m2.cerrar_archivo()
