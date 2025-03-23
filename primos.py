# Fichero números primos

"""

Ramon Llobet Duch

Determinación de la primalidad y mínimo común múltiplo y máximo común divisor


"""

def esPrimo(numero):
        """
        Devuelve True si el número es Primo,
        False si no lo es
        >>> for numero in range(2,10): 
        ...     print(esPrimo(numero))
        True
        True
        False
        True
        False
        True
        False
        False
        """
        for prueba in range(2, numero):
                if(numero % prueba == 0):
                       return False
        
        return True





def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que el número dado.

    >>> primos(10)
    (2, 3, 5, 7)

    >>> primos(20)
    (2, 3, 5, 7, 11, 13, 17, 19)

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    >>> primos(2)
    ()
    """
    lista = []
    for prueba in range(2, numero): 
        if esPrimo(prueba):
            lista.append(prueba) 

    return tuple(lista)  # Se convierte la lista en una tupla

    

def descompon(numero): 
    """
    Devuelve una tupla con la descomposición en factores primos del número dado.
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    
    >>> descompon(10)
    (2, 5)

    >>> descompon(30)
    (2, 3, 5)

    >>> descompon(13)  # Es primo
    (13,)

    """
    arg_primos = []
    divisor = 2  # menor número primo

    while numero > 1: 
        while numero % divisor == 0: 
            arg_primos.append(divisor)
            numero //= divisor  
        divisor += 1  

    return tuple(arg_primos)



def mcm(numero1,numero2):

    """
    Devuelve el mínimo común múltiplo (MCM) de dos números enteros.
    El MCM se calcula a partir de los factores primos de ambos números.
    
    >>> mcm(50, 30)
    150
    
    >>> mcm(15, 20)
    60

    """
    factors1 = descompon(numero1)
    factors2 = descompon(numero2)
    comuns =   set(factors1) | set(factors2)
    resultat = 1
    for num in comuns:
        exp1 = factors1.count(num)
        exp2 = factors2.count(num)
        expo_max = max(exp1,exp2)
        resultat = resultat*num**expo_max
    
    return resultat



def mcd(numero1,numero2):

    """
    Devuelve el máximo común divisor (MCD) de dos números.

    El MCD se calcula descomponiendo los números en sus factores primos,
    identificando los factores comunes y tomando la mínima potencia de cada uno.

    >>> mcd(924, 780)
    12

    >>> mcd(36, 48)
    12

    """
     
    factors1 = descompon(numero1)
    factors2 = descompon(numero2)
    comuns = set(factors1) &set(factors2)
    resultat = 1
    for num in comuns:
        exp1 = factors1.count(num)
        exp2 = factors2.count(num)
        expo_min = min(exp1,exp2)
        resultat = resultat*num**expo_min
    return resultat


def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    acumulado = numeros[0]

    for numero in numeros[1:]:
        acumulado = mcm(acumulado,numero)

    return acumulado

def mcdN(*numeros): 
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    acumulado = numeros[0]

    for numero in numeros[1:]:
        acumulado = mcd(acumulado,numero)

    return acumulado

     



if __name__ == "__main__":
    import doctest
    doctest.testmod()




