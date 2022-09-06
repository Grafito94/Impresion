from flask import render_template, redirect, session, request, flash
from flask_app import app

from werkzeug.utils import secure_filename
import os

from flask_app.models.faults import Fail
from flask_app.models.machines import Machine
from flask_app.models.users import User
from flask_app.models.drawings import Draw
from flask_app.models.likes import Like


@app.route('/like', methods = ['POST'])
def like():
    if 'user_id' not in session:
        return redirect('/')

    formulario1 = {
        'Drawing_id' : request.form['Drawing_id'],
        'User_id': request.form['User_id']
    }

    like = Like.save(formulario1)
    
    return redirect('/alldesigns')



