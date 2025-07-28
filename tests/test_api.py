import pytest


def test_openapi_spec(client):
    """GET /openapi.yaml returns the OpenAPI document."""
    resp = client.get("/openapi.yaml")
    assert resp.status_code == 200
    text = resp.get_data(as_text=True)
    assert "openapi:" in text
    assert "paths:" in text


def test_swagger_ui_redirect(client):
    """GET /docs serves the Swagger UI HTML."""
    resp = client.get("/docs")
    # Flask-Swagger-UI serves an HTML page with a <title> tag
    assert resp.status_code == 200
    html = resp.get_data(as_text=True)
    assert "<html" in html.lower()
    assert "swagger-ui" in html.lower()


def test_health_endpoint(client):
    """If you add a health endpoint, test it here. e.g. GET /healthz."""
    # Assuming you implement /healthz returning {"status":"ok"}:
    resp = client.get("/healthz")
    if resp.status_code == 404:
        pytest.skip("Health endpoint not implemented")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get("status") == "ok"
