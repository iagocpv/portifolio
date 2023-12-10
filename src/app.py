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
        {
            'nome': 'API 1',
            'img': "/static/img/virus.png",
            'desc': 'Projeto desenvolvido para a API (Aprendizagem por Projeto Integrado) do 1° semestre de Desenvolvimento de Software Multiplataforma (DSM) em parceria com a Vanguarda sobre dados relacionados à covid longa no Vale do Paraíba para um site de uso jornalístico. Contribuí principalmente na parte de tratamento dos dados dos arquivos csv e geração de gráficos, entre outras coisas.',
            'repo': 'https://github.com/Equipe-01-DSM-2023/API-2023.1',
            'tech': 'Python, Flask, HTML, CSS, Javascript, MySQL'
        },
        {
            'nome': 'API 2',
            'img': "/static/img/callnet.png",
            'desc': 'O sistema desenvolvido, chamado CallNet, é focado em fornecer auxílio aos problemas relacionados a Internet Fixa, e busca aprimorar o sistema de Gerenciamento de Chamadas de Serviço. Contribuí principalmente na geração das listas de chamados e mensagens no front, e no back na parte do banco de dados e geração de relatórios',
            'repo': 'https://github.com/Equipe-CodeLand/API-2023.2',
            'tech': 'Typescript, React, HTML, CSS, Node, Express, MySQL, TypeORM'
        },
        {
            'nome': 'Portfolio',
            'img': "/static/img/port.png",
            'desc': 'Repositório com o código do meu portfolio, desenvolvido na matéria de Design Digital',
            'repo': 'https://github.com/iagocpv/portifolio',
            'tech': 'Python, Flask, HTML, CSS'
        },
    ]
    return render_template("projetos.html", title="Projetos", projetos=projetos)

if __name__ == "__main__":
    app.run(debug=True)