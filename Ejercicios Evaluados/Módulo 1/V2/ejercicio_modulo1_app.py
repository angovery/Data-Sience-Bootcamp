# Archivo principal de la aplicación

import ejercicio_modulo1_menus as menu
import ejercicio_modulo1_usuario_crud as crud

lista = crud.crear_lista_inicial()
crud.imprimir_lista(lista)
crud.imprimir_menu(menu.opciones_menu_principal)

while True:
    option = crud.seleccionar_opcion(menu.opciones_menu_principal)
    match option:
        case 1: # Imprimir todos los usuarios de la lista.
            crud.imprimir_lista(lista)
            
        case 2: # Imprimir los usuarios ordenados por edad, ascendente o descendentemente.
            crud.imprimir_usuarios_ordenados_edad(lista, menu.opciones_submenu_lista_ordenada)
                
        case 3: # Buscar usuario por email
            crud.imprimir_usuario_por_email(lista)
                
        case 4: # Crea un nuevo usuario y se añade a la lista
            crud.crear_usuario(lista)
                            
        case 5: # Actualizar datos de un usuario existente. Dado que se utiliza el email como clave única, el email no puede modificarse. En caso de actualizarse el email, se deberá eliminar el usuario en cuestión y crear un nuevo usuario con los datos actualizados.
            crud.actualizar_usuario(lista)
        
        case 6: # Se elimina un usuario a partir de su email asociado.
            crud.eliminar_usuario(lista)

        case 7: # Se elimina la lista completa de usuarios.
            crud.eliminar_lista(lista)
        
        case 8:
            print ("\n", "Hasta pronto.", "\n")
            break

    crud.imprimir_menu(menu.opciones_menu_principal)