from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from checkout.shopping_cart.infrastructure.sqlalchemy.entity.base import Base


def database_bootstrap() -> Session:
    engine = create_engine('mysql+pymysql://mercaclean:mercaclean@database:3306/mercaclean')
    Base.metadata.create_all(bind=engine)
    create_session = sessionmaker(bind=engine)
    return create_session()
