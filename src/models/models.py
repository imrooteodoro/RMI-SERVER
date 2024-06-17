import Pyro5.api
from flask import session

def get_servidor():
    uri = session.get('uri')
    return Pyro5.api.Proxy(uri)
