from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

sqlite_database = "sqlite:///primer.db"
engine = create_engine(sqlite_database, echo=True)


class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    # добавляем два объекта
    bob = Person(name="Bob", age=42)
    sam = Person(name="Sam", age=25)
    db.add(bob)
    db.add(sam)
    db.commit()

    alice = Person(name="Alice", age=33)
    kate = Person(name="Kate", age=28)
    db.add_all([alice, kate])
    db.commit()

