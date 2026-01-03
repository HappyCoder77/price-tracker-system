import pytest
from fastapi.testclient import TestClient
from api import app, API_KEY

client = TestClient(app)


def test_read_main_success():
    """The root endpoint should be public and return 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"
    assert response.json()["message"] == "Welcome to the Price Tracker API"


def test_get_products_unauthorized():
    """Accessing products without an API Key should return 403."""
    response = client.get("/products")
    assert response.status_code == 403


def test_get_product_authorized():
    """Accessing products with the correct API Key should return 200."""
    headers = {"X-API-KEY": API_KEY}
    response = client.get("/products", headers=headers)
    assert response.status_code == 200
    assert "products" in response.json()


def test_get_deals_unauthorized():
    """Accessing deals without an API Key should return 403."""
    response = client.get("/deals")
    assert response.status_code == 403


def test_get_deals_authorized():
    """Accessing deals with correct API Key should return 200 and success status."""
    headers = {"X-API-KEY": API_KEY}
    response = client.get("/deals", headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    # Ensure 'data' is a list, even if it's empty
    assert isinstance(response.json()["data"], list)


def test_invalid_api_key():
    """Sending a wrong API Key should be blocked with 403."""
    headers = {"X-API-KEY": "wrong_key_123"}
    response = client.get("/products", headers=headers)
    assert response.status_code == 403
    assert "Invalid API Key" in response.json()["detail"]


def test_non_existent_endpoint():
    """Accessing a non-existent route should still return 404."""
    response = client.get("/this-does-not-exist")
    assert response.status_code == 404
