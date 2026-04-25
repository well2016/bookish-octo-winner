from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_rota_principal_status_200():
    response = client.get("/")
    assert response.status_code == 200

def test_rota_principal_retorna_mensagem():
    response = client.get("/")
    assert response.json() == {"message": "Hello World"}

def test_rota_teste1_status_200():
    response = client.get("/teste1")
    assert response.status_code == 200

def test_rota_teste1_retorna_json():
    response = client.get("/teste1")
    assert response.json() == {"teste": "deu certo"}

def test_rota_inexistente_status_404():
    response = client.get("/nao-existe")
    assert response.status_code == 404