from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

class Print:
    def __init__(self,data):
        self.id = data['id']
        self.direction_send = data['direction_send']
        self.date_send = data['date_send']
        self.telephone = data['telephone']
        self.city = data['city']
        self.creted_at = data['created_at']
        self.updated_at = data['updated_at']
        self.logo = data['logo']

        #import User_id, Drawing_id
        self.User_id = data['User_id']
        self.Drawing_id = data['Drawing_id']



    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO prints (direction_send, date_send, User_id, Drawing_id, telephone, city) VALUES (%(direction_send)s, %(date_send)s, %(User_id)s, %(Drawing_id)s, %(telephone)s, %(city)s)"
        result = connectToMySQL('impresion3D').query_db(query, formulario) #me regresan el nuevo ID de la persona registrada
        #result = 5
        return result

    @classmethod
    def show(cls,formulario):
        query = "SELECT prints.* FROM prints LEFT JOIN Users ON Users.id = prints.User_id LEFT JOIN Drawings ON Drawings.id = prints.Drawing_id WHERE Drawing_id = %(id)s"
        results = connectToMySQL('impresion3D').query_db(query,formulario)
        repairs = []

        for x in results:
            print(x)
            repairs.append(cls(x))
        return repairs

    @staticmethod
    def valida_print(formulario):
        es_valido = True

        if len(formulario['direction_send']) < 3:
            flash('The direction value is not correct', 'print')
            es_valido = False

        if formulario['date_send'] == "":
            flash('The year value is not correct', 'print')
            es_valido = False
                

        return es_valido
    
    @classmethod
    def show_by_id(cls,formulario):
        print(formulario)
        query = "SELECT prints.*, Drawings.logo FROM prints LEFT JOIN Users ON Users.id = prints.User_id LEFT JOIN Drawings ON Drawings.id = prints.Drawing_id WHERE Users.id = %(id)s"
        results = connectToMySQL('impresion3D').query_db(query,formulario)
        print(results)
        prints = []
        print(prints)
        for x in results:
            print(x)
            prints.append(cls(x))
        return prints

