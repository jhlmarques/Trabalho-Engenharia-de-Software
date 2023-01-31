from flask import Flask, render_template

app = Flask(__name__)

# Adicionar esse decorador em uma função faz com que o flask associe a função abaixo a
# um URL. Ex: URL Padrão
@app.route("/")
def hello_world():
    # render_template renderiza um arquivo html e retorna.
    return render_template('index.html')

if __name__ == "__main__":
    app.run()


