#EJECUTA nuestra aplicación
from flask_app import app

#Importando mi controlador
from flask_app.controllers import users_controller
from flask_app.controllers import machines_controller
from flask_app.controllers import faults_controller
from flask_app.controllers import designs_controller
from flask_app.controllers import prints_controller
from flask_app.controllers import likes_controller

if __name__=="__main__":
    app.run(debug=True)