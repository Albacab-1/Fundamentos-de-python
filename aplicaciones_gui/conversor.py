from tkinter import*     # el asterísco  es un comodín que le dice a Python: “Importa todo lo público del módulo”.
from tkinter import ttk

def calcular(*args):
    try:
        valor = float (pies.get()) #se dice parcial y es una conversión de datos y se asigna a la variable valor
        metros.set((0.3048*valor*10000.0+0.5)/10000.0) #con el valor SET se establece
    except ValueError: #no estamos validando otro tipo de datos, pero si te es posible conviertelo, sino no se hace nada
        pass   #aquí no hace nada (comentario de arriba)

raiz = Tk() #objeto principal, es la ventana aquí se crea el objeto que se llama raíz, de ahí se crean ramas (widgets)
raiz.title ("pies a metros") #es el titulo de la ventana

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12") #objet tipo frame (marco) es un contenedor que se usa para organizar y agrupar widgets (como botones, etiquetas, cajas de texto, etc.) dentro de una ventana. 
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E,S)) #el sticky es a donde se mueve
marcoPrincipal.columnconfigure(0,weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

pies = StringVar()
metros = StringVar()


txtPies = ttk.Entry(marcoPrincipal, width=7, textvariable=pies) # es nuestra caja de texto,() eso indica donde lo vamos a poner, el texttvariable es para que lo que se ingrese se valla a ese objeto. sin preocupación manual
txtPies.grid(column=2, row=1, sticky= (W, E)) 

ttk.Label(marcoPrincipal, textvariable=metros).grid(column=1, row=1, sticky=(W,E))
ttk.Button(marcoPrincipal,text="Calcular", command= calcular).grid(column=3, row=3, sticky=W) #command es llamar ala función

ttk.Label(marcoPrincipal, text="pies").grid(column=3, row=1, sticky= W)
ttk.Label(marcoPrincipal, text="es equivalente a:").grid(column=1, row=2, sticky=E)
ttk.Label(marcoPrincipal,text="metros").grid(column=3, row=2, sticky= W)

for child in marcoPrincipal.winfo_children(): #pad x y y, es la distancia wigdet a la ventana, es el margen del borde al inicio del texto
    child.grid_configure(padx=5, pady=5)

txtPies.focus() #aqui es donde puede escribir con focus
raiz.bind('<Return>',calcular) #Return es el nombre de la tecla enter, y se dice que cuando se presione la tecla, llame a la función calcular

raiz.mainloop() # este es un ciclo que hace que se empiece a correr