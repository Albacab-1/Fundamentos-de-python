from Fundamentos import nuevoTema #importación de módulos y funciones desde otros programas

import calc.operaciones as c

if __name__== "__main__":
    nuevoTema ("Módulos y paquetes")
    
    print(c.resta(6,1))
    print(c.suma(2,3,4))
    print(c.mult(5,6))
    print(c.div(11,2.5))
