from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.conf import settings

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
    settings.database.get("POSTGRES_USER"),
    settings.database.get("POSTGRES_PASSWORD"),
    "db" if settings.DEBUG else settings.database.get("POSTGRES_HOST"),
    settings.database.get("POSTGRES_DB"),
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
