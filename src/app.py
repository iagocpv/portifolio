from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", title="Home", eu = "/static/img/eu.png")

@app.route('/contato')
def contato():
    return render_template("contato.html", title="Contato")

@app.route('/sobre-mim')
def sobreMim():
    return render_template("sobre-mim.html", title="Sobre mim")

@app.route('/projetos')
def projetos():
    projetos = [
        {'nome': 'Covidinho (colaboração)',
          'img': "/static/img/logo.png",
           'desc': 'Plataforma online para visualização de dados sobre a Covid Longa no Vale do Paraíba',
           'site': '#',
           'repo': 'https://github.com/Equipe-01-DSM-2023/API-2023.1',
           'tech': 'Python, Flask, HTML, CSS, Javascript, MySQL', 
         },
    ]
    return render_template("projetos.html", title="Projetos", projetos=projetos)

if __name__ == "__main__":
    app.run(debug=True)