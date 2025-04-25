from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Books(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    autor: str #= Field(index=True)
    dtpubli: str #= Field(index=True)
    genero: str
    desc: str
    images: str
    # age: int | None = Field(default=None, index=True)
    # secret_name: str


sqlite_file_name = "books.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/book/")
def create_book(book: Books, session: SessionDep) -> Books:
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@app.get("/book/")
def read_book(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Books]:
    heroes = session.exec(select(Books).offset(offset).limit(limit)).all()
    return heroes


@app.get("/book/{book_id}")
def read_hero(book_id: int, session: SessionDep) -> Books:
    book = session.get(Books, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.delete("/book/{book_id}")
def delete_hero(book_id: int, session: SessionDep):
    book = session.get(Hero, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return {"ok": True}
