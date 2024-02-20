import tkinter as tk
from ttkbootstrap import Style

from controlers.carreras_controler import carreras_controler
from controlers.cursos_controler import cursos_controler
from controlers.alumnos_controler import alumnos_controler
from centrar_ventana import centrar

class mainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Gestion")

        self.estilo= Style("darkly")
        
        # Agregamos un icono a la ventana principal
        self.imagen = tk.PhotoImage(file = "image\\logocarena.png")
        self.root.iconphoto(True, self.imagen)
        self.labelFondo=tk.Label(image= self.imagen, master=self.root).grid(row=1, column=1, padx=170, pady=20)
        self.labelTitulo=tk.Label(text="Instituto Superior Dr. Carlos María Carena", master=self.root).grid(row=5, column=1)
        
        # Crea menubar
        self.menubar = tk.Menu(master=self.root)
        # Asigna menubar a root.
        root.config(menu=self.menubar)
        # Establece el tamaño de la ventana
        root.geometry(centrar(ancho=640, alto=410, app=self.root))
        # Fija el redimensionamiento de la ventana
        root.resizable(False, False)

        # Creamos los componentes del menu flotante
        self.alumnos_menu = tk.Menu(master=self.menubar, tearoff=False)
        self.carreras_menu = tk.Menu(master=self.menubar, tearoff=False)
        self.cursos_menu = tk.Menu(master=self.menubar, tearoff=False)
        # Añade al menu bar los submenu mediante la propiedad menu.
        self.menubar.add_cascade(label="Alumnos", menu=self.alumnos_menu)
        self.menubar.add_cascade(label="Carreras", menu=self.carreras_menu)
        self.menubar.add_cascade(label="Cursos", menu=self.cursos_menu)
        # Añadir funcion al menu de alumnos_menu
        # self.alumnos_menu.add_command(label="Alumnos", command= lambda: alumnos_controler(self.root))
        self.alumnos_menu.add_command(label="Alumnos", command= lambda: self.toggle_menu(3))
        self.alumnos_menu.add_separator()
        self.alumnos_menu.add_command(label="Salir", command=self.root.quit)
        # Añadir funcion al menu de carreras_menu
        self.carreras_menu.add_command(label="Carreras", command=lambda: self.toggle_menu(1))
        self.carreras_menu.add_separator()
        self.carreras_menu.add_command(label="Salir", command=self.root.quit)
        # Añadir funcion al menu de alumnos_menu
        self.cursos_menu.add_command(label="Cursos", command= lambda: self.toggle_menu(2))
        self.cursos_menu.add_separator()
        self.cursos_menu.add_command(label="Salir", command=self.root.quit)
        
    
    def toggle_menu(self, opcion: int) -> None:
        self.menubar.entryconfig(1, state="disabled")
        if opcion == 1:
            carreras_controler(self.root)
        elif opcion == 2:
            cursos_controler(self.root)
        elif opcion == 3:
            alumnos_controler(self.root)
        self.menubar.entryconfig(1, state="normal")



def main():
    root = tk.Tk()
    ventana= mainView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
