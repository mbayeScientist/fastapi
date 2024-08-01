from fastapi.testclient import TestClient
import pytest
from app import app as fastapi_app
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
client = TestClient(fastapi_app)

valid_inline_yamls = ["a:b", "a:2", "-----", "a:a:{a:{1,2,3}}"]
API = "/api"


@pytest.mark.parametrize("valid_yaml_content", valid_inline_yamls)
def test_valid_inline_yamls(valid_yaml_content) -> None:
    response = client.post(f"{API}/validate", content=valid_yaml_content)
    assert response.status_code == 200
    assert response.json() == {"detail": "YAML is valid"}


not_valid_inline_yamls = ["{"]


@pytest.mark.parametrize("not_yaml_content", not_valid_inline_yamls)
def test_none_valid_inline_yamls(not_yaml_content) -> None:
    response = client.post(f"{API}/validate", content=not_yaml_content)
    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid YAML"}


@pytest.mark.parametrize(
    "valid_yaml_doc", ["eden.yaml"], indirect=True, ids=["eden.yaml"]
)
def test_valid_samples(valid_yaml_doc):
    response = client.post(f"{API}/validate", data=valid_yaml_doc)
    assert response.status_code == 200
    assert response.json() == {"detail": "YAML is valid"}


@pytest.mark.parametrize(
    "non_valid_yaml_doc", ["non_valid1.yaml"], indirect=True, ids=["non_valid1.yaml"]
)
def test_non_valid_samples(non_valid_yaml_doc):
    response = client.post(f"{API}/validate", data=non_valid_yaml_doc)
    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid YAML"}
