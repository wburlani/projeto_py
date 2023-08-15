from flask import Flask, render_template, request, redirect, session, jsonify
import os
import json
import subprocess
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/converter', methods=['POST'])
def converter():
    try:
        script_path = r'C:/workspace/projeto_py/scripts/convertFiles.py'  # Substitua pelo caminho absoluto completo
        if os.path.exists(script_path):
            os.system(f'python {script_path}')
            return 'Conversão para PDF realizada com sucesso!'
        else:
            return 'Script não encontrado'
    except Exception as e:
        return f'Ocorreu um erro ao converter para PDF: {str(e)}'


@app.route('/listar_nomes_dir')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if not username or not password or not email:
            return "All fields are required"

        users = read_users()
        if username in users:
            return "Username already exists"

        users[username] = {'password': password, 'email': email}
        write_users(users)
        return "Registration successful! You can now log in."

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = read_users()
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect('/dashboard')
        else:
            return "Invalid username or password"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove o nome de usuário da sessão
    return redirect('/login')  # Redireciona para a página de login após encerrar a sessão

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

def read_users():
    data_path = os.path.join(os.path.dirname(__file__), 'data/users.json')
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    else:
        return {}

def write_users(users):
    data_path = os.path.join(os.path.dirname(__file__), 'data/users.json')
    try:
        with open(data_path, 'w') as f:
            json.dump(users, f)
    except Exception as e:
        print("Error writing users:", e)





