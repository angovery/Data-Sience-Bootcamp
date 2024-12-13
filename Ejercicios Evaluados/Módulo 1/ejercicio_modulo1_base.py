# Ejercicio Nº1 - Módulo 1

class Usuario:
# Declaración de la clase Usuario
    
    # Constructor de la clase Usuario
    def __init__(self, nombre, email, edad, altura, estudiante):
        self.nombre = nombre # Tipo str
        self.email = email # Tipo str
        self.edad = edad # Tipo int
        self. altura = altura # Tipo float
        self.estudiante = estudiante # Tipo bool
        # self.cumpleanos = cumpleanos # Tipo date
        
    # Método para imprimir el objeto
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Edad: {self.edad}, Altura: {self.altura}, Estudiante: {self.estudiante}"
               
""" Se crean las opciones del menú principal en una tupla (ya que, en principio, no se van a alterar los elementos del menú).
Si es preciso, para facilitar el mantenimiento, y por si posteriormente se desea añadir, modificar o eliminar alguna,
se puede modificar la tupla a nivel de código. El primer elemento de la lista indica el tipo de menú.
"""
opciones_menu_principal = (
        "-----MENU DE PRINCIPAL-----\n",
        "1 - Imprimir todos los usuarios de la lista",
        "2 - Imprimir todos los usuarios ordenados por edad",
        "3 - Imprimir un usuario por su email",
        "4 - Crear un nuevo usuario",
        "5 - Actualizar un usuario existente",
        "6 - Borrar usuario por su email",
        "7 - Borrar todos los usuarios",
        "8 - Salir"
    )

# Opciones posibles del submenú de la opción 2 del menú principal, Imprimir lista ordenada
opciones_submenu_lista_ordenada = (
    "-----OPCIONES DE ORDENACIÓN-----\n",
    "1 - Ascendente",
    "2 - Descendente",
    "3 - Volver al Menú Principal",
    "4 - Salir"
)

# Función para imprimir un menú
def imprimir_menu(lista_opciones):
    for opcion in lista_opciones:
        print(opcion)
    print("\n", "\n")

# Función para el tratamiento de la opción seleccionada. Toma como entrada una lista de opciones y devuelve un entero.
def seleccionar_opcion(lista_opciones):
    valido = False
    while not valido:
        try:
            opcion = int(input("Por favor, seleccione una de las opciones indicadas arriba, tecleando el número correspondiente y pulsando 'Enter': ").strip())
        except ValueError:
            print("No ha introducido un número entero. Por favor, inténtelo de nuevo.","\n")
        except:
            print("Se ha producido un error. Por favor, inténtelo de nuevo.","\n")
        else:
            if opcion > len(lista_opciones)-1:
                print(f"El número introducido no forma parte de las opciones disponibles. Por favor, introduzca un número entre 1 y {len(lista_opciones)-1}")
            else:
                valido = True
    return opcion

        
    
 
# Función para crear ina lista de usuarios inicial. Devuelve una lista de elementos de tipo Usuario
def crear_lista_inicial():   
    # Se definen los usuarios de base.
    user1 = Usuario("Jose", "jose@nttdata.com", 49, 1.83, True)
    user2 = Usuario("Juan", "juan@nttdata.com", 39, 1.95, True)
    user3 = Usuario("Aaron", "aaron@google.com", 26, 1.74, False)
    user4 = Usuario("Borja", "borja@microsoft.com", 51, 1.67, False)

    # Se crea una lista de usuarios.
    usuarios = [user1, user2, user3, user4]
    return usuarios

"""
usuarios = [
    Usuario("Jose", "jose@nttdata.com", "49", "1.83", True)
    Usuario("Juan", "juan@nttdata.com", "39", "1.95", True)
    Usuario("Aaron", "aaron@google.com", "26", "1.74", False)
    Usuario("Borja", "borjae@microsoft.com", "51", "1.67", False)    
]
"""
# Función para imprimir una lista cuyos elementos son de tipo Usuario (valdría igualmente cualquier tipo de elemento). La lista debe existir.
def imprimir_lista(lista):
    if not lista:
        print("Lista vacía. No se puede imprimir")
    else:
        for elemento_lista in lista:
            print(elemento_lista)
    print("\n")

# Función que valida si un email tiene el formato correcto.
# Sólo considera válido el email si se ha incluido una '@'. No se hace ningún otro tipo de validación.
def email_formato_valido(email):
    return ("@" in email)

# Función que comprueba si existe un email en una lista de elementos de tipo Usuario.
def existe_email(lista, email):
    email_encontrado = False
    for indice in range(len(lista)):
        if email == lista[indice].email:
            email_encontrado = True
            break
    return email_encontrado

# Función que busca el índice del elemento de una lista de usuarios que coincide con el email dado. El email debe existir en la lista.
def indice_email(lista, email):
    for indice in range(len(lista)):
        if email == lista[indice].email:
            return indice

# Función para buscar un usuario por medio de un email. Toma como entrada una lista de usuarios
# Devuelve el índice de la lista donde se encuentra el usuario. Si no hay ningún usuario con el email introducido, devuelve -1.
def buscar_usuario_por_email(lista):
    index = -1
    email_valido = False
    email_encontrado = False
    while email_valido == False:
        email_a_buscar = input("\nIntroduzca el email del usuario que desea buscar: ").strip().lower()
        if email_formato_valido(email_a_buscar):
            email_valido = True
            break
        else:
            print("\nEmail no válido. ¿Seguro que has introducido el email correctamente?. Por favor, vuelva a intentarlo.")
            continue
    if existe_email(lista,email_a_buscar):
        return indice_email(lista,email_a_buscar)
    #for indice in range(len(lista)):
    #    if email_a_buscar == lista[indice].email:
    #        email_encontrado = True
    #        index = indice
    #        break
    if email_encontrado == False:
        print("\nEl email introducido no se encuentra en la lista de usuarios.\n")
    return index

# Función para añadir un nuevo usuario a la lista. Los datos se introducen desde la consola.
               

# Función para buscar un elemento de una lista de objetos de tipo Usuario, dado un email.
# def buscar_por_email (lista):
#   email_a_buscar = input 


# Función para ordenar una lista, en base a una clave, ya sea de forma ascendente o descendente
# def ordenar_lista(lista, clave, orden):
    

# ---------- BLOQUE PRINCIPAL DEL PROGRAMA ----------

lista = crear_lista_inicial()
imprimir_lista(lista)
imprimir_menu(opciones_menu_principal)

while True:
    option = seleccionar_opcion(opciones_menu_principal)
    match option:
        case 1: # Imprimir todos los usuarios de la lista.
            imprimir_lista(lista)
            
        case 2: # Imprimir los usuarios ordenados por edad, ascendente o descendentemente.
            imprimir_menu(opciones_submenu_lista_ordenada)
            sub_opcion = seleccionar_opcion(opciones_submenu_lista_ordenada)
            match sub_opcion:
                case 1: # Orden ascendente
                    lista_ascendente_edad = sorted(lista, key = lambda asc : asc.edad, reverse = False)
                    imprimir_lista(lista_ascendente_edad)
                case 2: # Orden descendente
                    lista_descendente_edad = sorted(lista, key = lambda desc : desc.edad, reverse = True)
                    imprimir_lista(lista_descendente_edad)
                case 3: # Volver al menu principal
                    pass
                case 4: # Salir
                    print ("\n", "Hasta pronto.", "\n")
                    break                     
        case 3: # Buscar usuario por email
            indice = buscar_usuario_por_email(lista)
            if indice != -1:
                print(lista[indice])
        case 4:
            #email = input("Introduzca el email del nuevo usuario").strip().lower()
            #if email_vale(email):
            #    if buscar_usuario_por_email(lista)
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            print ("\n", "Hasta pronto.", "\n")
            break
    imprimir_menu(opciones_menu_principal)


    


