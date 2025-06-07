#función
def nuevoTema (tema:str): #declara a la variable como cadena
    print(f"\n-----{tema}-----\n") # concatenando ("\n-----",+tema+, "----- \n")
# (f"\n-----{tema}-----\n") declarando mas tema de python cadena
# ("\n-----",tema, "----- \n") normal

if __name__ == "__main__":
    nuevoTema ("Operadores aritméticos")
    print ("operador suma, 5 + 6 =", 5 + 6)
    print ("operador resta, 9 - 8 =", 9 - 8)
    print ("operador multiplicación, 5 * 8 =", 5 * 8)
    print ("operador división entera, 13 // 7 =", 13 // 7)
    print ("operador división, 3/2 =",  3/2)
    print ("operador módulo, 21%7 =",  21%7)
    print ("operador cambio de signo, -2 =",  -2)
    print ("operador potencia, 2**3 =",  2**3) # comentarios línea por línea

    nuevoTema ("------operadores lógicos-----")
    print ("True and True:",True and True)
    print ("False and False:",False and False)
    print ("True and False:",True and False)
    print ("True or False:", True or False)
    print ("True or True:", True or True)
    print ("False or false:", False or False)
    print ("not False:", not  False)
    print ("not True:", not  True)
    
    
    nuevoTema ("----Operadores de comparación")
    print ("Igualdad, 4 == 3",4 == 3)
    print ("Diferente, 4 != 3",4 != 3)
    print ("Mayor, 4 > 3",4 > 3)
    print ("Mayor o igual, 4 >= 5",4 >= 5)
    print ("Menor, 2 < 3",2 < 3)
    print ("Menor o igual, 3 >= 3", 3 <= 3)
    
    '''viernes 6 de junio'''

    nuevoTema ("Variables")
    Variable1 = 10
    _variable2 = 6.2547
    VAriable3 = "Pepe"
    nombreVariable = 8
    print(Variable1, _variable2, VAriable3, nombreVariable)
    
    a, b, c = 8, 5, "Hola"
    print(a)
    print(b)
    print(c)

    nuevoTema("Enteros")

    w = 105
    x = 12394949402
    y = -58
    z = 0b00110011 #0b indica binario
    h = 0xFF #0x indica número hexadecimal 255 
    print (w, type(w))
    print (x, type(x))
    print (y, type(y))
    print (z, type(z))
    print (h, type(h))

    nuevoTema("flotantes")

    x = 1234.56
    print (x, type(x))
    y = -0.2576
    print (y, type(y))


    nuevoTema("Complejos")
    _C1 = -46j
    _C2 = 12+45j
    print (_C1, type(_C1))
    print (_C2, type(_C2))
    c = _C1 + _C2
    print ("suma, -46j +12 +14j  =", c )

    nuevoTema("booleanos")
    x = True
    print (x, type(x))


    nuevoTema ("listas")
    lista = [10, 20.5, "lista de python"] #orden elemento 10 es el elemento 0, 20.5 es el elemento 1
    print(lista)
    print (lista[1])
    lista[0] = "hola"
    lista.append (34)
    lista.insert (0, 101)
    print(lista)
    lista.append ([3, 4, 5, 6, 7, 8]) 
    print (lista[5])
    print (lista[5][4])
    print (lista[3][3])

    nuevoTema ("Tuplas")
    tupla = (25,"tupla", 1 +10j)
    print (tupla)
   #tupla[0] = 1.2 error, porque es inmutable    


    nuevoTema("Conjuntos")
    conjunto = {40, 20, 30, 30, 10}
    segundo = {25,30,14,16}
    c = conjunto.intersection(conjunto,segundo)
    d = conjunto.union (conjunto,segundo)
    print(c)
    print("union",d)

    nuevoTema ("diccionarios")
    diccionario = {"nombre": "Alba", "edad": "34", "telefono": "2345554"}
    print (diccionario)
    print(diccionario["telefono"])

    nuevoTema ("Cadena")
    C1 = "esto es muy complicado"
    C2 = 'para mi cerebro hoy'
    multilinea = '''esto es una cadena
    de varias líneas    con  tabuladores    y
    saltos
    de línea'''
    print (C1, C2)
    print (multilinea, type(multilinea))
    #print(C1.count(C1,2)) investigar este dato
    print (C1[2:5])
    print (C1[::-2])
    print (C1[:-5])
    print (C1[5])