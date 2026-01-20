# working with core
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
engine = create_engine(url=DATABASE_URL, echo=True)

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, unique=True, autoincrement=True),
    Column("fullname", String),
    Column("name", String(30)),
)

address_table = Table(
    "addresses",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("user_id", ForeignKey("users.id")),
    Column("email_address", String(30)),
)

metadata.create_all(engine)

stmt = insert(user_table).values(name="John Doe", fullname="John Doe")
# print(stmt)
