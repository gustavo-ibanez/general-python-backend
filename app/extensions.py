from flask_pymongo import PyMongo
import os

mongo = PyMongo()


def is_running_in_docker():
    # Verifica variáveis de ambiente comuns em Docker
    if os.path.exists("/.dockerenv"):
        return True

    # Verifica o arquivo cgroup
    try:
        with open("/proc/self/cgroup", "r") as f:
            for line in f:
                if "docker" in line:
                    return True
    except FileNotFoundError:
        pass

    return False

def init_extensions(app):

    if is_running_in_docker() :
        print("Inicializando mondoDB por Docker")
        mongo.init_app(app, uri=app.config['MONGO_URI'])
    else:
        print("Inicializando mondoDB Local")
        mongo.init_app(app, uri=app.config['MONGO_URI_LOCAL'])