from typing import Dict
import yaml
from fastapi.exceptions import HTTPException
from fastapi.applications import Request
from fastapi.routing import APIRouter

import logging

logger = logging.getLogger()


router = APIRouter(
    prefix="/api/validate",
)


@router.post("/")
async def validate(request: Request) -> Dict[str, str]:
    logger.info(f"Validating Yaml from user")
    raw_body = await request.body()
    logger.info(f"{raw_body=}")

    try:
        yaml.load(raw_body, Loader=yaml.Loader)
    except yaml.YAMLError as e:
        raise HTTPException(status_code=422, detail="Invalid YAML")

    return {"detail": "YAML is valid"}
