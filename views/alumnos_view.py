#views.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
from ttkbootstrap import Style
from centrar_ventana import centrar

class alumnos_view():
    def __init__(self, root) -> None:
        '''Constructor de la clase'''
        self.root = root
        # self.root.title('Gestión de Nombres')
        self.estilo=Style("darkly")
        self.ventana_modal = tk.Toplevel(self.root)
        self.ventana_modal.title("Gestion de Alumnos")
        self.ventana_modal.geometry(centrar(alto=360, ancho=640, app=self.root))
        self.ventana_modal.resizable(False, False)
        # Hacer que la ventana modal sea transitoria y modal
        self.ventana_modal.transient(self.root)
        # Bloquea el enfoque en la ventana modal
        self.ventana_modal.grab_set()

        #Aplicamos estilos y los modificamos para la cabecera del treeview.
        # self.style = ttk.Style(self.root)
        # self.style.theme_use('clam')
        # self.style.configure("Treeview.Heading", background='grey', foreground='white')

        #Define el Nombre y el ancho en píxeles de las columnas.
        columns = {'Id': 50, 'Apellido': 180, 'Nombre': 180, 'Inscripcion': 90, 'Curso Id': 90}
        self.treeview = ttk.Treeview(self.ventana_modal, columns=tuple(columns.keys()), show='headings', height=14, selectmode='browse')
        #Define las cabeceras
        for clave, valor in columns.items():
            self.treeview.heading(clave, text=clave)
            self.treeview.column(clave, width=valor)

        self.treeview.grid(row=0, column=0, sticky='nsew')

        #Añade un barra lateral de scroll (enrollado).
        scrollbar = ttk.Scrollbar(self.ventana_modal, orient=tk.VERTICAL, command=self.treeview.yview)
        #self.treeview.configure(yscroll=scrollbar.set)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.frame3 = ttk.Frame(self.ventana_modal, border=0)
        self.frame3.grid(padx=5, pady=5, row=2, column=0, sticky='nsesw')

        self.buttonAdd = ttk.Button(self.frame3, text='Añadir')
        self.buttonAdd.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.buttonUpdate = ttk.Button(self.frame3, text='Actualizar')
        self.buttonUpdate.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.buttonRemove = ttk.Button(self.frame3, text='Eliminar')
        self.buttonRemove.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.buttonExit = ttk.Button(self.frame3, text='Salir')
        self.buttonExit.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.frame4 = ttk.Frame(self.ventana_modal, border=1, relief='groove')
        self.frame4.grid(padx=5, pady=5, row=3, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)

        statusbar = tk.Label(self.frame4, text='Tabla Alumnos', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def getCursorId(self) -> str:
        '''getCursorId obtiene el valor de Id del cursor.

        Returns:
            str: devuelve el valor de Id del cursor.
        '''
        selectedLbData = self.treeview.selection()[0]
        id = self.treeview.item(selectedLbData)['values'][0]
        return id

    def getCursorNombre(self) -> str:
        '''getCursorNombre obtiene el valor de Nombre del cursor.

        Returns:
            str: devuelve el valor de Nombre del cursor.
        '''
        selectedLbData = self.treeview.selection()[0]
        Nombre = self.treeview.item(selectedLbData)['values'][1]
        return Nombre

    def getCursorApellido(self) -> str:
        selectedLbData = self.treeview.selection()[0]
        apellido = self.treeview.item(selectedLbData)['values'][2]
        return apellido

    def getCursorInscripcion(self):
        selectedLbData = self.treeview.selection()[0]
        inscripcion = self.treeview.item(selectedLbData)['values'][3]
        return inscripcion

    def getCursorCursorId(self):
        selectedLbData = self.treeview.selection()[0]
        cursorId = self.treeview.item(selectedLbData)['values'][4]
        return cursorId

    def setTreeview(self, data: list):
        '''setTreeview pones datos en el treeview

        Args:
            data (list): recibe datos como lista.
        '''
        #Sale si no trae datos y evita la asignación de datos vacios.
        if not data: return

        #Elimina los datos anteriores.
        self.treeview.delete(*self.treeview.get_children())
        #Asigna los datos del data.
        for row in data:
            #Inserta una row en el treeview.
            self.treeview.insert('', tk.END, text=row[0], values=row)

    def showMessageBox(self, message: str, title: str, type: str):
        '''showMessageBox muestra un mensaje en una ventana emergente.

        Args:
            message (str): mensaje a mostrar.
            title (str): Nombre de la ventana.
            type (str): tipo de ventana.
        '''
        if type == 'info':
            messagebox.showinfo(title, message)
        elif type == 'warning':
            messagebox.showwarning(title, message)
        elif type == 'error':
            messagebox.showerror(title, message)

class modalWindow:
    def __init__(self, parent, Nombre, datos=()) -> None:
        self.parent = parent

        self.modal = tk.Toplevel(self.parent)
        self.modal.geometry(centrar(alto=280, ancho=425, app=self.parent))
        # self.modal.geometry(centrar(alto=230, ancho=410, app=self.parent))
        self.modal.title(Nombre)

        # Fija el redimensionamiento de la ventana
        self.modal.resizable(False, False)
        # Hacer que la ventana modal sea transitoria y modal
        self.modal.transient(parent)
        # Bloquea el enfoque en la ventana modal
        self.modal.grab_set()

        self.frame1 = ttk.Frame(self.modal, border=2, relief='groove')
        self.frame1.grid(padx=10, pady=10, row=0, column=0, sticky='nsew')

        self.labelId = ttk.Label(self.frame1, text='Id: ')
        self.labelId.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.textvarId = tk.StringVar()
        self.entryId = ttk.Entry(self.frame1, textvariable=self.textvarId, state='disabled')
        self.entryId.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.labelApellido = ttk.Label(self.frame1, text='Apellido: ')
        self.labelApellido.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        self.textvarApellido = tk.StringVar()
        self.entryApellido = ttk.Entry(self.frame1, textvariable=self.textvarApellido, width=50)
        self.entryApellido.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.labelNombre = ttk.Label(self.frame1, text='Nombre: ')
        self.labelNombre.grid(row=2, column=0, padx=5, pady=5, sticky='e')

        self.textvarNombre = tk.StringVar()
        self.entryNombre = ttk.Entry(self.frame1, textvariable=self.textvarNombre, width=50)
        self.entryNombre.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.labelInscripcion = ttk.Label(self.frame1, text='Inscripcion: ')
        self.labelInscripcion.grid(row=3, column=0, padx=5, pady=5, sticky='e')

        self.textvarInscripcion = tk.StringVar()
        self.entryInscripcion = ttk.Entry(self.frame1, textvariable=self.textvarInscripcion, width=50)
        self.entryInscripcion.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.labelCursoId = ttk.Label(self.frame1, text='Curso ID: ')
        self.labelCursoId.grid(row=4, column=0, padx=5, pady=5, sticky='e')

        self.textvarCursoId = tk.IntVar()
        self.entryCursoId = ttk.Entry(self.frame1, textvariable=self.textvarCursoId)
        self.entryCursoId.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.frame2 = tk.Frame(self.modal)
        self.frame2.grid(padx=5, pady=5, row=2, column=0, sticky='nsesw')

        self.aceptarButton = tk.Button(self.frame2, text="Aceptar", command=lambda: self.close_modal(True))
        #self.aceptarButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.aceptarButton.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        self.cancelarButton = tk.Button(self.frame2, text="Cancelar", command=lambda: self.close_modal(False))
        #self.cancelarButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='e')
        self.cancelarButton.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X, expand=True)

        # Si vienen datos en la tupla se copian en los StingVar del formulario.
        # Da Falso cuando datos es None.
        if datos:
            self.setId(datos[0])
            self.setApellido(datos[1])
            self.setNombre(datos[2])
            self.setInscripcion(datos[3])
            self.setCursoId(datos[4])

        # Establece el enfoque en la ventana modal.
        self.modal.focus_set()
        # Establecer el enfoque en el botón de cierre.
        self.entryNombre.focus_set()
        self.modal.wait_window(self.modal)

    def close_modal(self, buttonClicked=False) -> None:
        # Define la propiedad buttonCliked para guardar el boton pulsado.
        self.buttonClicked = buttonClicked
        # Liberar el bloqueo del enfoque
        self.modal.grab_release()
        # Eliminación completa del widget
        self.modal.destroy()

    def getId(self) -> str:
        '''getId Obtiene el valor de textvarId

        Returns:
            str: retorna el valor de textvarId
        '''
        return self.textvarId.get()

    def setId(self, id: str) -> None:
        '''setId establece el valor de textvarId.

        Args:
            id (str): valor de textvarId.
        '''
        self.textvarId.set(id)

    def getApellido(self) -> str:
        return self.textvarApellido.get()

    def setApellido(self, Nombre: str) -> None:
        self.textvarApellido.set(Nombre)

    def getNombre(self):
        return self.textvarNombre.get()
        # '%Y-%m-%d'

    def setNombre(self, inicio: str) -> None:
        self.textvarNombre.set(inicio)

    def getInscripcion(self):
        return datetime.strptime(self.textvarInscripcion.get(), "%Y-%m-%d")
        # '%Y-%m-%d' '%d-%m-%Y'

    def setInscripcion(self, Fin: str) -> None:
        self.textvarInscripcion.set(Fin)

    def getCursoId(self) -> int:
        return self.textvarCursoId.get()

    def setCursoId(self, curso_id: int) -> None:
        self.textvarCursoId.set(curso_id)
