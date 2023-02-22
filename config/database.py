import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # para manipular las tablas en las bases de datos

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__)) # Leer directorio .path

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" # Conecto la base de datos con la url

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

