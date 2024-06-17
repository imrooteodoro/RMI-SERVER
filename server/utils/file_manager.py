import os

class FileManager:
    def __init__(self, directory):
        self.directory = directory

    def list_files(self):
        return os.listdir(self.directory)

    def upload_file(self, file_name, file_content):
        file_path = os.path.join(self.directory, file_name)
        with open(file_path, 'wb') as file:
            file.write(file_content)
        return "Arquivo enviado com sucesso!"

    def delete_file(self, file_name):
        file_path = os.path.join(self.directory, file_name)
        os.remove(file_path)
        return "Arquivo excluído com sucesso!"

    def download_file(self, file_name):
        file_path = os.path.join(self.directory, file_name)
        if os.path.exists(file_path):
            return file_path
        else:
            return "Arquivo não encontrado!", 404
