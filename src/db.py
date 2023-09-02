from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from os import getenv

engine = create_engine(f"postgresql+psycopg2://{getenv('BD_USER')}:{getenv('BD_PASSWORD')}@localhost:5433/postgres")

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    user_id = Column(String(255), unique=True, nullable=False)
