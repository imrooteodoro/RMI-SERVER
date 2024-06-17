from flask import Flask, request, redirect, url_for, render_template
import Pyro5.api

app = Flask(__name__)
file_server = Pyro5.api.Proxy("PYRO:fileserver@localhost:5000")

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_server.upload(file.read(), file.filename)
    return redirect(url_for('list_files'))


@app.route('/files')
def list_files():
    files = file_server.list_files()
    return render_template('index.html', files=files)
