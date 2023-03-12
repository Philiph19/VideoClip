from socio import Socio
from videoclub import VideoClub
from pelicula import Pelicula
from os import system

class Menu:

    def __init__(self, videoclub):
        self.videoclub = videoclub

    def adicionar_socio(self):
        system("cls")
        print("****************************")
        print("****  ADICIONAR SOCIO   ****")
        print("****************************")
        codigo = input("Digite el codigo del socio: ")
        nombre = input("Digite el nombre del socio: ")
        telefono = input("Digite el telefono del socio: ")
        domicilio = input("Digite el domicilio del socio: ")
        socio = Socio(codigo, nombre, telefono, domicilio)

        if self.videoclub.adicionar_socio(socio):
            print("*******************************")
            print("Info - El Socio fue adicionado correctamente!") 
            print("*******************************")
            input()
        
        else:
            print("*******************************")
            print("Info - El Socio no fue adicionado!") 
            print("*******************************")
            input()

    def listar_socio(self):
        system("cls")
        print("**************************")
        print("****  LISTAR SOCIOS   ****")
        print("**************************")
        self.videoclub.listar_socio()
        input()

    def eliminar_socio(self):
        system("cls")
        print("**************************")
        print("****  ELIMINAR SOCIOS   ****")
        print("**************************")
        codigo = input("Digite el Codigo del socio que desea eliminar: ")

        if self.videoclub.eliminar_socio(codigo):
            print("*******************************")
            print("Info - El Socio fue eliminado correctamente!") 
            print("*******************************")
            input()
        
        else:
            print("*******************************")
            print("Info - El Socio no existe, no se pudo eliminar!") 
            print("*******************************")
            input()

    def adicionar_pelicula(self):
        system("cls")
        print("**************************")
        print("****  ADICIONAR PELICULA   ****")
        print("**************************")
        codigo = input("Digite el codigo de la pelicula: ")
        titulo = input("Digite el titulo de la pelicula: ")
        genero = input("Digite el genero de la pelicula: ")
        pelicula = Pelicula(codigo, titulo, genero)

        if self.videoclub.adicionar_pelicula(pelicula):
            print("*******************************")
            print("Info - La pelicula fue añadida correctamente!") 
            print("*******************************")
            input()
        
        else:
            print("*******************************")
            print("Info - La pelicula no se pudo añadir!") 
            print("*******************************")
            input()

    def listar_pelicula(self):
        system("cls")
        print("**************************")
        print("****  LISTAR PELICULAS   ****")
        print("**************************")
        self.videoclub.listar_pelicula()
        input()

    def eliminar_pelicula(self):
        system("cls")
        print("**************************")
        print("****  ELIMINAR PELICULAS   ****")
        print("**************************")
        codigo = input("Digite el Codigo de la película que desea eliminar: ")

        if self.videoclub.eliminar_pelicula(codigo):
            print("*******************************")
            print("Info - La película fue eliminada correctamente!") 
            print("*******************************")
            input()
        
        else:
            print("*******************************")
            print("Info - La película no se pudo eliminar!") 
            print("*******************************")
            input()

    def alquilar_pelicula(self):
        system("cls")
        print("**************************")
        print("****  ALQUILAR PELICULAS   ****")
        print("**************************")
        codigo_pelicula = input("Digite el Codigo de la película: ")
        codigo_socio = input("Digite el codigo del socio: ")

        if self.videoclub.alquilar_pelicula(codigo_pelicula, codigo_socio):
            print("*******************************")
            print("Info - La película fue alquilada correctamente!") 
            print("*******************************")
            input()
        
        else:
            print("*******************************")
            print("Info - La película no se pudo alquilar!") 
            print("*******************************")
            input()

    def devolver_pelicula(self):
        system("cls")
        print("**************************")
        print("****  DEVOLVER PELICULAS   ****")
        print("**************************")
        codigo_pelicula = input("Digite el Codigo de la película a devolver: ")
        codigo_socio = input("Digite el codigo del socio: ")

        if self.videoclub.devolver_pelicula(codigo_pelicula, codigo_socio):
            print("*******************************")
            print("Info - La película fue devuelta correctamente!") 
            print("*******************************")
            input()
        
        else:
            print("*******************************")
            print("Info - La película no se pudo devolver!") 
            print("*******************************")
            input()

    def mostrar_menu_principal(self):
        while True:
            system("cls")
            print("*******************************")
            print("*******************************")
            print("*****     VideoClub       *****")
            print("*******************************")
            print("Menu Principal")
            print("*******************************")
            print("*******************************")
            print("1 = Crear Socios")
            print("2 = Listar Socios")
            print("3 = Eliminar Socios")
            print("4 = Crear pelicula")
            print("5 = Listar pelicula")
            print("6 = Eliminar pelicula")
            print("7 = Alquilar pelicula")
            print("8 = Devolver pelicula")
            print("9 = Salir")
            print("*******************************")
            print("*******************************")

            try:
                op = int(input("Digite su opción: "))
                print("****************************")

                if op == 1:
                    self.adicionar_socio()
                
                elif op == 2:
                    self.listar_socio()

                elif op == 3:
                    self.eliminar_socio()

                elif op == 4:
                    self.adicionar_pelicula()

                elif op == 5:
                    self.listar_pelicula()

                
                elif op == 6:
                    self.eliminar_pelicula()
                
                elif op == 7:
                    self.alquilar_pelicula()

                elif op == 8:
                    self.devolver_pelicula()

                elif op == 9:
                    break

                else:
                    print("****************************")
                    print("Error, la Opción del menú es inválida!")
                    print("****************************")
                    input()

            except ValueError:
                print("****************************")
                print("***Error, el dato no es un entero!***")
                print("*******************************")
                input()

if __name__ == "__main__":
    videoclub = VideoClub("ABC")
    menu = Menu(videoclub) 
    menu.mostrar_menu_principal()