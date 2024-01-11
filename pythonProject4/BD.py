from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship, Session

sqlite_database = 'sqlite:///primer5.db'
engine = create_engine(sqlite_database)


class Base(DeclarativeBase): pass


class User(Base):
    __tablename__ = 'users'
    _id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company_id = Column(Integer, ForeignKey('companies._id'))
    company = relationship('Company', back_populates='users')


class Company(Base):
    __tablename__ = 'companies'
    _id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship('User', back_populates='company')


# Base.metadata.create_all(bind=engine)


# with Session(autoflush=False, bind=engine) as db:
#     microsoft = Company(name='Microsoft')
#     google = Company(name='Google')
#     tom = User(name='Tom')
#     bob = User(name='Bob')
#     microsoft.users = [tom]
#     google.users = [bob]
#     db.add_all([microsoft, google])
#     db.commit()
#
#     alice = User(name='Alice')
#     google.users.extend([alice])
#
#     sam = User(name='Sam')
#     sam.company = microsoft
#     db.add(sam)
#     db.commit()

with Session(autoflush=False, bind=engine) as db:
    users = db.query(User).all()
    for u in users:
        print(f'{u.name} ({u.company.name})')


with Session(autoflush=False, bind=engine) as db:
    companies = db.query(Company).all()
    for c in companies:
        print(f'_id = {c._id}, name = {c.name}')
        for u in c.users:
            print(f'_id = {u._id}, name = {u.name}')
        print()







