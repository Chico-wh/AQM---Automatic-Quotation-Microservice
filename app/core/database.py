from sqlalchemy.engine import create_engine
from core.config import settings
#import da engine do sqlalchemy e do settings do arquivo de configuração. A engine é usada para criar conexões com o banco de dados, e o settings contém a URL do banco de dados que será usada para configurar a engine.

engine = create_engine(settings.DATABASE_URL, echo=True)

#criamos a engine usando a função create_engine do SQLAlchemy, passando a URL do banco de dados obtida do settings. O parâmetro echo=True é usado para habilitar o log das consultas SQL geradas pela engine, o que pode ser útil para depuração durante o desenvolvimento.

from sqlalchemy.orm import sessionmaker
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#criamos uma fábrica de sessões usando a função sessionmaker do SQLAlchemy, configurando-a
session = session_local(engine)
