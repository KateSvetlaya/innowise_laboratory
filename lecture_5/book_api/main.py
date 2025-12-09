from fastapi import FastAPI
from . import models
from . database import engine
from . import books

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["books"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API!"}