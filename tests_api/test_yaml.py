from fastapi.testclient import TestClient
import pytest
import app

client = TestClient(app.app)

valid_inline_yamls = ["a:b", "a:2", "-----", "a:a:{a:{1,2,3}}"]


@pytest.mark.parametrize("valid_yaml_content", valid_inline_yamls)
def test_valid_inline_yamls(valid_yaml_content) -> None:
    response = client.post("/validate", content=valid_yaml_content)
    assert response.status_code == 200
    assert response.json() == {"detail": "YAML is valid"}


not_valid_inline_yamls = ["{"]


@pytest.mark.parametrize("not_yaml_content", not_valid_inline_yamls)
def test_none_valid_inline_yamls(not_yaml_content) -> None:
    response = client.post("/validate", content=not_yaml_content)
    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid YAML"}
