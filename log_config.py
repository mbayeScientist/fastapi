from pydantic import BaseModel
from typing import ClassVar, Dict, Any

class LogConfig(BaseModel):
    """Configuration de la journalisation pour le serveur"""

    LOGGER_NAME: str = "YamlHouse"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Configuration de la journalisation
    version: ClassVar[int] = 1
    disable_existing_loggers: ClassVar[bool] = False
    formatters: ClassVar[Dict[str, Dict[str, Any]]] = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: ClassVar[Dict[str, Dict[str, Any]]] = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: ClassVar[Dict[str, Dict[str, Any]]] = {
        "YamlHouse": {"handlers": ["default"], "level": LOG_LEVEL},
    }

    def to_dict(self) -> Dict[str, Any]:
        # Convertir les champs d'instance en dictionnaire
        config_dict = self.dict()
        # Ajouter les variables de classe
        config_dict.update({
            "version": self.version,
            "disable_existing_loggers": self.disable_existing_loggers,
            "formatters": self.formatters,
            "handlers": self.handlers,
            "loggers": self.loggers,
        })
        return config_dict
