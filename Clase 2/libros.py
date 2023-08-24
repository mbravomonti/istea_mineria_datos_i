import csv


class Libro ():
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion


lista_libros = []
permanencia = True

with open('libros.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        libro = Libro(row['titulo'], row['autor'], row['genero'], float(row['puntuacion']))
        lista_libros.append(libro)

while (permanencia):
    print("""1. Agregar libro
2. Buscar libros por género
3. Recomendar libro
4. Salir""")
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Opción no válida")
        continue
    if opcion == 1:
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        puntuacion = int(input("Ingrese la puntuación del libro: "))
        libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(libro)
    elif opcion == 2:
        genero = input("Ingrese el género del libro: ")
        for libro in lista_libros:
            if libro.genero == genero:
                print(libro.titulo)
    elif opcion == 3:
        genero = input("Ingrese el género del libro: ")
        puntuacion_maxima = 0
        titulo_libro = ""
        for libro in lista_libros:
            if libro.genero == genero:
                if libro.puntuacion > puntuacion_maxima:
                    puntuacion_maxima = libro.puntuacion
                    titulo_libro = libro.titulo
        print("El libro recomendado es: " + titulo_libro)
    elif opcion == 4:
        permanencia = False
    else:
        print("Opción no válida")
