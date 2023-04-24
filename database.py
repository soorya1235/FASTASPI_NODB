from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://admin:tiger@localhost/item",echo=True)
sessionLocal = sessionmaker(bind=engine)
