from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Continuous Integration and Continuous Delivery"
----

16. dentro do diretório /app crie o arquivo requirements.txt
----
flask == 3.1.0
gunicorn == 23.0.0