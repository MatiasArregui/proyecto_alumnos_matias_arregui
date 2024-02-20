#carreras_models.py
from datetime import date

from database import dbConn

class carreras_model():
    '''carrerasModel Modelo de la tabla carreras.
    '''
    def __init__(self) -> None:
        '''__init__ Constructor de la clase, establece la conexión a la base
        de datos e intenta crear la tabla si no existe..
        '''
        self.nombre = ''
        self.inicio = None
        self.fin = None
        self.duracion = 0

        #Abre la conexión con la base de datos alumnos y si no existe la crea.
        self.conn = dbConn.dbConn('database\\alumnos.sqlite3')
        #Crea la tabla carreras si no existe.
        tableName = 'carreras'
        fieldsDescripcion = '('\
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '\
            'nombre TEXT NOT NULL UNIQUE, '\
            'inicio DATE NOT NULL, '\
            'fin DATE NOT NULL, '\
            'duracion INTEGER NOT NULL)'
        #Ejecuta el comando en la base de datos.
        self.conn.createTable(tableName=tableName, fieldsDescripcion=fieldsDescripcion)

    def create(self, nombre: str, inicio: date, fin: date, duracion: int) -> list:
        command = 'INSERT INTO carreras (nombre, inicio, fin, duracion) VALUES (?, date(?), date(?), ?)'
        values = (nombre, inicio, fin, duracion)
        return self.conn.execute(command, values)

    def read(self, id: int) -> list:
        '''read Lee un registro de la base de datos.

        Args:
            id (int): Id del registro a leer.

        Returns:
            list: Retorna el registro leído.
        '''
        command = 'SELECT * FROM carreras WHERE id = ?'
        values = (id,)
        return self.conn.execute(command, values)

    def update(self, id: str, nombre: str, inicio: date, fin: date, duracion: int) -> list:
        command = 'UPDATE carreras SET nombre = ?, inicio = date(?), fin = date(?), duracion = ? WHERE id = ?'
        values = (nombre, inicio, fin, duracion, id)
        return self.conn.execute(command, values)

    def delete(self, id: str) -> list:
        '''delete Borra un registro de la base de datos.

        Args:
            id (str): Id del registro a borrar.

        Returns:
            list: Devuelve el registro borrado.
        '''
        command = 'DELETE FROM carreras WHERE id = ?'
        values = (id,)
        return self.conn.execute(command, values)

    def getAllData(self) -> list:
        '''getAllData Recupera todos los registros de la base de datos.

        Returns:
            list: devuelve una lista de carreras.
        '''
        command = 'SELECT * FROM carreras'
        return self.conn.execute(command)

    def __del__(self) -> None:
        '''__del__ Destructor de la clase.'''
        del self.conn
        del self

