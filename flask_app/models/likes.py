from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash


class Like:
    def __init__(self, data):
        self.Drawing_id = data['Drawing_id']
        self.User_id= data['User_id']


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO likes (Drawing_id, User_id) VALUES (%(Drawing_id)s, %(User_id)s)"
        result = connectToMySQL('impresion3D').query_db(query, formulario)
        return result

    @staticmethod
    def show_by_id(formulario):
        query = "SELECT COUNT(Drawing_id) FROM Likes WHERE Drawing_id = (%(id)s)"
        result = connectToMySQL('impresion3D').query_db(query, formulario)
        return result

    