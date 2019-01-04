class Equipo:
    
    def __init__(self, n, ciu, camp, numJ):
 
        self.nombres = n
        self.ciudad = ciu
        self.campeonatos = int(camp)
        self.numJugadores = int(numJ)

    def agregar_nombres(self, n):

        self.nombres = n

    def obtener_nombres(self):
        
        return self.nombre

    def agregar_ciudad(self, ciu):

        self.ciudad = ciu

    def obtener_ciudad(self):
    
        return self.ciudad
    
    def agregar_campeonatos(self, camp):
        
        self.campeonatos = int(camp)

    def obtener_campeonatos(self):
        
        return self.campeonatos
    
    def agregar_numJugadores(self, numJ):
        
        self.numJugadores = int(numJ)

    def obtener_numJugadores(self):

        return self.numJugadores

    
    def __str__(self):
        """
        """
        return "%s - %s - %s - %s" % (self.nombres, self.ciudad, self.campeonatos, self.numJugadores)
