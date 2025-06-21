from tkinter import*     # el asterísco  es un comodín que le dice a Python: “Importa todo lo público del módulo”.
from tkinter import ttk

raiz = Tk() #objeto principal, es la ventana aquí se crea el objeto que se llama raíz, de ahí se crean ramas (widgets)
raiz.title ("Prueba de frame") #es el titulo de la ventana

ventanaMadre = Tk()
ventanaMadre.title ("ventana con varios marcos")
ventanaMadre.geometry ("400x400")


#-------------Marco uno-----------

marcosup = ttk.Frame(ventanaMadre, padding="10")
marcosup.pack (side="top", fill = "x")
ttk.Label(marcosup,text = "Encabezado", front= ("Arial",14)).pack()




'''(column=0, row=0, sticky=(N, W, E,S)) #el sticky es a donde se mueve
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

raiz.mainloop() # este es un ciclo que hace que se empiece a correr'''