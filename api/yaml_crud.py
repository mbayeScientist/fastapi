import os
import uuid

from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from fastapi.routing import APIRouter


from fastapi import status
import yaml

import logging

logger = logging.getLogger()
router = APIRouter(
    prefix="/api/yaml",
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_yaml(request: Request):
    logger.info(f"creating YAML")
    yaml_uuid = str(uuid.uuid4())
    raw_body = await request.body()
    try:
        loaded_yaml = yaml.load(raw_body, Loader=yaml.Loader)
        with open(f"yaml_db/{yaml_uuid}.yaml", "w") as f:
            yaml.dump(loaded_yaml, f, sort_keys=False, default_flow_style=False)

    except yaml.YAMLError as e:
        raise HTTPException(status_code=422, detail="Invalid YAML")
    return {"detail": "success", "yaml_doc_id": yaml_uuid}


@router.get("/{yaml_doc_id}")
def read_yaml(yaml_doc_id: str):
    dict_with_id = {"id": yaml_doc_id}
    with open(f"yaml_db/{yaml_doc_id}.yaml", "r") as f:
        yaml_data = yaml.load(f, Loader=yaml.loader.Loader)
        returned_doc = {**dict_with_id, **yaml_data}

    return returned_doc


@router.put("/{yaml_doc_id}")
async def update_yaml(yaml_doc_id: str, request: Request):
    raw_body = await request.body()
    try:
        loaded_yaml = yaml.load(raw_body, Loader=yaml.Loader)
    except yaml.YAMLError as e:
        raise HTTPException(status_code=422, detail="Invalid YAML")

    file_path = f"{os.getcwd()}/yaml_db/{yaml_doc_id}.yaml"
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail=f"YAML doc {yaml_doc_id} not found")

    os.remove(file_path)

    with open(f"yaml_db/{yaml_doc_id}.yaml", "w") as f:
        yaml.dump(loaded_yaml, f, sort_keys=False, default_flow_style=False)

    return f"update yaml doc with id {yaml_doc_id}"


@router.delete("/{yaml_doc_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_yaml(yaml_doc_id: str):
    file_path = f"{os.getcwd()}/yaml_db/{yaml_doc_id}.yaml"
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail=f"YAML doc {yaml_doc_id} not found")

    os.remove(file_path)


@router.get("/")
def read_yaml_list():
    logger.info(f"getting all yaml docs from server...")

    loaded_yamls = []
    for root, _, files in os.walk("./yaml_db"):
        for name in files:
            file_path = os.path.join(root, name)
            logger.info(f"{file_path}")
            with open(file_path, "r") as f:
                yaml_data = yaml.load(f, Loader=yaml.loader.Loader)
                if yaml_data:
                    yaml_data["id"] = name.split(".")[0]

            loaded_yamls.append(yaml_data)

    return {"data": loaded_yamls}
