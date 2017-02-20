from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    street = Column(String(250), nullable=False)    # include house number
    city = Column(String(250), nullable=False)
    zip_code = Column(Integer, nullable=False)
    email_address = Column(String(250), nullable=False)
