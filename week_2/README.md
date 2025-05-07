# Banco de Dados com SQLAlchemy + SQLite

- Introdução ao SQLAlchemy
- Sessões de banco (ORM) e criação de tabelas
- CRUD básico com SQLAlchemy
- Integração FastAPI + SQLAlchemy (dependências de sessão)
-  Pydantic + ORM (respostas com orm_mode=True)


O objetivo da semana 2 é a configuração de banco de dados utilizando [SQLAlchemy](https://www.sqlalchemy.org/), esse framework permite criar, atualizar e deletar informações de um banco de dados de modo simples e eficiente.

- ### Crud
CRUD é um acrônimo que representa as quatro operações básicas de persistência em bancos de dados: Create (Criar), Read (Ler), Update (Atualizar) e Delete (Excluir).

###### Registra Usuário no banco de dados
```python
def create_user(db: Session, user_data: CreateUser):
    user = models.User(name = user_data.name, dt_nasc = user_data.dt_nasc, email = user_data.email, tel = user_data.tel)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

```

###### Pega um usuário com base no seu id
```python
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
```


###### Ler todos os usários
```python
def get_users(db: Session):
    return db.query(models.User).all()
```


###### Atualiza usuário no banco de dados
```python
def update_user(db: Session, user_id: int, name: str, dt_nasc: str, email: str, tel:str):
    user = get_user(db, user_id)
    if user:
        user.name = name
        user.dt_nasc = dt_nasc
        user.email = email
        user.tel = tel

    return user
```


###### Deleta usuário do banco de dados
```python
def delete_user(db:Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user

```

