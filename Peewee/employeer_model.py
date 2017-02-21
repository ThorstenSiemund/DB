from peewee import SqliteDatabase, Model, ForeignKeyField, CharField, DateField


db = SqliteDatabase('employeers.sqlite')


class Department(Model):
    name = CharField()

    class Meta:
        database = db   # This model uses the "db" database.


class Employee(Model):
    firstname = CharField()
    lastname = CharField()
    hired_on = DateField()
    department = ForeignKeyField(Department)

    class Meta:
        database = db   # This model uses the "db" database.
