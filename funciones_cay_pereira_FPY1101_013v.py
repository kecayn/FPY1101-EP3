def registrar_libro(libros): #registro de libros ok
    titulo = input("Ingresar titulo del libro: ")
    autor = input("Ingresar autor del libro: ")
    ano_publicado = input("Ingresar año de publicación: ")
    sku = input("Ingresar SKU")

    libro = {
        "Titulo" : titulo,
        "Autor" : autor,
        "año" : ano_publicado,
        "SKU" : sku
    }
    libros.append(libro)

def prestar_libro():

    nom_usuario = input("Ingresa tu nombre de usuario: ")
    sku_libro = input("Favor ingresa el SKU del libro deseado: ")
    fecha_prestamo = input("Ingresar fecha de hoy ")

    usuario = {
        "Nombre de usuario" : nom_usuario,
        "fecha de prestamo" : fecha_prestamo
    }


def listar_libros(libros): # listar libros ok
    for libro in libros:
        print(f"{libro["Titulo"]}, {libro["Autor"]},{libro["Año de publicacion"]}, {libro["SKU"]}")
    print()
def imprimir_prestamos(libros, nom_usuario = None):
    if nom_usuario is None:
        nom_usuario = input("Ingresar usuario o enter para mostrar todos: ")
        if nom_usuario =="":
            nom_usuario = None
    
    print("Gerenando planilla...")
    with open ("planilla_libros.txt","w") as file:
        for libro in libros:
            if nom_usuario is None or libro["nom_usuario"].lower() == nom_usuario.lower:
                file.write(f"{libro["Nombre usuario"]}{libro["Titulo"]},{libro["fecha de prestamo "]}\n")
def main(): #menu principal ok
    libros=[]
    while True:
        print("1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de préstamos\n5. Salir del programa ")

        op = input(" Ingrese una opción: ")
    
        if op == "1":
            registrar_libro(libros)
        elif op == "2":
            prestar_libro(libros)
        elif op == "3":
            listar_libros(libros)
        elif op == "4":
            imprimir_prestamos(libros)
        elif op == "5":
            print("Saliendo del programa")
        else:
            print("Opción no valida, favor")
    
if __name__=='_main_': 
    main()