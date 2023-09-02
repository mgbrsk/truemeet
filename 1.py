# from sqlalchemy import insert
# from sqlalchemy import create_engine, ForeignKey
# from sqlalchemy import Column, Date, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

# engine = create_engine('sqlite:///truemeet.sqlite', echo=True)
# conn = engine.connect()
# Base = declarative_base()


# class Truemeet(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    
#     def __init__(self, name):
#         self.name = name


# Base.metadata.create_all(engine)

# query = insert(Truemeet).values(name='Matthew', Pass=True)
# Result = conn.execute(query)

# output = conn.execute(Truemeet.select()).fetchall()
# print(output)

engine = db.create_engine('sqlite:///datacamp.sqlite')
conn = engine.connect()
metadata = db.MetaData()

Student = db.Table('Student', metadata,
              db.Column('Id', db.Integer(),primary_key=True),
              db.Column('Name', db.String(255), nullable=False),
              db.Column('Major', db.String(255), default="Math"),
              db.Column('Pass', db.Boolean(), default=True)
              )

# metadata.create_all(engine)
query = db.insert(Student).values(Id=1, Name='Matthew', Major="English", Pass=True)
query2 = db.insert(Student).values(Id=2, Name='aefaf', Major="Englaefaefish", Pass=True)

Result = conn.execute((query))
# Result = conn.execute((query2))

output = conn.execute(Student.select()).fetchall()
print(output)


