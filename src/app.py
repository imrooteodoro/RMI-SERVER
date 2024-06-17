from flask import Flask, request, render_template
import Pyro5.api

app = Flask(__name__)

def get_servidor():
    uri = "PYRO:obj_9709036ba91a4aa89f0469c5ad3327cd@localhost:36745"  
    return Pyro5.api.Proxy(uri)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/files', methods=['GET'])
def listar_arquivos():
    servidor = get_servidor()
    arquivos = servidor.listar_arquivos()
    return render_template('index.html', arquivos=arquivos)

@app.route('/enviar_arquivo', methods=['POST'])
def enviar_arquivo():
    servidor = get_servidor()
    nome_arquivo = request.form['nome_arquivo']
    conteudo_arquivo = request.files['conteudo_arquivo'].read()
    servidor.enviar_arquivo(nome_arquivo, conteudo_arquivo)
    return "Arquivo enviado com sucesso!"

@app.route('/excluir_arquivo', methods=['POST'])
def excluir_arquivo():
    servidor = get_servidor()
    nome_arquivo = request.form['nome_arquivo']
    servidor.excluir_arquivo(nome_arquivo)
    return "Arquivo excluído com sucesso!"

@app.route('/baixar_arquivo', methods=['GET'])
def baixar_arquivo():
    servidor = get_servidor()
    nome_arquivo = request.args.get('nome_arquivo')
    conteudo_arquivo = servidor.baixar_arquivo(nome_arquivo)
    return conteudo_arquivo

if __name__ == '__main__':
    app.run(debug=True)
