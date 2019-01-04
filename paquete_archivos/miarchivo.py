
import codecs

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/info2.csv", "a")

    def agregar_informacion(self, e):
        self.archivo.write("%s-%s-%d-%d\n" % (e.nombres, e.ciudad, e.campeonatos, e.numJugadores))

    def cerrar_archivo(self):
        self.archivo.close()
