from dotenv import load_dotenv
from pathlib import Path
import os

BASE_PATH = Path().parent.parent.resolve()

load_dotenv(f"{BASE_PATH}/.env",)

DEBUG = True

database = {
    "POSTGRES_DB": os.getenv('POSTGRES_DB'),
    "POSTGRES_USER": os.getenv("POSTGRES_USER", "root"),
    "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD", "root"),
}
