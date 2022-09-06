from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

class Fail:
    def __init__(self, data):
        self.id = data['id']
        self.description = data['description']
        self.failure = data['failure']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.Machine_id = data['Machine_id']
        self.User_id = data['User_id']
        self.model = data['model']
        self.image = data['image']

    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO faults (description, failure, Machine_id, User_id) VALUES (%(description)s, %(failure)s, %(Machine_id)s, %(User_id)s)"
        result = connectToMySQL('impresion3D').query_db(query, formulario) #me regresan el nuevo ID de la persona registrada
        #result = 5
        return result

    @classmethod
    def show(cls,formulario):
        #query = "SELECT Users.last_name, Machines.model, faults.description, faults.failure FROM Users INNER JOIN Machines ON Machines.User_id = Machines.id INNER JOIN faults ON Users.id = faults.id WHERE Users.id = %(id)s"
        query = "SELECT faults.*, Machines.model, Machines.image FROM faults LEFT JOIN Users ON Users.id = faults.User_id LEFT JOIN Machines ON Machines.id = faults.Machine_id WHERE Users.id = %(id)s"
        results = connectToMySQL('impresion3D').query_db(query,formulario)
        repairs = []

        for x in results:
            repairs.append(cls(x))

        return repairs

    @classmethod
    def delete(cls, formulario): #Recibe formulario con id de receta a borrar
        query = "DELETE FROM faults WHERE id = %(id)s"
        result = connectToMySQL('impresion3D').query_db(query, formulario)
        return result

    @classmethod
    def update(cls, formulario):
        query = "UPDATE faults SET description=%(description)s, failure=%(failure)s, image=%(image)s WHERE id = %(Machine_id)s"
        result = connectToMySQL('impresion3D').query_db(query, formulario)
        return result
    
    @staticmethod
    def valid_repair(formulario): 

        es_valido = True 

        if formulario['description'] == "":
            flash('The description value is not correct', 'create')
            es_valido = False

        if formulario['failure'] == "":
            flash('The widht value is not correct', 'create')
            es_valido = False
        
        return es_valido
    
    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT faults.*, Machines.model, Machines.image FROM faults LEFT JOIN Users ON Users.id = faults.User_id LEFT JOIN Machines ON Machines.id = faults.Machine_id WHERE faults.id = %(id)s"
        result = connectToMySQL('impresion3D').query_db(query, formulario) 
        repair = cls(result[0])
        return repair

        



    
