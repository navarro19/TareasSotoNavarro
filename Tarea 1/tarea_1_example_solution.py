#Función 1, capaz de alternar mayúsculas y minúsculas en una cadena
def invert_case(cadena):
    #string se utiliza para comparar el tipo de dato, la cadenainv será el resultado invertido y código indica el error
    string = "string"
    cadenainv = ""
    codigo = ""
    #se compara el tipo de dato, en caso de no ser string muestra el error
    if(type(cadena) != type(string)):
        codigo = -16 #Entrada no es string
        cadenainv = None
    #revisa si la cadena es un string vacio comparándola con ""
    elif(cadena == ""):
        codigo = -48 #String vacio
        cadenainv = None
    #revisa si todos los caracteres son letras del abecedario utilizando isalpha()    
    elif(cadena.isalpha() == False):
        codigo = -32 #Fuera del abecedario
        cadenainv = None
    #En caso de ser una cadena válida realiza la inversión
    else:
        #Si la letra es minúscula la vuelve mayúscula y viceversa, guarda la letra invertida
        #en una variable auxiliar y rellena la cadenainv
        for x in range(0, len(cadena)):
            if(cadena[x].islower()):
                aux = cadena[x].upper()
            else:
                aux = cadena[x].lower()
            cadenainv = cadenainv+aux
        codigo = 0 #Éxito
    return [codigo, cadenainv]

#Función 2, capaz de devolver un arreglo con los números primos entre 1 y la base
def numero_primo(base):
    #Se primos para albergar los números y codigo para el error
    primos = ""
    codigo = ""
    #Comparamos con el 1 para saber si es un entero
    if(type(base) != type(1)):
        codigo = -64 #no es un entero
        primos = None
    #Se asegura que sea menor a 100
    elif(base>100):
        codigo = -80 #mayor a 100
        primos = None
    #Verifica si son primos con la función es_primo
    else:
        primos = []
        for x in range(2, base+1):
            #Si son primos se añaden a la lista
            if(es_primo(x, 2)):
                primos.append(x)
        codigo = 0 #Éxito
    return [codigo, primos]

#Función para reconocer si es primo
def es_primo(num, n):
    #Si el numero es menor o igual al divisor es primo
    if n >= num:
        return True
    #Revisa si no es divisible por el divisor, suma uno al divisor y vuelve a revisar
    elif num % n != 0:
        return es_primo(num, n + 1)
    #Caso contrario no es primo
    else:
        return False