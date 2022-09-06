from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

class Machine:
    def __init__(self, data):
        self.id = data['id']
        self.model = data['model']
        self.type_machine = data['type_machine']
        self.tall = data['tall']
        self.width = data['width']
        self.year = data['year']
        self.material = data['material']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.User_id = data['User_id']

    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO Machines (model, type_machine, tall, width, year, material, User_id, image) VALUES \
        (%(model)s, %(type_machine)s, %(tall)s, %(width)s, %(year)s, %(material)s, %(User_id)s, %(image)s)"
        result = connectToMySQL('impresion3D').query_db(query,formulario) #Return Id machine
        return result

    @classmethod
    def get_by_id(cls,formulario):
        query = "SELECT * FROM Machines WHERE id = (%(id)s)"
        result = connectToMySQL('impresion3D').query_db(query,formulario) 
        machine = cls(result[0]) #Instance of Machine
        return machine

    @staticmethod
    def valida_maquina(formulario):
        es_valido = True

        if len(formulario['model']) < 3:
            flash('The model value is not correct', 'machine')
            es_valido = False

        if len(formulario['type_machine']) < 3:
            flash('The type machine value is not correct', 'machine')
            es_valido = False
        
        if len(formulario['tall']) < 1:
            flash('The tall value is not correct', 'machine')
            es_valido = False

        if len(formulario['width']) < 1:
            flash('The widht value is not correct', 'machine')
            es_valido = False
        
        if formulario['year'] == "":
            flash('The year value is not correct', 'machine')
            es_valido = False
                
        if len(formulario['material']) < 3:
            flash('The material value is not correct', 'machine')
            es_valido = False

        return es_valido
    



