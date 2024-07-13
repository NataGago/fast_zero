from http import HTTPStatus

from fastapi.testclient import TestClient


def test_root_deve_retornar_ok_e_ola_mundo(client: TestClient):
    """Teste de Retorno"""
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_root_deve_retornar_ok_e_ola_mundo_html(client: TestClient):
    """Teste de Retorno HTML"""
    response = client.get('/html/')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
    )


def test_create_user(client: TestClient):
    """post - criação de usuário"""
    response = client.post(
        '/users/',
        json={
            'username': 'nata',
            'email': 'nata@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'nata',
        'email': 'nata@example.com',
        'id': 1,
    }


def test_read_users(client: TestClient):
    """Teste de listar usuários"""
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'nata',
                'email': 'nata@example.com',
                'id': 1,
            }
        ]
    }


def test_get_user(client: TestClient):
    """Retorna um usuário"""
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'nata',
        'email': 'nata@example.com',
        'id': 1,
    }


def test_get_user_fail(client: TestClient):
    """Retorna um usuário"""
    response = client.get('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client: TestClient):
    """Teste de atualizar um usuário"""
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_fail(client: TestClient):
    """Testa quando um usuário não é atualizado corretamente"""
    response = client.put(
        '/users/0',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client: TestClient):
    """Testa a deleção de um usuário"""
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_fail(client: TestClient):
    """Testa quando um usuário não pôde ser deletado"""
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
