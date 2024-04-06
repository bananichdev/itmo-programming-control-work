import os

from dotenv import load_dotenv

load_dotenv()

DB_DRIVER = "postgresql"
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")

DB_FULL_URL = f"{DB_DRIVER}+asyncpg://{DB_USER}:{DB_PASS}@{DB_URL}/{DB_NAME}"
