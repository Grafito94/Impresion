from flask import render_template, redirect, session, request, flash
from flask_app import app

from werkzeug.utils import secure_filename
import os

from flask_app.models.faults import Fail
from flask_app.models.machines import Machine
from flask_app.models.users import User
from flask_app.models.drawings import Draw
from flask_app.models.prints import Print

@app.route("/new/print", methods = ['POST'])
def newprint():
    if 'user_id' not in session:
        return redirect('/')

    if not Print.valida_print(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/print/'+request.form['User_id'])
    
    print_1 = Print.save(request.form)

    return redirect("/dashboard")

@app.route("/print/<int:id>")
def Tobuy(id):
    
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': id
    }

    formulario1 = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario1)
    design = Draw.show_by_id(formulario)

    return render_template('print.html',user = user, design = design)

@app.route("/carshop")
def Car():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
    
    prints = Print.show_by_id(formulario)


    return render_template("carshop.html", prints = prints)

