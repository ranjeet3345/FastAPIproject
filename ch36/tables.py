from db import engine
from sqlalchemy import MetaData,Table,Integer,String,Column

metadata=MetaData()


#user Table
users=Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(length=5),nullable=False),
    Column("email",String,nullable=False,unique=True),
)


#user Table
# users=Table(
#     "users",
#     metadata,
#     Column("id",Integer,primary_key=True),
#     Column("name",String(length=5),nullable=False),
#     Column("email",String,nullable=False,unique=True),
# )



#Create Table
def create_table():
    metadata.create_all(engine)

# drop Table
# def drop_table():
#     metadata.drop_all(engine)