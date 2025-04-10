from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route('/schedules', methods=['GET'])
def get_schedules():
    schedules = [
        {"faculty": "Dr. Smith", "course": "Math 101", "room": "A101", "time": "10:00"},
        {"faculty": "Prof. Johnson", "course": "CS 101", "room": "B202", "time": "11:00"},
        {"faculty": "Dr. Carter", "course": "Chemistry 101", "room": "C303", "time": "12:00"}
    ]
    return jsonify(schedules)

if _name_ == '_main_':
    app.run(debug=True)