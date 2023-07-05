from flask import Flask, render_template, request, redirect, url_for


from usuarios import Usuario

app=Flask(__name__)

@app.route('/')
def home():
    return redirect("/users")

@app.route('/users')
def mostrar_usuario():
    return render_template("leer.html", usuarios = Usuario.get_all())

@app.route('/user/new')
def new():
    return render_template("crear.html")


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("editar_usuario.html",usuario=Usuario.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("formulario_mostrar_usuario.html",usuario=Usuario.get_one(data))

@app.route('/user/create', methods=['POST'])
def crear_usuario():
    new_user_id = Usuario.save(request.form)
    return redirect(url_for('show', id=new_user_id))

@app.route('/user/update', methods=['POST'])
def update():
    Usuario.update(request.form)
    return redirect('/users')

@app.route ('/user/destroy/<int:id>')
def destroy(id):
    data={
        'id': id
    }
    Usuario.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)
