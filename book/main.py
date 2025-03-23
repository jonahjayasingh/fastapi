from fastapi import FastAPI
from routes import book_router


app = FastAPI()


app.include_router(book_router,prefix="/books")
