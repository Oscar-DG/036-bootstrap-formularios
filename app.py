from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Proyecto Semana 8 funcionando"


if __name__ == "__main__":
    app.run(debug=True)