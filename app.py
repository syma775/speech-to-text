import flask
from flask import request,jsonify
import sqlite3

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/',methods=['GET'])
def home():
    return 'Hi Syma Pochu !!!!!'


def dict(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/syma.api/v1/students/all',methods=['GET'])
def student_all():
    conn = sqlite3.connect('Student.db')
    conn.row_factory  = dict
    cur = conn.cursor()
    all_student= cur.execute("SELECT * FROM Student").fetchall()
    return jsonify(all_student)


@app.route('/syma.api/v1/student', methods=['GET'])
def student_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')
    age = query_parameters.get('age')
    roll = query_parameters.get('roll')
    gender = query_parameters.get('gender')

    query = "SELECT * FROM Student WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)

    if name:
        query += ' name=? AND'
        to_filter.append(name)

    if age:
        query += ' age=? AND'
        to_filter.append(age)

    if roll:
        query += ' roll=? AND'
        to_filter.append(roll)

    if gender:
        query += ' gender=? AND'
        to_filter.append(gender)
  

    query = query[:-4] + ';'

    conn = sqlite3.connect('Student.db')
    conn.row_factory = dict
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()
    return jsonify(results)

app.run()




# if __name__ == '_main_':
#     app.run(debug=True)