# **Gerando token de autenticação com JWT, e criptografando senhas digitadas pelo usuário utilizando passlib**

```python
from passlib.context import CryptContext
```

```python
@app.post("/login", response_model=Token)

async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


```