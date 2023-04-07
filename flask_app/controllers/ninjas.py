from flask import redirect,session,render_template,request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas_index():
    dojos = Dojo.show_all()
    return render_template('show_ninja.html', dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def ninjas_create():
    # print(request.form)
    ninja = Ninja.create(request.form)
    return redirect('/dojos')

@app.route('/ninjas/delete/<int:id>/<int:dojo_id>')
def ninjas_delete(id, dojo_id):
    Ninja.delete(id)
    return redirect('/dojos/show/' + str(dojo_id))

@app.route('/ninjas/update/<int:id>/<int:dojo_id>')
def ninjas_update(id,dojo_id):
    ninja = Ninja.ninja_show_one(id)
    return render_template('edit.html', ninja=ninja, dojo_id=dojo_id)

@app.route('/ninjas/send/<int:dojo_id>', methods=['POST'])
def send(dojo_id):
    Ninja.update(request.form)
    return redirect('/dojos/show/' + str(dojo_id))