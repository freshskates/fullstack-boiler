import os
from typing import Any, Dict
from dotenv import load_dotenv

load_dotenv()

def get_env_or_default(key: str, default: Any) -> Any:
    value = os.getenv(key, default)
    return value 

config_map: Dict[str, str | int] = {
    "JWT_SECRET_KEY": get_env_or_default("JWT_SECRET_KEY", "fake-super-secret-key"),
    "DEBUG": get_env_or_default("DEBUG", False),  
    "DATABASE_URL": get_env_or_default("DATABASE_URL", "sqlite:///./test.db"),
    "JWT_ALGORITHM": get_env_or_default("JWT_ALGORITHM", "HS256"),
    "TOKEN_EXPIRE_MINUTES": get_env_or_default("TOKEN_EXPIRE_MINUTES", 30),  
}

class Config:
    def __getattr__(self, name: str) -> Any:
        if name in config_map:
            return config_map[name]
        raise AttributeError(f"Configuration '{name}' not found")

config = Config()
