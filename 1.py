# import sqlalchemy as db

# engine = db.create_engine('sqlite:///truemeet.sqlite')
# conn = engine.connect()
# metadata = db.MetaData()

# Student = db.Table('Student', metadata,
#               db.Column('id', db.Integer(), primary_key=True),
#               db.Column('Name', db.String(255), nullable=False),
#               )

# # metadata.create_all(engine)
# # query = db.insert(Student).values(Id=1, Name='Matthew', Major="English", Pass=True)
# query2 = db.insert(Student).values(Id=2, Name='aefaf', Major="Englaefaefish", Pass=True)

# # conn.execute((query2))
# # conn.commit()
# # # Result = conn.execute((query2))

# output = conn.execute(Student.select()).fetchall()
# print(output)
