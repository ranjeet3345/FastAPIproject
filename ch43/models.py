from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import String,Integer
from db import engine

class Base(DeclarativeBase):
    pass

##User MOdel
class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[String]=mapped_column(String(50),nullable=False)
    email:Mapped[str]=mapped_column(String(50),nullable=False,unique=True)


    def __repr__(self)->str:
        return f"<User ({self.id},{self.name},{self.email})> "


def create_tables():
    Base.metadata.create_all(engine)


# def drop_tables():
#     Base.metadata.drop_all(engine)