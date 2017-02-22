from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from employeer_model import Base, Employee, Department
from csv import DictReader
from time import time
from sys import exit
import argparse


def delete_all_tables(session):
    print('deleting table "departments"')
    for department in session.query(Department).all():
        session.delete(department)

    print('deleting table "employees"')
    for employee in session.query(Employee).all():
        session.delete(employee)
    session.commit()


def fill_with_testdata(session):
    '''
    Fills DB with fake departments and employees
    '''
    dict_of_departments = {}

    session.query(Employee).delete()
    session.commit()

    fill_start_tm = time()
    # read all fake names and add them to the DB
    # with open('employee_fakenames.csv', 'r', encoding='utf-8-sig') as csv_file:
    with open('employee_fakenames.csv', 'r') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            if row['Department'] in dict_of_departments:
                dept = dict_of_departments[row['Department']]
            else:
                dept = Department(name=row['Department'])
                dict_of_departments[row['Department']] = dept

            employee = Employee(firstname=row['Firstname'],
                                lastname=row['Lastname'],
                                hired_on=row['Hired'],
                                department=dept,)
            # if session.query(Employee).filter(and_(Employee.firstname == employee.firstname), Employee.lastname == employee.lastname).count() > 0:
            #     print('exists: %s' % employee)
            session.add(dept)
            session.add(employee)
    print('Runtime: ', time() - fill_start_tm)
    commit_start_tm = time()
    session.commit()
    print('Runtime: ', time() - commit_start_tm)



def create_session():
    """
    Creates a sesson object
    @return: session object^
    """
    # Create an engine that stores data
    engine = create_engine('sqlite:///employees.sqlite')

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    # A DBSession() instance establishes all conversations with the database
    # and represents a "staging zone" for all the objects loaded into the
    # database session object. Any change made against the objects in the
    # session won't be persisted into the database until you call
    # session.commit(). If you're not happy about the changes, you can
    # revert all of them back to the last commit by calling
    # session.rollback()
    DBSession = sessionmaker(bind=engine)
    return(DBSession())


def main():
    '''
    Main part of the programm
    '''
    session = create_session()

    # fill db with test data?
    if results.init_db:
        answer = input('If you realy sure to delete the whole DB, type "YES": ')
        if answer == 'YES':
            delete_all_tables(session)
        exit()
        print('-' * 100)
        fill_with_testdata(session)

    print('\nEmployees whose firstnames start with "C":')
    for employee in session.query(Employee).filter(Employee.firstname.startswith("C")):
        print(employee)

    print('\nEmployees whose lastname is "Braun":')
    for employee in session.query(Employee).filter(Employee.lastname == 'Braun'):
        print(employee, employee.department)

    print('\nEmployees whose departement is "Sales":')
    for employee in session.query(Employee).join(Employee.department).filter(Department.name == 'Sales'):
        print(employee, employee.department)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(allow_abbrev=False, description='Program for playing around with Sqlite and SQLAlchemy.')
    parser.add_argument('--init_db', action="store_true", dest='init_db', default=False, help='fill DB with fake employees')
    results = parser.parse_args()
    print(results.init_db)
    main()
