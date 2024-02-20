'''
carreras_controler.py: Contiene el controlador de Carreras.
'''
from views.alumnos_view import alumnos_view, modalWindow
from models.alumnos_model import alumnos_model

class alumnos_controler():
    """Nombres_controller se encarga de manejar la vista y el modelo que sera representado de la ventana modal.
    """
    def __init__(self, root: object) -> None:
        self.root = root
        # Instancia el modelo.
        self.model = alumnos_model()
        # Crea  un istancia la vista.
        self.view = alumnos_view(self.root)
        # Añade la función addToTreeview al botón de agregar.
        self.view.buttonAdd["command"] = self.addToTreeview
        # Añade la función removeFromTreeview al botón de eliminar.
        self.view.buttonUpdate["command"] = self.updateFromTreeview
        # Añade la función updateFromTreeview al botón de actualizar.
        self.view.buttonRemove["command"] = self.removeFromTreeview
        # Añade la función loadTreeviewToEntry al evento de selección de fila.
        self.view.buttonExit["command"] = self.__del__

        # Añade la función loadTreeviewToEntry al evento de selección de fila.
        #self.view.treeview.bind('<<TreeviewSelect>>', self.loadTreeviewToEntry)
        # Carga los datos de la base de datos al treeview.
        self.loadToTreeview()

        pass

    def loadToTreeview(self):
        """loadToTreeview(): Carga los datos de la base de datos al treeview.
        """
        data = self.model.getAllData()
        self.view.setTreeview(data)

    def addToTreeview(self):
        """addToTreeview(): Agrega un registro a la base de datos y al treeview.
        """
        # Crea una instancia de la ventana modal
        self.modal = modalWindow(self.root, 'Altas de Alumnos')

        #Solo si hay un registro seleccionado el el treeview.
        if self.modal.buttonClicked:
            if self.modal.textvarApellido.get() != '' and \
                self.modal.textvarNombre.get() != '' and \
                self.modal.textvarInscripcion.get() != '' and \
                self.modal.textvarCursoId.get() != '' :

                self.addToDB()
                self.loadToTreeview()
                self.clearForm()
            else:
                self.view.showMessageBox(message='Debe llenar todos los campos.', title='Error', type='error')

    def removeFromTreeview(self):
        """removeFromTreeview Elimina un registro de la base de datos y del treeview.
        """
        #Solo si hay un registro seleccionado el el treeview.
        if self.view.treeview.selection():
            # Crea una instancia de la ventana modal
            self.modal = modalWindow(self.root, 'Bajas de Alumnos', self.loadTreeviewToEntry())

            if self.modal.buttonClicked:
                    self.removeFromDB()
                    self.loadToTreeview()
                    self.clearForm()

    def updateFromTreeview(self):
        """updateFromTreeview Actualiza un registro de la base de datos y del treeview.
        """
        #Solo si hay un registro seleccionado el el treeview.
        if self.view.treeview.selection():
            # Crea una instancia de la ventana modal
            self.modal = modalWindow(self.root, 'Modificación de Alumnos', self.loadTreeviewToEntry())

            if self.modal.buttonClicked:
                    self.updateDB()
                    self.loadToTreeview()
                    self.clearForm()

    def loadTreeviewToEntry(self, event=None)-> tuple:
        """loadTreeviewToEntry(): retorna una tupla del campo seleccionado.

        Args:
            event (None, optional): Defaults to None.

        Returns:
            tuple: devuelve una tupla con id, apellido, nombre, inscripcion, cursoId.
        """
        #Solo si hay un registro seleccionado el el treeview.
        if self.view.treeview.selection():
            self.id = self.view.getCursorId()
            self.apellido = self.view.getCursorApellido()
            self.nombre = self.view.getCursorNombre()
            self.inscripcion = self.view.getCursorInscripcion()
            self.cursoId = self.view.getCursorCursorId()

        return (self.id,
                self.apellido,
                self.nombre,
                self.inscripcion,
                self.cursoId)

    def addToDB(self)->None:
        """addToDB(): realiza un nuevo registro en la DB.
        """
        apellido = self.modal.getApellido()
        nombre = self.modal.getNombre()
        inscripcion = self.modal.getInscripcion()
        cursoId = self.modal.getCursoId()
        self.model.create(apellido, nombre, inscripcion, cursoId)

    def updateDB(self)->None:
        """updateDB(): actualiza un registro en la DB.
        """
        id = self.view.getCursorId()
        apellido = self.modal.getApellido()
        nombre = self.modal.getNombre()
        inscripcion = self.modal.getInscripcion()
        cursoId = self.modal.getCursoId()
        self.model.update(id, apellido, nombre, inscripcion, cursoId)

    def removeFromDB(self):
        id = self.view.getCursorId()
        self.model.delete(id)

    def clearForm(self):
        self.modal.setId('')
        self.modal.setNombre('')
        self.modal.setApellido('')
        self.modal.setInscripcion('')
        self.modal.setCursoId(0)

        #Deselecciona fila de treeview.
        self.view.treeview.selection_remove(self.view.treeview.selection())

        return

    def __del__(self) -> None:
        #self.model.__del__
        #self.view.__del__
        
        self.view.ventana_modal.destroy()
        self.view.frame3.destroy()
        self.view.frame4.destroy()

        #del self
