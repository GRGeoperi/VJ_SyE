import tkinter as tk
from PIL import Image, ImageTk

def crear_cuadricula(raiz, filas, columnas, imagenes):
    cuadriculas = []
    for i in range(filas):
        raiz.grid_rowconfigure(i, weight=1)
    for i in range(columnas):
        raiz.grid_columnconfigure(i, weight=1)
    for i in range(filas):
        fila = []
        for j in range(columnas):
            imagen = Image.open(imagenes[i][j])
            width, height = imagen.size  # Obtener el tamaño de la imagen
            img = ImageTk.PhotoImage(imagen)
            label = tk.Label(raiz, image=img, borderwidth=2, relief="solid")
            label.image = img  # Mantener una referencia a la imagen para evitar que se elimine por el recolector de basura
            label.grid(row=i, column=j, sticky='nsew')
            label.grid_propagate(False)  # Desactivar el ajuste automático del widget Label
            label.config(width=width, height=height)  # Establecer el tamaño de la etiqueta al tamaño de la imagen
            fila.append(label)  # Agregar el label a la fila
        cuadriculas.append(fila)
    return cuadriculas

def main():
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Serpientes y escaleras")
    imagenes = [
        ["imagenes/alarm.gif", "imagenes/alice.gif", "imagenes/alligator.gif", "imagenes/anacondaq.gif"],
        ["imagenes/angeling.gif", "imagenes/antonio.gif", "imagenes/banshee.gif", "imagenes/bathory.gif"],
        ["imagenes/carat.gif", "imagenes/cenere.gif", "imagenes/crab.gif", "imagenes/cruiser.gif"],
        ["imagenes/deviling.gif", "imagenes/deviruchi.gif", "imagenes/d_frame.gif", "imagenes/disguise.gif"],
        ["imagenes/domovoi.gif", "imagenes/drake.gif", "imagenes/elvira.gif", "imagenes/entweihen.gif"]
        ]
    crear_cuadricula(ventanaPrincipal, 5, 4, imagenes)
    ventanaPrincipal.mainloop()

if __name__ == "__main__":
    main()
