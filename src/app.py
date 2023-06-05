from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", title="Home")

@app.route('/contato')
def contato():
    return render_template("contato.html", title="Contato")

@app.route('/sobre-mim')
def sobreMim():
    return render_template("sobre-mim.html", title="Sobre mim")

@app.route('/projetos')
def projetos():
    projetos = ['Projeto 1', 'Projeto 2']
    return render_template("projetos.html", title="Projetos", projetos = projetos)

if __name__ == "__main__":
    app.run(debug=True)