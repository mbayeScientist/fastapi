import pytest


@pytest.fixture
def valid_yaml_doc(request):
    doc_id = request.param
    with open(f"tests_api/valid_yaml_samples/{doc_id}", "rb") as f:
        return f.read()


@pytest.fixture
def non_valid_yaml_doc(request):
    doc_id = request.param
    with open(f"tests_api/non_valid_yaml_samples/{doc_id}", "rb") as f:
        return f.read()
