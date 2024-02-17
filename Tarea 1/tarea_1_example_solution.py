# Función 1, capaz de alternar mayúsculas y minúsculas en una cadena
def invert_case(cadena):
    valorsinuso = ""
    cadenainv = ""  # la cadenainv será el resultado invertido
    if not isinstance(cadena, str):  # compara el tipo de dato
        codigo = -16  # Entrada no es string
        cadenainv = None
    elif cadena == "":  # la cadena es un string vacio?
        codigo = -48  # String vacio
        cadenainv = None
    elif not cadena.isalpha():  # todos son letras del abecedario?
        codigo = -32  # Fuera del abecedario
        cadenainv = None
    else:  # Invierte la cadena válida
        for x in range(0, len(cadena)):
            if cadena[x].islower():
                aux = cadena[x].upper()
            else:
                aux = cadena[x].lower()
            cadenainv = cadenainv+aux
        codigo = 0  # Éxito
    return [codigo, cadenainv]

          # Función 2, devuelve números primos entre 1 y la base


def numero_primo(base):
    x = isinstance(base, int)
    y = isinstance(base, bool)
    if (not x or y):  # Es entero?
        codigo = -64  # no es un entero
        primos = None
    elif base > 100:  # Es menor a 100?
        codigo = -80  # mayor a 100
        primos = None
    else:  # Verifica si son primos con la función es_primo
        primos = []
        for x in range(2, base+1):
            if es_primo(x, 2):
                primos.append(x)  # Si son primos se añaden a la lista
        codigo = 0  # Éxito
    return [codigo, primos]

# Función para reconocer si es primo


def es_primo(num, n=2):
    if n >= num:  # Si el numero es menor o igual al divisor es primo
        return True
# Revisa si no es divisible, suma uno al divisor y vuelve a revisar
    elif num % n != 0:
        return es_primo(num, n + 1)
# Caso contrario no es primo
    else:
        return False
