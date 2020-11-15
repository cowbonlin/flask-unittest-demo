import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.cli.command()
def test():
    print('in test command')
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def create_db(): # with command 'flask create-db'
    print('create db')
    from app import db
    db.create_all()