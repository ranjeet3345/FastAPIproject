from sqlalchemy import text
from db import engine  # assuming engine is defined in db.py

# def raw_sql_query():
#     with engine.connect() as conn:
#         stmt = text("""
#             INSERT INTO users(name, email)
#             VALUES (:name, :email)
#         """)
#         conn.execute(stmt, {"name": "Ranjeet", "email": "Ranjeet@gmail.com"})
#         conn.commit()


def raw_sql_example():
    with engine.connect() as conn:
        stmt = text("""
            SELECT * from users where email=:email
        """)
        res=conn.execute(stmt, { "email": "Ranjeet@gmail.com"}).first()
        return res
