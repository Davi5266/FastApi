from fastapi import FastAPI

from db.DB_config import Base
from routers import users
from db.models.User import create_db_and_tables

app = FastAPI()

create_db_and_tables()

# Routes
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    print("ok")
    uvicorn.run("main:app",
        host="localhost", port=8000, reload=True)