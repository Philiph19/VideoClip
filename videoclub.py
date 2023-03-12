from socio import Socio
from pelicula import Pelicula

class VideoClub():

    def __init__(self, nombre):
        self.nombre = nombre
        self.socios = []
        self.peliculas = []

    def buscar_socio(self, codigo):
        for i in range(len(self.socios)):
            if self.socios[i].codigo == codigo:
                return i
        return -1
    
    def adicionar_socio(self, socio):
        if self.buscar_socio(socio.codigo) == -1:
            self.socios.append(socio)
            return True
        return False

    def listar_socio(self):
        for socio in self.socios:
            print("**********************")
            socio.mostrar_socio()
    
    def eliminar_socio(self, codigo):
        pos = self.buscar_socio(codigo)
        if pos != -1:
            del(self.socios[pos])
            return True
        return False

    def buscar_pelicula(self, codigo):
        for i in range(len(self.peliculas)):
            if self.peliculas[i].codigo == codigo:
                return i
        return -1
    
    def adicionar_pelicula(self, pelicula):
        if self.buscar_pelicula(pelicula.codigo) == -1:
            self.peliculas.append(pelicula)
            return True
        return False
    
    def listar_pelicula(self):
        for pelicula in self.peliculas:
            print("**********************")
            pelicula.mostrar_pelicula()

    def eliminar_pelicula(self, codigo):
        pos = self.buscar_pelicula(codigo)
        if pos != -1:
            del(self.peliculas[pos]) 
            return True
        return False
    
    def alquilar_pelicula(self, codigo_pelicula, codigo_socio):
        pos_pelicula = self.buscar_pelicula(codigo_pelicula)
        pos_socio = self.buscar_socio(codigo_socio)
        if self.peliculas[pos_pelicula].alquilada == False:
            if pos_pelicula != -1 and pos_socio != -1:
                self.peliculas[pos_pelicula].alquilada = True
                return True
            else:
                return False
        else:
            return False

    def devolver_pelicula(self, codigo_pelicula, codigo_socio):
        pos_pelicula = self.buscar_pelicula(codigo_pelicula)
        pos_socio = self.buscar_socio(codigo_socio)
        if self.peliculas[pos_pelicula].alquilada == True:
            if pos_pelicula != -1 and pos_socio != -1:
                self.peliculas[pos_pelicula].alquilada = False
                return True
            else:
                return False
        else:
            return False