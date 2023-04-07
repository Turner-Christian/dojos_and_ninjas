from flask import redirect,session,render_template,request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def index():
    dojos = Dojo.show_all()
    return render_template('index.html', dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    dojo = Dojo.create_dojo(request.form)
    print(dojo)
    return redirect('/dojos')

@app.route('/dojos/show/<int:id>')
def show(id):
    dojo = Dojo.show_one(id)
    ninjas = Dojo.get_ninjas(id)
    return render_template('show_dojo.html', ninjas=ninjas, dojo=dojo)
