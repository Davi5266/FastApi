from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import crud
from database import get_db

# criando um contexto de hashing de senhas usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Recebe uma senha digitada pelo usuário e a criptografa
def hash_password(password:str) -> str:
    return pwd_context.hash(password)
# Realiza uma comparação entre a senha digitada com a senha registrada no sistema
def verify_password(plain_password: str, hashed_password:str) -> bool:
    # A senha digitada é criptografada e o seu hash é comparado com o hash no sistema
    return pwd_context.verify(plain_password, hashed_password)

# Configurando o JWT(Json web token)
SECRET_KEY = "SENHASECRETA" # chave usada para assinar o JWT, garantindo que ninguém possa forjar tokens sem conhecê-la. Essa chave é utilizada para gerar quanto para verificar o token

ALGORITHM = "HS256" # algoritmo usado para assinar o JWT. HMAC usando SHA-256
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # tempo de vida do token gerado 

# a função create_access_token gera um token com base em dois parêmtros, data que armazena infomações do usuário, e o expires_delta que define um tempo de expiração opcional
def create_access_token(data:dict, expires_delta:timedelta | None = None):
    to_encode = data.copy() # cópia dos dados gerados pelo usuário
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15)) # Define o tempo de vida do JWT, se o expires_delta for None(vazio) o tempo padrão vai ser de 15 minutos 
    to_encode.update({"exp":expire}) # passa o tempo de expiração do JWT como parâmetro do dicionario data
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # codifica o token JWT com algoritmo HS256 e uma chave secreta
    return encoded_jwt 

# Verificador de token
def verify_token(token: str):

    # Recebe o token do usuário como parâmetro, e tenta decodificar caso de error a função entra na exceção JWTError e retorna vazio(None)
    try:
        # Decodificando o token atribuido e utilizando como parâmetro a chave secreta(SECRET_KEY) e o algoritmo(ALGORITHM) 
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

# CONFIGURÇÃO DE ROTAS AUTENTICADAS COM TOKEN
# Essa configuração permite que apenas usuários autenticados tenham acessos a determinadas rotas privadas

# Dependencia que extrai o token JWT do cabeçalho {Authorization: Bearer <token>}, e o parâmetro tokenUrl passa o endpoint reponsavel por fornecer o token, através de uma rota POST /login que passa um body com username e password (no caso desse código ele passa um body com email e password)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Recebe o JWT extraido do oauth2_scheme, através de uma dependencia(Depends) que tem como parâmetro o oauth2_scheme que retorna o token extraido da requisição 
def get_current_user(token:str = Depends(oauth2_scheme), db:Session = Depends(get_db)):

    # Resposta para tratar errors de autorização de rota
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate":"Bearer"},
    )

    try:
        # extraindo credenciais do token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # pegando o parâmetro email extraido do token
        email: str = payload.get("sub")
        # Se o email não existe retorna um erro de credenciais
        if email is None:
            raise credentials_exception
    except JWTError: # Se ouver algum erro durante a extração das credenciais do token entra em uma exceção JWTError e retorna um erro de credencias
        raise credentials_exception

    # Realiza uma comparação do email extraido do token com o email do banco de dados
    user = crud.get_user_by_email(db, email)
    # Se o email não existe, retorna um erro de credenciais
    if user is None:
        raise credentials_exception
    
    # Se o usuário extraido do token está cadastrado no banco de dados, retorna o usuário 
    return user