#!flask/bin/python
from flask import Flask, jsonify, abort, request
import meeting
import json
import requests
import MySQLdb

app = Flask(__name__)

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
    "date" : 0byyyyyyymmmmddddd,
    "start_time" : 0bhhhhhmmmmmm,
    "end_time" : 0bhhhhhmmmmmm,
    "attendees" : [id1, id2, id3,...],
    "status" : -1,
    "is routine" : 0,
    "need hw support" : 1,
    "sites" : [id1, id2, ...]
}"""

'''initiate a new meeting'''
@app.route('/backend/api/v1.0/meetings', methods=['POST'])
def initiate_recommend():
    #initiate a meeting
    if not request.json or not 'title' in request.json:
        abort(400)
    new_meeting = Meeting()
    new_meeting.id = #read from database the largest id and +1
    new_meeting.meeting_name = request.json["meeting_name"]
    new_meeting.meeting_topic = request.json["meeting_topic"]
    new_meeting.date = convert_date(request.json["date"]) #data type?
    new_meeting.start_time = convert_time(request.json["start_time"])
    new_meeting.end_time = convert_time(request.json["end_time"])
    new_meeting.is_routine = request.json["is routine"]
    new_meeting.requires = request.json["need hw support"]
    new_meeting.sites = request.json["sites"]
    #recommend

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

if __name__ == "__main__":
    app.run(debug=True)
'''