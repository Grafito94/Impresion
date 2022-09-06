from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.machines import Machine
from flask_app.models.users import User

from werkzeug.utils import secure_filename
import os
#Para subir imagenes

@app.route('/machine/save', methods = ['POST'])
def SaveMachine():

    if 'user_id' not in session:
        return redirect('/')

    if not Machine.valida_maquina(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/machines')

    if 'image' not in request.files:
        flash('imagen no encontrada','machine')
        return redirect('/machines')

    image = request.files['image'] #Se guarda la imagen en una variable

    if image.filename == '':
        flash('Nombre de imagen vacio', 'machine')
        return redirect('/machines')

    nombre_imagen = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen)) #De todo el sistema operativo me das todo el pad

    formulario ={
        "model" : request.form['model'],
        "type_machine" : request.form['type_machine'],
        "tall" : request.form['tall'],
        "width" : request.form['width'],
        "year" : request.form['year'],
        "material" : request.form['material'],
        "User_id" : request.form['User_id'],
        "image" : nombre_imagen
    }

    machine = Machine.save(formulario)
    session['machine_id'] = machine

    return redirect('/machine/failure')

@app.route('/machine/failure')
def ViewBroke():

    if 'user_id' not in session and 'machine_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['machine_id']
    }

    formulario1 = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario1)
    machine = Machine.get_by_id(formulario) #Falta method


    return render_template('machinefail.html',user = user, machine = machine)
