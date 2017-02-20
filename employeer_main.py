from employeer_model import db, Employee, Department
from peewee import OperationalError
from csv import DictReader
from time import time


def fill_with_testdata():
    '''
    Fills DB with fake departments and employees
    '''
    dict_of_departments = {}

    start = time()

    # read all fake names and add them to the DB
    with open('employee_fake_names.csv', 'r') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            # print(row)
            with db.transaction():
                # department already exists?
                if row['Department'] in dict_of_departments:
                    dept = dict_of_departments[row['Department']]
                else:
                    dept = Department(name=row['Department'])
                    dept.save()
                    dict_of_departments[row['Department']] = dept

                employee = Employee(firstname=row['Firstname'],
                                    lastname=row['Lastname'],
                                    hired_on=row['Hired'],
                                    department=dept)
                employee.save()
    print('Runtime: ', time() - start)
    db.commit()


def main():
    '''
    Main part of the programm
    '''
    db.connect
    # db.create_tables([Employee, Department])
    try:
        Employee.create_table()
    except OperationalError:
        print('"Employee" table already exists!')

    try:
        Department.create_table()
    except OperationalError:
        print('"Department" table already exists!')

    fill_with_testdata()


if __name__ == '__main__':
    main()
