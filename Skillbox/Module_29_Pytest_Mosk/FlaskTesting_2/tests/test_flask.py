import json
import pytest



def test_math_route(client) -> None:
    response = client.get('/test_route?number=8')
    data_after_decode = response.data.decode()  # Декодируем ответ
    data = json.loads(data_after_decode)  # Десериализуем данные из JSON в python
    assert data["result"] == 64

def test_user(client) -> None:
    resp = client.get('/users/1')
    assert resp.status_code == 200
    assert resp.json == {"id": 1, "name": "TestBob", "email": "testing@gmail.com"}
    # assert json.loads(resp.data.decode()) == {"id": 1, "name": "TestBob", "email": "testing@gmail.com"}


def test_create_user(client) -> None:
    data = {"name": "TestMan", "email": "testman@gmail.com"}
    resp = client.post('/users', data=data)
    assert resp.status_code == 201


def test_app_config(app):
    assert not app.config["DEBUG"]
    assert app.config['TESTING']
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite://"

def test_render_jinja2(client, captured_templates) -> None:
    route = "/products"
    resp = client.get(route)
    assert resp.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "user_products.html"
    assert context["products"]
    products = context["products"]
    assert products[0]["name"] == "name"

@pytest.mark.parametrize("route", ["/test_route?number=8", "/users/1", "/users", "/products"])
def test_route_status(client, route) -> None:
    rv = client.get(route)
    assert rv.status_code == 200