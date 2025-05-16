# from sqlalchemy import create_engine, URL
# from sqlalchemy.orm import sessionmaker

# USERNAME = "root"
# PASSWORD = "123456789"
# PORT = 3306
# HOST = "127.0.0.1"
# DBNAME = "testepython"
# URL_DB = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(USERNAME, PASSWORD, HOST, PORT, DBNAME)

# print(URL_DB)

# url_object = URL.create(
#     "mysql+pymysql",
#     username=USERNAME,
#     password=PASSWORD,
#     host=HOST,
#     database=DBNAME,
# )



# # engine = create_engine('mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DBNAME')

# # def get_connection():
# #     return create_engine(
# #         url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
# #             USERNAME, PASSWORD, HOST, PORT, DBNAME
# #         )
# #     )

# def get_connection():
#     return create_engine(url_object)
 

# try:
#     engine = get_connection()
#     print(f'Banco de dados conectado!\nuser: {USERNAME}\nhost: {HOST}')
# except Exception as ex:
#     print("Erro ao conectar com o banco de dados!\nInformções do Erro: ", ex)


# # Session = sessionmaker(bind=engine)
# # session = Session()


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Formato da URL:
# mysql+pymysql://usuario:senha@host:porta/nome_do_banco

DATABASE_URL = "mysql+pymysql://root:123456789@127.0.0.1:3306/vamola"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

