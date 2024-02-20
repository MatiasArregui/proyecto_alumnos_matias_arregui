#carreras_models.py
from datetime import date
from database import dbConn

class alumnos_model():
    '''carrerasModel Modelo de la tabla carreras.
    '''
    def __init__(self) -> None:
        '''__init__ Constructor de la clase, establece la conexión a la base
        de datos e intenta crear la tabla si no existe..
        '''
        self.nombre = ''
        self.apellido = ''
        self.inscripcion = None
        self.cursos_id = 0

        #Abre la conexión con la base de datos alumnos y si no existe la crea.
        self.conn = dbConn.dbConn('database\\alumnos.sqlite3')
        #Crea la tabla carreras si no existe.
        tableName = 'alumnos'
        fieldsDescripcion = '('\
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '\
            'apellido TEXT NOT NULL UNIQUE, '\
            'nombre TEXT NOT NULL, '\
            'inscripcion DATE NOT NULL, '\
            'cursos_id INTEGER NOT NULL)'
        #Ejecuta el comando en la base de datos.
        self.conn.createTable(tableName=tableName, fieldsDescripcion=fieldsDescripcion)

    def create(self, apellido:str, nombre:str, inscripcion:date, cursos_id:int) -> list:
        command = 'INSERT INTO alumnos (apellido, nombre, inscripcion, cursos_id) VALUES (?, ?,date(?), ?)'
        values = (apellido, nombre, inscripcion, cursos_id)
        return self.conn.execute(command, values)

    def read(self, id: int) -> list:
        '''read Lee un registro de la base de datos.

        Args:
            id (int): Id del registro a leer.

        Returns:
            list: Retorna el registro leído.
        '''
        command = 'SELECT * FROM alumnos WHERE id = ?'
        values = (id,)
        return self.conn.execute(command, values)

    def update(self, id: str, apellido: str, nombre:str, inscripcion:date, cursos_id:int) -> list:
        command = 'UPDATE alumnos SET apellido = ?, nombre = ?, inscripcion = date(?), cursos_id = ? WHERE id = ?'
        values = (apellido, nombre, inscripcion, cursos_id, id)
        return self.conn.execute(command, values)

    def delete(self, id: str) -> list:
        '''delete Borra un registro de la base de datos.

        Args:
            id (str): Id del registro a borrar.

        Returns:
            list: Devuelve el registro borrado.
        '''
        command = 'DELETE FROM alumnos WHERE id = ?'
        values = (id,)
        return self.conn.execute(command, values)

    def getAllData(self) -> list:
        '''getAllData Recupera todos los registros de la base de datos.

        Returns:
            list: devuelve una lista de carreras.
        '''
        command = 'SELECT * FROM alumnos'
        return self.conn.execute(command)

    def __del__(self) -> None:
        '''__del__ Destructor de la clase.'''
        del self.conn
        del self
