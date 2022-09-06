from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

class Draw:
    def __init__(self,data):
        self.id = data['id']
        self.tittle = data['tittle']
        self.type = data['type']
        self.description = data['description']
        self.size = data['size']
        self.STL = data['STL']
        self.logo = data['logo']
        self.user_type = data['user_type']
        self.first_name = data['first_name']
        self.creted_at = data['created_at']
        self.updated_at = data['updated_at']

        #import User_id
        self.User_id = data['User_id']





    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO Drawings (tittle, type, description, size, STL, logo, User_id) VALUES (%(tittle)s, %(type)s, %(description)s, %(size)s, %(STL)s, %(logo)s, %(User_id)s)"
        result = connectToMySQL('impresion3D').query_db(query, formulario) #me regresan el nuevo ID de la persona registrada
        #result = 5
        return result

    @classmethod
    def show(cls,formulario):
        
        query = "SELECT Drawings.*, Users.first_name, Users.user_type FROM Drawings LEFT JOIN Users ON Users.id = Drawings.User_id WHERE Users.id = %(id)s"
        results = connectToMySQL('impresion3D').query_db(query,formulario)
        repairs = []

        for x in results:
            repairs.append(cls(x))

        return repairs

    @classmethod
    def show_all(cls):
        query = "SELECT Drawings.*, Users.first_name, Users.user_type FROM Drawings LEFT JOIN Users ON Users.id = Drawings.User_id"
        results = connectToMySQL('impresion3D').query_db(query)
        repairs = []

        for x in results:
            repairs.append(cls(x))

        return repairs

    @classmethod
    def show_by_id(cls, formulario):
        query = "SELECT Drawings.*, Users.first_name, Users.user_type FROM Drawings LEFT JOIN Users ON Users.id = Drawings.User_id WHERE Drawings.id = %(id)s"
        results = connectToMySQL('impresion3D').query_db(query,formulario)
        draw = cls(results[0])
        print(draw.id)
        return draw

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM likes WHERE Drawing_id = %(id)s "
        
        result = connectToMySQL('impresion3D').query_db(query, formulario)
        return result
    @classmethod
    def delete2(cls, formulario):
        query = "DELETE FROM Drawings WHERE id = %(id)s"
        result = connectToMySQL('impresion3D').query_db(query, formulario)
        return result