'''
carreras_controler.py: Contiene el controlador de Carreras.
'''
# from views.carreras_view import carreras_view, modalWindow
# from models.carreras_model import carreras_model

from views.cursos_view import cursos_view, modalWindow
from models.cursos_model import cursos_model

class cursos_controler():
    '''Nombres_controller se encarga de manejar la vista y el modelo.
    '''
    def __init__(self, root: object) -> None:
        self.root = root
        # Instancia el modelo.
        self.model = cursos_model()
        # Crea  un istancia la vista.
        self.view = cursos_view(self.root)
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
        '''loadToTreeview Carga los datos de la base de datos al treeview.
        '''
        data = self.model.getAllData()
        self.view.setTreeview(data)

    def addToTreeview(self):
        '''addToTreeview Agrega un registro a la base de datos y al treeview.'''
        # Crea una instancia de la ventana modal
        self.modal = modalWindow(self.root, 'Altas de Cursos')

        #Solo si hay un registro seleccionado el el treeview.
        if self.modal.buttonClicked:
            if self.modal.textvarNombre.get() != '' and \
                self.modal.textvarNivel.get() != '' and \
                self.modal.textvarCarrerasId.get() != '':
                # and \
                # self.modal.textvarDuracion.get() != '' :

                self.addToDB()
                self.loadToTreeview()
                self.clearForm()
            else:
                self.view.showMessageBox(message='Debe llenar todos los campos.', title='Error', type='error')

    def removeFromTreeview(self):
        '''removeFromTreeview Elimina un registro de la base de datos y del treeview.'''
        #Solo si hay un registro seleccionado el el treeview.
        if self.view.treeview.selection():
            # Crea una instancia de la ventana modal
            self.modal = modalWindow(self.root, 'Bajas de Cursos', self.loadTreeviewToEntry())

            if self.modal.buttonClicked:
                    self.removeFromDB()
                    self.loadToTreeview()
                    self.clearForm()

    def updateFromTreeview(self):
        '''updateFromTreeview Actualiza un registro de la base de datos y del treeview.'''
        #Solo si hay un registro seleccionado el el treeview.
        if self.view.treeview.selection():
            # Crea una instancia de la ventana modal
            self.modal = modalWindow(self.root, 'Modificación de Cursos', self.loadTreeviewToEntry())

            if self.modal.buttonClicked:
                    self.updateDB()
                    self.loadToTreeview()
                    self.clearForm()

    def loadTreeviewToEntry(self, event=None):
        #Solo si hay un registro seleccionado el el treeview.
        if self.view.treeview.selection():
            self.id = self.view.getCursorId()
            self.nombre = self.view.getCursorNombre()
            self.nivel = self.view.getCursorNivel()
            self.carr_id = self.view.getCursorCarrerasId()
            # self.duracion = self.view.getCursorDuracion()

        return (self.id,
                self.nombre,
                self.nivel,
                self.carr_id)

    def addToDB(self):
        nombre = self.modal.getNombre()
        nivel = int(self.modal.getNivel())
        carr_id = int(self.modal.getCarrerasId())
        self.model.create(nombre, nivel, carr_id)

    def updateDB(self):
        id = self.view.getCursorId()
        nombre = self.modal.getNombre()
        nivel = int(self.modal.getNivel())
        carr_id = int(self.modal.getCarrerasId())
        # duracion = self.modal.getDuracion()
        self.model.update(id, nombre, nivel, carr_id)

    def removeFromDB(self):
        id = self.view.getCursorId()
        self.model.delete(id)

    def clearForm(self):
        self.modal.setId('')
        self.modal.setNombre('')
        self.modal.setNivel("")
        self.modal.setCarrerasId("")
        # self.modal.setDuracion(0)

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
