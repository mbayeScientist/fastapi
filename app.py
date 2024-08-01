from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from logging.config import dictConfig
import logging
import yaml
from api.yaml_crud import router as yaml_crud_router
from api.validate import router as validate_router
from log_config import LogConfig
import uvicorn
# Initialisation de l'application FastAPI avec l'URL de l'OpenAPI
app = FastAPI(openapi_url="/static/swagger.yaml")

# Configurer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurer la journalisation
dictConfig(LogConfig().to_dict())
logger = logging.getLogger("YamlHouse")

# Fonction personnalisée pour charger le schéma OpenAPI à partir d'un fichier YAML
def custom_openapi():
    with open("static/swagger.yaml", "r") as myfile:
        data = myfile.read()
    app.openapi_schema = yaml.load(data, Loader=yaml.Loader)
    return app.openapi_schema

app.openapi = custom_openapi

# Inclure les routers pour les différentes routes de l'application
app.include_router(validate_router)
app.include_router(yaml_crud_router)

# Configurer FastAPI pour servir les fichiers statiques
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route de redirection vers la documentation de l'API
@app.get("/")
async def redirect():
    response = RedirectResponse(url="/static/index.html")
    return response

# Démarrer l'application avec Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
