from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from .db import db
from .schema import userCreate
app = FastAPI()
db.Base.metadata.create_all(bind = db.engine)

@app.post('/signup', status_code=status.HTTP_201_CREATED, response_model=userCreate)
async def create_user(user:userCreate, db: Session = Depends(db.get_db)):
    pass