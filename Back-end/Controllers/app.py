#!flask/bin/python
from flask import Flask, jsonify, abort, request
from flask_cors import *
from Models.Meeting import Meeting
import json
import requests
import datetime
import time
from Models.DatabaseOperator import DatabaseOperator as DB
# import mysql.connector
# from mysql.connector import Error


app = Flask(__name__)
# CORS(app, supports_credentials = True)
'''description of the tasks that need to be performed based on the front-end design 
once a button is clicked. (can be used as documentation)'''
tasks = [
    {
        "id": 1,
        "title": u"Check Login Info",
        "description": u"Gets login info from the front-end, and returns a bool & perform task 2 (for success) / an error message (for failure)."
    },
    {
        "id": 2,
        "title": u"Publish Home",
        "description": u"Gets user id (possibly from task 1), and returns current user\'s icon, id, department, top 3 notices, on going meeting, next meetings, etc."
    },
    {
        "id": 3,
        "title": u"Notices - More",
        "description": u"Gets user id, and returns all notices of current user."
    },
    {
        "id": 4,
        "title": u"Ongoing & Next Meetings - check",
        "description": u"Gets meeting id, and returns date, time, location(for the current user), name, topic, outline, file links."
    },
    {
        "id": 5,
        "title": u"Start a New Meeting",
        "description": u"Returns the names and ids of all sites, and all employees (returns employee after site selection or what?)"
    },
    {
        "id": 6,
        "title": u"New Meeting - step 2 Next",
        "description": u"Gets meeting name, topic, date, time, attendees, sites and meeting outline(s), and returns meeting id and meeting recommendation list(site and room)."
    },
    {
        "id": 7,
        "title": u"New Meeting - step 3 Previous",
        "description": u"Gets meeting id, and returns meeting name, topic, date, time, attendees, sites and meeting outline(s) from the meeting object."
    },
    {
        "id": 8,
        "title": u"New Meeting - step 3 Submit",
        "description": u"Gets meeting id and user\'s choices of meeting rooms, move the meeting object info to the meeting database."
    },
    {
        "id": 9,
        "title": u"Meeting History",
        "description": u"Gets user id and pulls out meetings[] date, name, site, location, id, and initiator from the employee database."
    }
]

'''JSON data for a meeting - string'''
# you can also use the open function to read the content of a JSON file to a string
json_meeting = """{
    "id" : 0,
    "meeting_name" : "meeting_1",
    "meeting_topic" : "design review 3 is killing me",
    "meeting_rooms" : {site1:id1, site2:id2,...},
    "start_timestamp" : 1232440958,
    "end_timestamp" : 1232440960,
    "attendees" : {id1:{"status":-1,"feedback":"coming","role":"staff","site":11},id2:{"status":-1,"feedback":"coming","role":"staff","site":1},...},
    "status" : -1,
    "is_routine" : 0,
    "need_hw_support" : 1,
    "sites" : [id1, id2, ...],
    "meeting_memo" : {id1 : "memo1", id2 : "memo2", ...},
    "meeting_outline" : ["outline1", "outline2", ...],
    "initiator" : 1239084(id)
}"""

json_recommendation = """{
    site_id1 : [room_id1, room_id2,...],
    site_id2 : [room_id1, room_id2,...]
}"""

json_package = """{
    "type" : "meeting" / "message" / "recommendation" / "error" / "login"
    ...
}"""


'''helper functions & variables'''
length_of_employeeid = 8.;


def generate_name(id):
    return "meeting_" + str(id)


def add_message(msg, pkg):
    pkg["message"] = msg
    return pkg


def add_type(tp, pkg):
    pkg["type"] = tp
    return pkg


'''initiate a new meeting'''
@app.route('/backend/api/v1.0/meetings', methods=['GET', 'POST'])
def initiate_recommend():
    # initiate a meeting
    print(request.json)
    # if not request.json:
    #     abort(400)
    package = request.json
    if not package["type"] == "meeting":
        pkg = {}
        pkg = add_type("error",pkg)
        pkg = add_message("Wrong package sent.", pkg)
        return jsonify(pkg)
    meeting_info = package
    new_meeting = Meeting(meeting_info)
    if meeting_info["meeting_name"] == "":
        meeting_info["meeting_name"] = generate_name(new_meeting.meeting_id)
    # recommend
    recommendation, flag = new_meeting.recommend()
    if recommendation == {}:
        pkg = add_message("No recommendation available, please try some other time.", recommendation)
        pkg = add_type("message",pkg)
        return jsonify(pkg)
    elif flag == 0:
        # return jsonify(add_type("recommendation", recommendation))
        return jsonify(recommendation)
    elif flag == 1:
        pkg = add_type("message and recommendation", recommendation)
        pkg = add_message("We have lowered the capacity to schedule the meeting.", pkg)
        return jsonify(pkg)

@app.route('/backend/api/v1.0/meeting_submit', methods=['GET','POST'])
def submit_meeting():
    package = request.form
    if not package["type"] == "meeting":
        pkg = {}
        pkg = add_type("error",pkg)
        pkg = add_message("Wrong package sent.", pkg)
        return jsonify(pkg)
    meeting_info = package
    submit_mt = Meeting.Meeting(meeting_info)
    submit_mt.submit()
    db = DB()
    db.update_door_access(2,0)
    for item in submit_mt.attendees:
        if item['id'] == 42:
            db.update_door_access(2,1)
            break

@app.route('/backend/api/v1.0/test', methods=['GET', 'POST'])
def test():
    print(request.json)
    print(request.form)
    return jsonify({"type": "message", "message": "Connected."})


@app.route('/backend/api/v1.0/test_upload', methods=['GET','POST'])
def test_upload():
    name = request.form['name']
    age = request.form['age']
    return jsonify(request.form)


@app.route('/backend/api/v1.0/get_sites', methods = ['POST'])
def get_sites():
    employee_id = request.json['id']
    print(employee_id)
    db = DB()
    sites = db.site_list()
    print(sites)
    return jsonify(sites)

@app.route('/backend/api/v1.0/get_user')
def get_user():
    pass

@app.route('/backend/api/v1.0/validate_login', methods = ['POST'])
def validate_login():
    user = request.json
    print(type({}), type(user))
    res = {
        'token': None,
        'info': {},
        'pass': False,
    }
    db = DB()
    validate, info = db.validate(user)
    print(validate, type(validate))
    if validate == 1:
        res['pass'] = True
        res['info']['EmployeeID'] = info[0]
        res['info']['SiteID'] = info[1]
        res['info']['EmployName'] = info[2]
        res['token'] = "{}{}{}".format(info[1], info[0], int(time.time()))
    else:
        res['pass'] = False
    print(res)
    return jsonify(res)

@app.route('/backend/api/v1.0/check_open', methods = ['POST'])
def check_open():
    employee_id = request.json['id']
    print(employee_id)
    db = DB()
    door_access = db.get_door_access(employee_id)
    return jsonify(door_access)

@app.route('/backend/api/v1.0/check_notice', methods = ['POST'])
def check_notice():
    employee_id = request.json
    return jsonify(True)


@app.route('/backend/api/v1.0/get_notice', methods = ['POST'])
def get_notice():
    employee_id = request.json
    return jsonify(['I', 'love', 'you', 'I', 'hate', 'you'])

@app.route('/backend/api/v1.0/get_meeting_history', methods = ['POST'])
def get_meeting_history():
    employee_id = request.json['id']
    db = DB()
    history = db.fetch_meeting_history(employee_id)
    print('history', history)
    return jsonify(history)

@app.route('/backend/api/v1.0/get_ongoing_meeting', methods = ['POST'])
def get_ongoing_meeting():
    employee_id = request.json
    return jsonify({'type': 'meeting', 'meeting_name': 'asds', 'meeting_topic': 'aa', 'is_routine': False, 'date': '2019-08-04', 'startTime': '00:30', 'endTime': '01:00', 'sites': ['Site1'], 'attendees': [['s1', 'ea'], ['s1', 'eb'], ['s1', 'ec']], 'need_hw_support': False, 'initiator': 'admin', 'start_timestamp': 1564849800000, 'end_timestamp': 1564851600000, 'meeting_outline': ['aaaa', 'ffff'], 'outline_descriptions': ['', ''], 'going': True, 'id': 2})


@app.route('/backend/api/v1.0/get_employee', methods = ['POST'])
def get_employee():
    employee_id = request.json['id']
    print(employee_id)
    db = DB()
    employee = db.selection_list_meeting(employee_id)
    print(employee)
    return jsonify(employee)


@app.route('/backend/api/v1.0/finish_recommendation', methods = ['POST'])
def finish_recommendation():
    meeting_info = request.json
    print(meeting_info)
    return jsonify(True)

'''
@app.route("/todo/api/v1.0/tasks", methods=["GET"])
def read_tasks_documentation():
    return jsonify({"tasks": tasks})

@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = filter(lambda t: t["id"] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({"task": task[0]})
'''

def selection_list():
    a = '''SELECT * FROM meeting_test
    where
    JSON_CONTAINS('Attendee'->'$[*].id', "12", '$')'''

if __name__ == "__main__":
    app.run(debug=True)
