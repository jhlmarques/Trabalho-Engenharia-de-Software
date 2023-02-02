from flask import Flask, render_template, request

app = Flask(__name__)

# Adicionar esse decorador em uma função faz com que o flask associe a função abaixo a
# um URL. Ex: URL Padrão
@app.route("/", methods=["GET", "POST"])
def login():
    # render_template renderiza um arquivo html e retorna.
        return render_template('login.html')

@app.route("/activities", methods=["GET", "POST"])
def activities():
        return render_template('activities.html')

if __name__ == "__main__":
    app.run()
