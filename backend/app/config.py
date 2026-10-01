import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

TYPESENSE_HOST = os.getenv("TYPESENSE_HOST")
TYPESENSE_PORT = os.getenv("TYPESENSE_PORT")
TYPESENSE_PROTOCOL = os.getenv("TYPESENSE_PROTOCOL")
TYPESENSE_API_KEY = os.getenv("TYPESENSE_API_KEY")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is not set in the .env file")

if not TYPESENSE_API_KEY:
    raise ValueError("TYPESENSE_API_KEY is not set in the .env file")