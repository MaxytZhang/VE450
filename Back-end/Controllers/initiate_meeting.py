#!flask/bin/python
from flask import Flask, jsonify, abort, request
from flask_cors import *
from Models.Meeting import Meeting
import json
import requests
import datetime

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
        return jsonify(make_package("error","error - sending wrong data"))
    meeting_info = package
    new_meeting = Meeting()
    if meeting_info["meeting_name"] == "":
        meeting_info["meeting_name"] = generate_name(new_meeting.id)
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