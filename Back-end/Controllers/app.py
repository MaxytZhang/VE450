#!flask/bin/python
from flask import Flask, jsonify, abort, request
from flask_cors import *
from Models.Meeting import Meeting
import json
import requests
import datetime
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

def convert_date(tstp):
    time = datetime.datetime.fromtimestamp(tstp)
    return time.date()

def convert_time(tstp):
    time = datetime.datetime.fromtimestamp(tstp)
    #convert the time slots to 0-95
    return (time.hour*4 + time.minute/15)

def generate_name(id):
    return ("Meeting_" + str(id))

def add_message(msg, pkg):
    pkg["message"] = msg
    return pkg

def add_type(tp, pkg):
    pkg["type"] = tp
    return pkg

'''initiate a new meeting'''
@app.route('/backend/api/v1.0/meetings', methods=['GET','POST'])
def initiate_recommend():
    #initiate a meeting
    print(request.form.to_dict())
    # if not request.json:
    #     abort(400)
    package = request.form
    if not package["type"] == "meeting":
        pkg = {}
        pkg = add_type("error",pkg)
        pkg = add_message("Wrong package sent.", pkg)
        return jsonify(pkg)
    meeting_info = package
    new_meeting = Meeting()
    new_meeting.meeting_name = meeting_info["meeting_name"]
    new_meeting.meeting_topic = meeting_info["meeting_topic"]
    new_meeting.date = convert_date(int(meeting_info["start_timestamp"])/1000)
    new_meeting.start_time = convert_time(int(meeting_info["start_timestamp"])/1000)
    new_meeting.end_time = convert_time(int(meeting_info["end_timestamp"])/1000)
    new_meeting.is_routine = meeting_info["is_routine"]
    new_meeting.requires = meeting_info["need_hw_support"]
    new_meeting.sites = meeting_info["sites"]
    new_meeting.meeting_outline = meeting_info["meeting_outline"]
    new_meeting.initiator = meeting_info["initiator"]
    new_meeting.attendees = meeting_info["attendees"]
    new_meeting.id = int(meeting_info["start_timestamp"])/1000 * length_of_employeeid + int(meeting_info["initiator"]) #meeting id = timestamp + initiator id
    if meeting_info["meeting_name"] == "":
        meeting_info["meeting_name"] = generate_name(new_meeting.id)
    #recommend
    recommendation, flag = new_meeting.recommend()
    if recommendation == {}:
        pkg = add_message("No recommendation available, please try some other time.",recommendation)
        pkg = add_type("message",pkg)
        return jsonify(pkg)
    elif flag == 0:
        return jsonify(add_type("recommendation",recommendation))
    elif flag == 1:
        pkg = add_type("message and recommendation", recommendation)
        pkg = add_message("We have lowered the capacity to schedule the meeting.", pkg)
        return jsonify(pkg)

@app.route('/backend/api/v1.0/test', methods=['GET','POST'])
def test():
    print(request.json)
    print(request.form)
    print(request.data)
    print(request.get_json())
    print(request.args)
    return jsonify({"type":"message","message":"Connected."})

@app.route('/backend/api/v1.0/test_upload', methods=['GET','POST'])
def test_upload():
    name = request.form['name']
    age = request.form['age']
    return jsonify(request.form)

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

if __name__ == "__main__":
    app.run(debug=True)
