from flask import render_template, redirect, session, request, flash
from flask_app import app

from werkzeug.utils import secure_filename
import os

from flask_app.models.faults import Fail
from flask_app.models.machines import Machine
from flask_app.models.users import User

@app.route('/machine/failure', methods = ['POST'])
def saveFailure():
    if 'user_id' not in session:
        return redirect('/')

    fail = Fail.save(request.form)

    return redirect('/dashboard')

@app.route('/MyRepairs')
def showRepairs():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    foults = Fail.show(formulario)

    return render_template('myrepairs.html', user = user, foults = foults)

@app.route('/delete/repair/<int:id>')
def delete_repair(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    formulario = {"id": id}
    Fail.delete(formulario)

    return redirect('/dashboard')

@app.route('/edit/repair/<int:id>')
def show_edit(id):

    formulario_2 = {"id": id}
    print(id)
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
    fail = Fail.get_by_id(formulario_2)
    user = User.get_by_id(formulario)

    return render_template('machinefailup.html', fail = fail, user = user)

@app.route('/update/repair', methods = ['POST'])
def update():

    if 'user_id' not in session:
        return redirect('/')
    
    if not Fail.valid_repair(request.form): 
        return redirect('/edit/repair/'+request.form['Machine_id'])
    print(request.form)
    Fail.update(request.form)
    return redirect('/dashboard')




    
