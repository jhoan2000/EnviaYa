domiciliarios = []

def crear_domiciliario(domiciliario):
    domiciliarios.append(domiciliario)
    return domiciliario


def login_usuario(correo, password):
    for d in domiciliarios:
        if d.correo == correo and d.password == password:
            return d
    return None
