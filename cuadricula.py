import tkinter as tk
from PIL import Image, ImageTk

def crear_cuadricula(raiz, filas, columnas, imagenes, tamano):
    cuadriculas = []
    for i in range(filas):
        raiz.grid_rowconfigure(i, weight=1)
    for i in range(columnas):
        raiz.grid_columnconfigure(i, weight=1)
    for i in range(filas):
        fila = []
        for j in range(columnas):
            imagen = Image.open(imagenes[i][j])
            imagen.thumbnail((tamano, tamano))  # Escalar imagen conservando la proporción
            img = ImageTk.PhotoImage(imagen)
            label = tk.Label(raiz, image=img, borderwidth=2, relief='sunken')
            label.image = img  # Mantener una referencia a la imagen para evitar que se elimine por el recolector de basura
            label.grid(row=i, column=j, sticky='nsew')
            fila.append(label)  # Agregar el label a la fila
        cuadriculas.append(fila)
    return cuadriculas

def main():
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Serpientes y escaleras")
    imagenes = [
        ["imagenes/alarm.gif", "imagenes/alice.gif", "imagenes/alligator.gif", "imagenes/anacondaq.gif","imagenes/angeling.gif", "imagenes/antonio.gif", "imagenes/banshee.gif", "imagenes/bathory.gif", "imagenes/carat.gif", "imagenes/cenere.gif", "imagenes/crab.gif", "imagenes/cruiser.gif", "imagenes/deviling.gif", "imagenes/deviruchi.gif", "imagenes/d_frame.gif", "imagenes/disguise.gif","imagenes/domovoi.gif", "imagenes/drake.gif", "imagenes/elvira.gif", "imagenes/entweihen.gif"],
        ["imagenes/evil_cloud.gif", "imagenes/evil_druid.gif", "imagenes/executioner.gif", "imagenes/fallen_bishop.gif","imagenes/ferus.gif", "imagenes/flame_skull.gif", "imagenes/flora.gif", "imagenes/fur_seal.gif","imagenes/galapago.gif", "imagenes/galion.gif","imagenes/garden_keeper.gif","imagenes/gargoyle.gif","imagenes/g_general.gif","imagenes/ghostring.gif","imagenes/ghoul.gif","imagenes/giant_octopus.gif","imagenes/gibbet.gif","imagenes/goblin.gif","imagenes/goblin_leader.gif","imagenes/hell_poddle.gif"],
        ["imagenes/hidden_priest.gif","imagenes/hydro.gif","imagenes/incantation.gif","imagenes/incarnation.gif","imagenes/jakk.gif","imagenes/joker.gif","imagenes/khali.gif","imagenes/kiel.gif","imagenes/king_k.gif","imagenes/knight.gif","imagenes/kobold.gif","imagenes/kraken.gif","imagenes/ktullanux.gif","imagenes/kubkin.gif","imagenes/lava_g.gif","imagenes/leaf_cat.gif","imagenes/leak.gif","imagenes/lit_fatum.gif","imagenes/live_peach.gif","imagenes/loli_ruri.gif"],
        ["imagenes/lora.gif","imagenes/lude.gif","imagenes/magnolia.gif","imagenes/mananan.gif","imagenes/mang.gif","imagenes/marduk.gif","imagenes/marionette.gif","imagenes/mavka.gif","imagenes/muka.gif","imagenes/mummy.gif","imagenes/myst.gif","imagenes/necromancer.gif","imagenes/nightmare.gif","imagenes/noxious.gif","imagenes/nydhog.gif","imagenes/orc_hero.gif","imagenes/orc_skeleton.gif","imagenes/owl.gif","imagenes/panzer.gif","imagenes/petal.gif"],
        ["imagenes/phendark.gif","imagenes/piamette.gif","imagenes/pirate.gif","imagenes/pitman.gif","imagenes/pom_spider.gif","imagenes/quve.gif","imagenes/raggler.gif","imagenes/raydric.gif","imagenes/red_eruma.gif","imagenes/removal.gif","imagenes/requiem.gif","imagenes/retribution.gif","imagenes/rice_cake.gif","imagenes/rybio.gif","imagenes/sedora.gif","imagenes/shadow.gif","imagenes/shelter.gif","imagenes/shinobi.gif","imagenes/ske.gif","imagenes/skeleton_p.gif"]
        ]
    crear_cuadricula(ventanaPrincipal, 5, 20, imagenes, 80)
    ventanaPrincipal.mainloop()

if __name__ == "__main__":
    main()
