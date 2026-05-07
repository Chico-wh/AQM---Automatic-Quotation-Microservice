from sqlalchemy.engine import create_engine
from core.config import settings
from sqlalchemy.orm import DeclarativeBase, sessionmaker
#import da engine do sqlalchemy e do settings do arquivo de configuração. A engine é usada para criar conexões com o banco de dados, e o settings contém a URL do banco de dados que será usada para configurar a engine.
#Delaramos a base

class Base(DeclarativeBase):
    pass
#criamos a engine usando a função create_engine do SQLAlchemy, passando a URL do banco de dados obtida do settings. O parâmetro echo=True é usado para habilitar o log das consultas SQL geradas pela engine, o que pode ser útil para depuração durante o desenvolvimento.



engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)

#criamos uma fábrica de sessões usando a função sessionmaker do SQLAlchemy, configurando-a
from sqlalchemy.orm import sessionmaker

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#A função get_db é um gerador que cria uma nova sessão de banco de dados usando a fábrica de sessões e a retorna. A sessão é fechada automaticamente após o uso, garantindo que os recursos sejam liberados corretamente.

