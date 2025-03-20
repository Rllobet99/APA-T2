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

        
#PENDIENTE:
# descompon(numero) Devuelve una tupla con la descomposición en factores primos de su argumento.         






if __name__ == "__main__":
    import doctest
    doctest.testmod()




