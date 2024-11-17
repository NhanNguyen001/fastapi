from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from models import *
import models
from database import SessionLocal
from database import engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency injection really just means in programming that we need to do something before we execute
# what we're trying to execute
@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Todos).all()