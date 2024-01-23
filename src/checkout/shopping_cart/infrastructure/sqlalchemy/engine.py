from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://mercaclean:mercaclean@database:3306/mercaclean')

create_session = sessionmaker(bind=engine)
