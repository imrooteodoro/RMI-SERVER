from flask import Flask, request
from routes import pyroRoute
from models import pyro5
from controllers import pyroControl



app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Está funcionando"



if __name__ == '__main__':
    app.run(debug=True)

