from tkinter import*     # el asterísco  es un comodín que le dice a Python: “Importa todo lo público del módulo”.
from tkinter import ttk

raiz = Tk() #objeto principal, es la ventana aquí se crea el objeto que se llama raíz, de ahí se crean ramas (widgets)
raiz.title ("Inicio de sesión") #es el titulo de la ventana
raiz.geometry ("300x150") #tamaño de ventana

marcoPrincipal = ttk.Frame(raiz, padding="10 10 10 10") #objet tipo frame (marco) es un contenedor que se usa para organizar y agrupar widgets (como botones, etiquetas, cajas de texto, etc.) dentro de una ventana. 
marcoPrincipal.pack(padx = 10, pady= 10)
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E,S)) #el sticky es a donde se mueve
marcoPrincipal.columnconfigure(0,weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

contraseña = StringVar()
usuario = StringVar()


txtusuario = ttk.Entry(marcoPrincipal, width=20, textvariable = usuario) # es nuestra caja de texto,() eso indica donde lo vamos a poner, el texttvariable es para que lo que se ingrese se valla a ese objeto. sin preocupación manual
txtusuario.grid(column=1, row=1, sticky= (W,E)) 

txtcontraseña = ttk.Entry(marcoPrincipal, width = 20, textvariable = contraseña)
txtcontraseña.grid(column=1, row=2, sticky= (W,E)) 

ttk.Label(marcoPrincipal, text="Usuario:").grid(column=0, row=1, sticky=(E))
ttk.Label(marcoPrincipal, text="Contraseña").grid(column=0, row=2, sticky=(E))
ttk.Button(marcoPrincipal,text="Ingresar").grid(column=3, row=3, sticky=(W,E)) #command es llamar ala función


raiz.mainloop() # este es un ciclo que hace que se empiece a correr