import pytest

from fastapi import HTTPException
from unittest.mock import MagicMock

from utils.validaciones import (
    obtener_usuario,
    obtener_domiciliario,
    validar_perfil_domiciliario,
    obtener_solicitud,
    obtener_oferta
)

# Test obtener usuario
def test_obtener_usuario_correcto():

    db = MagicMock()
    usuario =  object()

    db.query.return_value.filter.return_value.first.return_value  = usuario

    resultado = obtener_usuario(db, 1)

    assert resultado == usuario

def test_obtener_usuario_no_encontrado():

    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as exc:

        obtener_usuario(db, 1)

    assert exc.value.status_code == 404
    assert exc.value.detail == "Usuario no encontrado"

# Test obtener domiciliario
def test_obtener_domiciliario_correcto():
    db = MagicMock()

    domiciliario = object()

    db.query.return_value.filter.return_value.first.return_value = domiciliario

    resultado = obtener_domiciliario(db, 1)

    assert resultado == domiciliario


def test_obtener_domiciliario_no_encontrado():

    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as exc:

        obtener_domiciliario(db, 1)

    assert exc.value.status_code == 404
    assert exc.value.detail == "Domiciliario no encontrado"

# Test Perfil de domiciliario
def test_validar_perfil_domiciliario_correcto():

    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    validar_perfil_domiciliario(db, 1)

def test_validar_perfil_domiciliario_existente():

    db = MagicMock()

    perfil = object()

    db.query.return_value.filter.return_value.first.return_value = perfil

    with pytest.raises(HTTPException) as exc:

        validar_perfil_domiciliario(db, 1)

    assert exc.value.status_code == 400
    assert exc.value.detail == "El usuario ya tiene perfil de domiciliario."

# Test obtener solicitudes
def test_obtener_solicitud_correcto():

    db = MagicMock()

    solicitud = object()

    db.query.return_value.filter.return_value.first.return_value = solicitud

    resultado = obtener_solicitud(db, 1)

    assert resultado == solicitud


def test_obtener_solicitud_no_encontrada():

    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as exc:

        obtener_solicitud(db, 1)

    assert exc.value.status_code == 404
    assert exc.value.detail == "Solicitud no encontrada"

def test_obtener_solicitud_no_encontrada():

    db = MagicMock()

    db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as exc:

        obtener_solicitud(db, 1)

    assert exc.value.status_code == 404
    assert exc.value.detail == "Solicitud no encontrada"

