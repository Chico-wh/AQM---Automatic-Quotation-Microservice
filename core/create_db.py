from core.database import Base, engine

# IMPORTANTE:
# Esse import faz o SQLAlchemy registrar o model User no Base.metadata.
# Sem isso, nenhuma tabela é criada.
from models.user import User
from models.customers import Customer
from models.services import Services
from models.quote import Quote
from models.pricing_rule import Rule


def create_tables():
    """
    Cria todas as tabelas registradas no Base.metadata.

    Se Base.metadata estiver vazio, o SQLAlchemy não cria nada.
    """

    print("Tabelas registradas:")
    print(Base.metadata.tables.keys())

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tabelas criadas com sucesso.")