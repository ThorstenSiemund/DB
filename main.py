from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from db_declarations import Base, Person
from csv import DictReader
import getopt
import sys
from time import time


def init(session):
    """ Initialize  the DB. The means delete all persons and fill the DB
    with fake names which are found in a cvs-file.
    If a person with the same name (firstname, lastname) wil be inserted in
    th DB, a printout is done.
    """
    # delete all persons
    session.query(Person).delete()
    session.commit()

    start = time()
    # read all fake names and add them to the DB
    with open('fakename.csv', 'r', encoding='utf-8-sig') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            person = Person(firstname=row['Vorname'],
                            lastname=row['Nachname'],
                            street=row['Strasse'],
                            city=row['Stadt'],
                            zip_code=row['PLZ'],
                            email_address=row['EmailAdresse'],)
            if session.query(Person).filter(and_(Person.firstname == person.firstname), Person.lastname == person.lastname).count() > 0:
                print('exists: ' + person.firstname + ' ' + person.lastname)
            session.add(person)
    print('Runtime: ', time() - start)
    session.commit()


def search_firstname(session, fname):
    """
    Query for looking for person with a specific firstname
    @session:   session object
    @fname:     firstname
    """
    q = session.query(Person).filter(Person.firstname == fname)
    for person in q:
        print(person.lastname + ', ' + person.firstname)
    print(str(q.count()) + ' persons found with firstname ' + fname)
    pass


def create_session():
    """
    Creates a sesson object
    @return: session object
    """
    # Create an engine that stores data
    engine = create_engine('sqlite:///persons.sqlite')

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


def main(argv):
    """ Main program
    """
    session = create_session()
    try:
        opts, args = getopt.getopt(argv, 'h', ['initdb'])
    except getopt.GetoptError:
        print('unknown option')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('\nUsage: main.py [--initdb]')
            print('The optinal paramster --initdb drops all atbles and fill DB with fake names')
            sys.exit()
        elif opt in ('', '--initdb'):
            print('initdb')
            answer = input('If you realy sure to delete the whole DB, type "YES": ')
            if answer == 'YES':
                init(session)

    search_firstname(session, 'Tim')


if __name__ == '__main__':
    main(sys.argv[1:])
