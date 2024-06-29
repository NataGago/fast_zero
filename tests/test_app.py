from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    """Teste de Retorno"""
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_root_deve_retornar_ok_e_ola_mundo_html(client):
    """Teste de Retorno HTML"""
    response = client.get('/html/')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
    )


def test_create_user(client):
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
