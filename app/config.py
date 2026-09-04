from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = "NOVA AI STUDIO"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///nova.db"
)
