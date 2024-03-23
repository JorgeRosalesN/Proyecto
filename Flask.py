# Funcionamiento pagina Web
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de usuario
usuario_valido = "admin"
contraseña_valida = "Inteia"


@app.route('/')
def inicio():
    return render_template('inicio.html')

# Inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    if usuario == usuario_valido and contraseña == contraseña_valida:
        # Credenciales válidas
        return redirect(url_for('cuerpo'))
    else:
        # Credenciales no válidas
        return redirect(url_for('inicio'))

# Acceso correcto
@app.route('/cuerpo')
def cuerpo():
    return render_template('cuerpo.html')

if __name__ == '__main__':
    app.run(debug=True)