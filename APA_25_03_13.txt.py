# coding: utf-8
import primos
import doctest
doctest.testmod(primos)
doctest.testmod(primos, verbose=True)
get_ipython().run_line_magic('run', 'primos')
get_ipython().run_line_magic('run', 'primos -v')
help(esPrimo)
esPrimo.__doc__
print(esPrimo.__doc__)
get_ipython().run_line_magic('save', '')
