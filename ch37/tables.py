from db import engine
from sqlalchemy import MetaData,Table,Integer,String,Column,ForeignKey

metadata=MetaData()


#user Table
users=Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(length=5),nullable=False),
    Column("email",String,nullable=False,unique=True),
)


#One TO Many RElation
post=Table(
    "post",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("users",Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False),
    Column("title",String(length=5),nullable=False),
    Column("content",String),
)


#One TO One
profile=Table(
    "profile",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("users",Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,unique=True),
    Column("bio",String(length=5),nullable=False),
    Column("address",String),
)


#Many TO Many
address=Table(
    "address",
    metadata,
    Column("id",Integer,primary_key=True),
    
    Column("Street",String(length=5),nullable=False),
    Column("country",String),
)

user_address_association=Table(
    "user_address_association",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("users",Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True),
    Column("address_id",Integer,ForeignKey("address.id",ondelete="CASCADE"),primary_key=True), 
    
)







#Create Table
def create_table():
    metadata.create_all(engine)
