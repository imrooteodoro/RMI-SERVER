import socket
import Pyro5.api
from models.server import Servidor

def get_private_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '0.0.0.0'
    finally:
        s.close()
    return IP

import time

def main():
    # Delay to allow container network setup
    time.sleep(5)

    servidor = Servidor('/app/server/arquivos')
    daemon = Pyro5.api.Daemon(host=get_private_ip_address())                
    uri = daemon.register(servidor, objectId="obj_188645a453a54bbc81948816e3d3edba")   
    print("Pronto. O URI do objeto é: {0}".format(uri))
    daemon.requestLoop()

if __name__ == '__main__':
    main()
