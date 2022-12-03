import uvicorn
import yaml
from fastapi.applications import FastAPI
from starlette.responses import RedirectResponse

from api import yaml_crud, validate

app = FastAPI(openapi_url="/static/swagger.yaml")

from logging.config import dictConfig
import logging
from log_config import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("YamlHouse")


def custom_openapi():
    with open("static/swagger.yaml", "r") as myfile:
        data = myfile.read()
    app.openapi_schema = yaml.load(data, Loader=yaml.Loader)
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(yaml_crud.router)
app.include_router(validate.router)


@app.get("/")
async def redirect():
    response = RedirectResponse(url="/docs")
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
