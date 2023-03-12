class Pelicula():

    def __init__(self, codigo, titulo, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.alquilada = False 

    def mostrar_pelicula(self):
        print("Codigo: ", self.codigo)
        print("Título: ", self.titulo)
        print("Genéro: ", self.genero)

        if self.alquilada == False:
            print("Estado: Disponible")
        else:
            print("Estado: Alquilada")