import Pyro5.api
from models.server import Servidor

def main():
    servidor = Servidor('/home/teodoro/Documents/Sistemas Distribuidos/RMI-SERVER/RMI-SERVER/server/arquivos')
    daemon = Pyro5.api.Daemon()                
    uri = daemon.register(servidor)   
    print("Pronto. O URI do objeto é: {0}".format(uri))
    daemon.requestLoop()

if __name__ == '__main__':
    main()
