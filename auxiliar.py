def message(option:int, description:str = "", field:str = ""):
    if option == 1:#identificador
        msg_out = "El identificador del " + description + " no ha sido encontrado!"
    if option == 2:#Listado
        msg_out = "No hay información de " + description + " registrados!"
    if option == 3:#Campo
        msg_out = "El " + field + " especificado no correponde a ningún " + description + " registrado!"
    if option == 4:#Actualizar
        msg_out = "Ningún dato ha cambiado y el proceso de actualización fue cancelado!"
    return msg_out