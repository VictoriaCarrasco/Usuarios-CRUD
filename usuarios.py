
from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo_electronico = data['correo_electronico']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('sql_usuarios').query_db(query)
        usuarios = []
        for u in results:
            usuarios.append(cls(u))
        return usuarios
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre,apellido,correo_electronico) VALUES (%(nombre)s,%(apellido)s,%(correo_electronico)s);"
        result = connectToMySQL('sql_usuarios').query_db(query,data)
        return result
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('sql_usuarios').query_db(query,data)
        return cls(result[0])

    
    @classmethod
    def update(cls, data):
        query = "UPDATE usuarios SET nombre=%(nombre)s,apellido=%(apellido)s,correo_electronico=%(correo_electronico)s,fecha_creacion=NOW() WHERE id = %(id)s;"
        return connectToMySQL('sql_usuarios').query_db(query,data)
        
    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('sql_usuarios').query_db(query,data)