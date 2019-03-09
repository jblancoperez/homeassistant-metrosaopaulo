#!/usr/bin/env python


from metrosaopaulo import metrosaopaulo

def a():
    metro=metrosaopaulo.MetroSaoPaulo()
    return metro.get_metro_status()
    
ret = a()
print (ret)
