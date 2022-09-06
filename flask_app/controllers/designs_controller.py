from flask import render_template, redirect, session, request, flash
from flask_app import app

from werkzeug.utils import secure_filename
import os

from flask_app.models.faults import Fail
from flask_app.models.machines import Machine
from flask_app.models.users import User
from flask_app.models.drawings import Draw
from flask_app.models.likes import Like

@app.route('/newdraw')
def viewForm():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)

    return render_template('newdraw.html', user=user)


@app.route('/new/draw', methods=['POST'])
def savedraw():
    if 'user_id' not in session:
        return redirect('/')
   

    if 'STL' not in request.files:
        flash('STL dont found','draw')
        return redirect('/newdraw')

    STL = request.files['STL']

    if STL.filename == "":
        flash('STL incorrect', 'draw')
        return redirect('/newdraw')
    
    nombre_STL = secure_filename(STL.filename)
    STL.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_STL))


    if 'logo' not in request.files:
        flash('Logo dont found','draw')
        return redirect('/newdraw')

    logo = request.files['logo']

    if logo.filename == "":
        flash('Logo incorrect', 'draw')
        return redirect('/newdraw')
    
    nombre_logo = secure_filename(logo.filename)
    logo.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_logo))

    formulario = {
        'tittle': request.form['tittle'],
        'type': request.form['type'],
        'description': request.form['description'],
        'size': request.form['size'],
        'User_id': request.form['User_id'],
        'logo': nombre_logo,
        'STL': nombre_STL
    }
    
    Draw.save(formulario)

    return redirect('/dashboard')


@app.route('/viewdraw')
def viewForm2():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    desgin = Draw.show(formulario)

    return render_template('viewdraws.html', user=user, design=desgin)

@app.route('/alldesigns')
def print():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    designs = Draw.show_all()

    

    return render_template('viewAllDraws.html', user=user, designs=designs)

@app.route('/delete/design/<int:id>')
def delete_design(id):
    
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    formulario = {'id': id}

    Draw.delete(formulario)
    Draw.delete2(formulario)

    return redirect('/viewdraw')










