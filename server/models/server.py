import os
import Pyro5.api
from utils.file_manager import FileManager

@Pyro5.api.expose
class Servidor(object):
    def __init__(self, diretorio):
        self.file_manager = FileManager(diretorio)

    def listar_arquivos(self):
        return self.file_manager.list_files()

    def enviar_arquivo(self, nome_arquivo, conteudo_arquivo):
        return self.file_manager.upload_file(nome_arquivo, conteudo_arquivo)

    def excluir_arquivo(self, nome_arquivo):
        return self.file_manager.delete_file(nome_arquivo)

    def baixar_arquivo(self, nome_arquivo):
        return self.file_manager.download_file(nome_arquivo)
