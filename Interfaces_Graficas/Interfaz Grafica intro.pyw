from tkinter import *

# clase Tk, raiz/root, contenedor general del frame donde iran todos los widget, aunque frame tambien es un widget en si.
raiz = Tk()
frame = Frame()


# La mayoria de metodos aplicables a la raiz, tambien lo son al frame.
# pack permite empaquetar el frame dentro de la raiz. Si se le pasa como parametro side="left,right,bottom,etc", quedara anclado donde se le señale. Para usar una segunda cardinalidad se pone segundo parametro "anchor= n,s,w,e" (norte sur este oeste)
# Tambien esta el parametro " fill= "x o y o both" ". Con x el frame se expande en conjunto con la raiz horizontalmente. Para que se expanda verticalmente con "y" hay que añadir segundo parametro " extend= "true" "... Both con extend expande ambos lados junto a la raiz.
frame.pack(fill="both", expand=True)

# justify, justifica el texto, Image=(<nombrevariable donde se almacena imagen>) coloca imagen en lugar de texto, Fg color de la fuente, font tipo de fuente,
label1 = Label(frame, text="Hola hola hola hola", fg="black",
               font=("Comic Sans MS", 18))
label1.place(x=100, y=100)

raiz.title("Ventana de prueba 1")

# Resizable permite o bloquea el ajustar tamaño de la ventana siendo anchoxalto. 1= true 0 = false
raiz.resizable(1, 1)

# Permite asignar icono a la ventana
raiz.iconbitmap(
    "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\Interfaces Graficas\\pikachu.ico")

# raiz.Geometry permite asignar manualmente anchoxalto estandar al iniciar. En el caso del frame, la raiz y ventana se ajusta al tamaño del frame, pero si se agranda ventana podra visibilizarse la diferencia entre el frame y la raiz.
frame.config(width="1080", height="720")

# Relief permite ponerle borde, entre comillas va el tipo de borde. bd=numero permite definir tamaño del borde
frame.config(relief="groove")
frame.config(bd=35)

# bg= background, es decir, color de fondo.
raiz.config(bg="Gray")
frame.config(bg="Blue")


# Ciclo infinito que permite que la ventana se mantenga abierta.
raiz.mainloop()
