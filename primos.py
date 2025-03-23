# Fichero números primos

"""

Ramon Llobet Duch

>>> esPrimo(5)
True

>>> esPrimo(10)
False

>>> esPrimo(74211)
False


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
     comuns =   set(factors1 + factors2)
     resultat = 1
     for num in comuns:
          exp1 = factors1.count(num)
          exp2 = factors2.count(num)
          expo_max = max(exp1,exp2)
          resultat = resultat*num**expo_max
    
     return resultat






     

        







if __name__ == "__main__":
    import doctest
    doctest.testmod()




