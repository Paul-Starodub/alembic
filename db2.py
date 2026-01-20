from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import (
    registry,
    declarative_base,
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
    relationship,
    Session,
)

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
engine = create_engine(url=DATABASE_URL, echo=True)


mapper_registry = registry()
# print(mapper_registry)
# print(mapper_registry.metadata)

# Base = mapper_registry.generate_base()  # old approach
# Base = declarative_base()


class Base(DeclarativeBase):
    abstract = True

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class User(Base):
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str]
    addresses: Mapped[list["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(name={self.name}, fullname={self.fullname})"


class Address(Base):
    email: Mapped[str] = mapped_column(String(120))
    user_id = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(email={self.email})"


# print(User.__table__.__dict__)
# print(Address.__table__.__dict__)

# user = User(name="jack", fullname="yuigbk", id=1)

with Session(bind=engine) as session:
    with session.begin():
        # Base.metadata.create_all(engine)
        Base.metadata.drop_all(engine)
        # user = User(name="jack", fullname="yuigbk", id=4)
        # session.add(user)
        session.commit()
