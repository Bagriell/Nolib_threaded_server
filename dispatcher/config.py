import os


class Config:
    """Config for dispatcher server"""

    PROXY_PORT: int = int(os.environ.get("PROXY_PORT", 8000))
    PROXY_HOST: str = os.environ.get("PROXY_HOST", "0.0.0.0")

    SERVER_PORT: int = int(os.environ.get("SERVER_PORT", 2111))
    SERVER_HOST: str = os.environ.get("SERVER_HOST", "0.0.0.0")

cfg = Config()
