usuarios = []

def crear_usuario(usuario):
    usuarios.append(usuario)
    return usuario

def login_usuario(correo, password):
    for u in usuarios:
        if u.correo == correo and u.password == password:
            return u
    return None