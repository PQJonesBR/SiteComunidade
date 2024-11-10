from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

lista_usuarios = ["Patrick", "João", "Augusto", "Marcelo", "Clarisse"]

# Entrar no temrinal e digitar python, em seguida import secrets
# Criar a chave com o comando secrets.token_hex(16)
app.config['SECRET_KEY'] = 'b1a7a73d7e029b82fe23fe102c56d0c2'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login = form_login, form_criarconta = form_criarconta)

# debug=True -> garante que rode sem precisar pausar e rodar de novo
if __name__ == '__main__':
    app.run(debug=True)