def resta(*nums:float)->float:
    res = 0
    for valor in nums:
        res -= valor
    return res

def suma(*nums:float)->float:
    suma = 0
    for valor in nums:
        suma += valor
    return suma
    
def mult(*nums:float)->float:
    mult = 1
    for valor in nums:
        mult *= valor
    return mult

def div(n1:float, n2:float)->float:
    div = n1/n2
    sobra = n1 % n2
    return div,sobra


