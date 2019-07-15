#!flask/bin/python
from flask import Flask, jsonify, abort, request
import MySQLdb

app = Flask(__name__)

'''description of the tasks that need to be performed based on the front-end design 
once a button is clicked. (can be used as documentation)'''
tasks = [
    {
        'id': 1,
        'title': u'Check Login Info',
        'description': u'Gets login info from the front-end, and returns a bool & perform task 2 (for success) / an error message (for failure).'
    },
    {
        'id': 2,
        'title': u'Publish Home',
        'description': u'Gets user id (possibly from task 1), and returns current user\'s icon, id, department, top 3 notices, on going meeting, next meetings, etc.'
    },
    {
        'id': 3,
        'title': u'Notices - More',
        'description': u'Gets user id, and returns all notices of current user.'
    },
    {
        'id': 4,
        'title': u'Ongoing & Next Meetings - check',
        'description': u'Gets meeting id, and returns date, time, location(for the current user), name, topic, outline, file links.'
    },
    {
        'id': 5,
        'title': u'Start a New Meeting',
        'description': u'Returns the names and ids of all sites, and all employees (returns employee after site selection or what?)'
    },
    {
        'id': 6,
        'title': u'New Meeting - step 1 Next',
        'description': u'Gets meeting topic, date, time, attendees id, sites id, and isRoutine and initiates a new meeting object, auto-generate the id. Returns meeting ID.'
    },
    {
        'id': 7,
        'title': u'New Meeting - step 2 Previous',
        'description': u'Gets meeting id, and returns meeting topic, date, time, attendees, and sites, from the meeting object.'
    },
    {
        'id': 8,
        'title': u'New Meeting - step 2 Next',
        'description': u'Gets meeting id and meeting outline(s), and returns meeting id and meeting recommendation list(site and room).'
    },
    {
        'id': 9,
        'title': u'New Meeting - step 3 Previous',
        'description': u'Gets meeting id, and returns meeting outline(s) from the meeting object.'
    },
    {
        'id': 10,
        'title': u'New Meeting - step 3 Submit',
        'description': u'Gets meeting id and user\'s choices of meeting rooms, move the meeting object info to the meeting database.'
    },
    {
        'id': 11,
        'title': u'Meeting History',
        'description': u'Gets user id and pulls out meetings[] date, name, site, location, id, and initiator from the employee database.'
    }
]

'''JSON for meetings'''
meetings = [
    {
        "id": 0,
        "name": "Test",
        "topic": "Test for add/delete for a meeting.",
        "roomsSiteAndId": [site-room1, site-room2,...],
        "date": "2019/07/14",
        "startTime": "11:30am",
        "endTime": "1:30pm",
        "attendeeId": [id1, id2, id3,...],
        "isRoutine": 0,
        "needHwSupport": 1
    }
]


@app.route('/todo/api/v1.0/meetings/<int:meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    meeting = filter(lambda m: m['id'] == meeting_id, meetings)
    if len(meeting) == 0:
        abort(404)
    return jsonify({'meeting': meeting[0]})

'''
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def read_tasks_documentation():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
'''