def comparar_cadenas_lexicograficas(cadena1, cadena2):

    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()

    if (cadena1 < cadena2):
        return -1
    elif (cadena2 < cadena1):
        return 1
    else:
        return 0
