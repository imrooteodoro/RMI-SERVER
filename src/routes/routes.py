from flask import request, render_template, url_for, send_file, session, redirect
from models.models import get_servidor
import os

def setup_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/files', methods=['GET'])
    def listar_arquivos():
        servidor = get_servidor()
        arquivos = servidor.listar_arquivos()
        arquivos_com_links = {arquivo: url_for('baixar_arquivo', nome_arquivo=arquivo) for arquivo in arquivos}
        return render_template('index.html', arquivos=arquivos_com_links)

    @app.route('/upload', methods=['POST'])
    def enviar_arquivo():
        servidor = get_servidor()
        nome_arquivo = request.form['nome_arquivo']
        conteudo_arquivo = request.files['conteudo_arquivo'].read()
        servidor.enviar_arquivo(nome_arquivo, conteudo_arquivo)
        return "Arquivo enviado com sucesso!"

    @app.route('/delete', methods=['POST'])
    def excluir_arquivo():
        servidor = get_servidor()
        nome_arquivo = request.form['nome_arquivo']
        servidor.excluir_arquivo(nome_arquivo)
        return "Arquivo excluído com sucesso!"

    @app.route('/download', methods=['GET'])
    def baixar_arquivo():
        servidor = get_servidor()
        nome_arquivo = request.args.get('nome_arquivo')
        path_arquivo = servidor.baixar_arquivo(nome_arquivo)

        if os.path.exists(path_arquivo):
            return send_file(path_arquivo, as_attachment=True)
        else:
            return "Arquivo não encontrado!", 404

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['uri'] = request.form['uri']
            return redirect(url_for('listar_arquivos'))
        return render_template('login.html')
