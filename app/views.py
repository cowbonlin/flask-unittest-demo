from flask import Blueprint, jsonify

from . import db
from .models import Student

api_bp = Blueprint('api', __name__)

@api_bp.route('/helloword')
def helloword():
    return 'greeting from cowbon'


@api_bp.route('/student', methods=['POST'])
def add_student():
    student = Student(name='Cowbon', gender=True)
    db.session.add(student)
    db.session.commit()
    return jsonify(status=0, id=student.id)