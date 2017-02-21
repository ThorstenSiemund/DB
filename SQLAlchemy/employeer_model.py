from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    def __repr__(self):
        return '<Department(name="%s")>' % (self.name)


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(20))
    lastname = Column(String(20))
    hired_on = Column(String(10))
    # department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship('Department')

    def __repr__(self):
        return('<Employee(firstname="%s", lastname="%s", hired_on="%s")>' %
               (self.firstname, self.lastname, self.hired_on))
