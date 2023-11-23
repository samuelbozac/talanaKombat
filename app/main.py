from fastapi import FastAPI

from app.combat.router import router
from app.combat import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
