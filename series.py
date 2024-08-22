from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_series = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        ano = request.form['ano']
        descricao = request.form['descricao']

        serie = len(lista_series) + 1
        lista_series.append({"serie": serie, "titulo": titulo, "genero": genero, "ano": ano, "descricao": descricao})

        return redirect(url_for('index'))

    return render_template('index.html', series=lista_series)

if __name__ == '__main__':
    app.run(debug=True)

