# working with metadata

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
engine = create_engine(url=DATABASE_URL, echo=True)

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String(50)),
)

address_table = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("email_address", String, nullable=False),
)

# print(user_table.c.keys())
# print(address_table.c.keys())

metadata.create_all(engine)
metadata.drop_all(engine)
