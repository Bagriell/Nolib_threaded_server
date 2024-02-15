import os


class Config:
    """config for task server"""

    SERVER_PORT: int = int(os.environ.get("SERVER_PORT", 2000))
    SERVER_HOST: str = os.environ.get("SERVER_HOST", "0.0.0.0")

    # smtp config
    SMTP_SENDER_PWD: str = "pppl ipng kqgt euxf"
    SMTP_RECEIVER: str = "gabriel.buetas@gmail.com"
    SMTP_SENDER: str = "gabriel.buetas@gmail.com"


cfg = Config()
