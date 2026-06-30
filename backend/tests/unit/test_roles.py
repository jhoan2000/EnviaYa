from utils.rol import RolUsuario

def test_rol_cliente():
    assert RolUsuario.CLIENTE == "CLIENTE"
def test_rol_domiciliario():
    assert RolUsuario.DOMICILIARIO == "DOMICILIARIO"