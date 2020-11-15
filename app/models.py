from . import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    gender = db.Column(db.Boolean)


class School(db.Model):
    __tablename__ = 'school'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    @staticmethod
    def insert_schools():
        names = ['USC', 'GaTech', 'UMD', 'UMich', 'UCSC', 'UCD', 'UTD', 'SCU', 'SJSU', 'UCI', 'VT']
        schools = [ School(name=name) for name in names]
        db.session.bulk_save_objects(schools)
        db.session.commit()
            