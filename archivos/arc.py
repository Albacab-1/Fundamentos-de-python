file = open("EjemploArchivo.txt",'w')
file.write("este es el contenido del archivo.")
file.close()

lista = ["Fresa", "Mango", "Papaya"]

with open("EjemploArchivo.txt",'a') as file: #with es el contexto de uso para ese open (archivo)
    for e in lista:
        file.write(e + "\n")
print("lista escrita en el archivo")

lista2 = ["Honda", "Suzuki", "Bajaj"]

with open("EjemploArchivo.txt",'a') as file:
    file.writelines(lista2)
print("lista escrita con writelines")

print("imprimir todo el archivo")
with open("ejemploArchivo.txt","r") as file:
    print(file.read())

print("leer dos líneas y después 5 caracteres")
with open("ejemploArchivo.txt","r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))

print("almacenar el contenido de una lista y mmostrar el ultimo elemento")
with open("ejemploArchivo.txt","r") as file:
    contenido = file.readlines()
    print(contenido [-1])
