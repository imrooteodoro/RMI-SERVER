from flask import Flask
from routes.routes import setup_routes

app = Flask(__name__)
app.secret_key = '3333' 

setup_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
