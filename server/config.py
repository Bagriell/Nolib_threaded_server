import os


class Config:
    """config for task server"""

    SERVER_PORT: int = int(os.environ.get("SERVER_PORT", 2111))
    SERVER_HOST: str = os.environ.get("SERVER_HOST", "localhost")

    # smtp config
    SMTP_SENDER_PWD: str = "secret"
    SMTP_RECEIVER: str = "secret"
    SMTP_SENDER: str = "secret"


cfg = Config()
