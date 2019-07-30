#!/usr/bin/python3
import Meeting
import json
import MeetingRoom
import pymysql
import datetime


def convert_date(tstp):
    time = datetime.datetime.fromtimestamp(tstp)
    return time.date()


def convert_time(tstp):
    time = datetime.datetime.fromtimestamp(tstp)
    # convert the time slots to 0-95
    return time.hour * 4 + time.minute / 15


def generate_name(meetingId):
    return "Meeting_" + str(meetingId)


def db_test():
    db = pymysql.connect(
        host='127.0.0.1',  # host
        port=3306,  # 默认端口，根据实际修改
        user='root',  # 用户名
        passwd='HHLK1479',  # 密码
        db='lbs_db',  # DB name
        charset='utf8',
    )
    cursor = db.cursor()
    cursor.execute("SELECT version()")
    result = cursor.fetchone()
    print(result[0])


if __name__ == '__main__':
    json_meeting = """{
        "id" : 0,
        "meeting_name" : "meeting_1",
        "meeting_topic" : "design review 3 is killing me",
        "start_timestamp" : 1232440958,
        "end_timestamp" : 1232440960,
        "attendees" : {id1:{"status":-1,"feedback":"coming","role":"staff","site":11},id2:{"status":-1,"feedback":"coming","role":"staff","site":1}},
        "status" : -1,
        "is routine" : 0,
        "need hw support" : 1,
        "sites" : [id1, id2, ...],
        "meeting memo" : {id1 : "memo1", id2 : "memo2"},
        "meeting outline" : ["outline1", "outline2"],
        "initiator" : 1239084(id)
    }"""
    meetingRoom = {
        "site_1_1": {
            "id": 1,
            "site": 1,
            "capacity": 2,
            "name": "SongJiangMeetingRoom1",
            "hardware": 1
        },
        "site_1_2": {
            "id": 2,
            "site": 1,
            "capacity": 3,
            "name": "SongJiangMeetingRoom2",
            "hardware": 1
        },
        "site_1_3": {
            "id": 3,
            "site": 1,
            "capacity": 4,
            "name": "SongJiangMeetingRoom3",
            "hardware": 1
        },
        "site_1_4": {
            "id": 4,
            "site": 1,
            "capacity": 1,
            "name": "SongJiangMeetingRoom4",
            "hardware": 1
        },
        "site_1_5": {
            "id": 5,
            "site": 1,
            "capacity": 5,
            "name": "SongJiangMeetingRoom5",
            "hardware": 1
        },
        "site_2_1": {
            "id": 6,
            "site": 2,
            "capacity": 2,
            "name": "LinGangMeetingRoom1",
            "hardware": 1
        },
        "site_2_2": {
            "id": 7,
            "site": 2,
            "capacity": 3,
            "name": "LinGangMeetingRoom2",
            "hardware": 1
        },
        "site_2_3": {
            "id": 8,
            "site": 2,
            "capacity": 4,
            "name": "LinGangMeetingRoom3",
            "hardware": 1
        },
        "site_2_4": {
            "id": 9,
            "site": 2,
            "capacity": 1,
            "name": "LinGangMeetingRoom4",
            "hardware": 1
        },
        "site_2_5": {
            "id": 10,
            "site": 2,
            "capacity": 5,
            "name": "LinGangMeetingRoom5",
            "hardware": 1
        },
        "site_3_1": {
            "id": 11,
            "site": 3,
            "capacity": 3,
            "name": "JIMeetingRoom1",
            "hardware": 1
        },
        "site_3_2": {
            "id": 12,
            "site": 3,
            "capacity": 5,
            "name": "JIMeetingRoom2",
            "hardware": 1
        }
    }
    attendeeList = {
        "100001": {
            "status": 0,
            "feedback": "coming",
            "role": "initiator",
            "site": 1
        },
        "101001": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 1
        },
        "101002": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 1
        },
        "101003": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 1
        },
        "102001": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 2
        },
        "102002": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 2
        },
        "102003": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 2
        },
        "103001": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 3
        },
        "103002": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 3
        },
        "103003": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 3
        },
        "103004": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 3
        },
        "103005": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 3
        },
        "103006": {
            "status": 0,
            "feedback": "coming",
            "role": "staff",
            "site": 3
        },
    }
    siteList = [
        {
            "name": "SongJiang",
            "meetingRoom": [
                "site_1_1",
                "site_1_2",
                "site_1_3",
                "site_1_4",
                "site_1_5"
            ],
            "roomNumber": 5
        },
        {
            "name": "LinGang",
            "meetingRoom": [
                "site_2_1",
                "site_2_2",
                "site_2_3",
                "site_2_4",
                "site_2_5"
            ],
            "roomNumber": 5
        },
        {
            "name": "JI",
            "meetingRoom": [
                "site_3_1",
                "site_3_2"
            ],
            "roomNumber": 2
        }
    ]
    currentMeeting = Meeting.Meeting()
    currentMeeting.id = 1
    currentMeeting.meeting_name = generate_name(1)
    currentMeeting.meeting_topic = 'test meeting'
    currentMeeting.meeting_room_id = {}
    currentMeeting.date = convert_date(1564469999)
    currentMeeting.start_time = convert_time(1564469999)
    currentMeeting.end_time = convert_time(1564498799)
    currentMeeting.attendees = attendeeList
    currentMeeting.status = -1  # before, during, after
    currentMeeting.is_routine = False
    currentMeeting.requires = False
    currentMeeting.sites = [1, 2, 3]
    currentMeeting.outline = []  # list of strings
    currentMeeting.initiator = 1
    currentMeeting.memo = {}
    # print(currentMeeting.id)
    # print(currentMeeting.attendees)

    recommendation, flag = currentMeeting.recommend(meetingRoom, siteList)
    if recommendation == {}:
        print("No recommendation available, please try some other time.")
    elif flag == 0:
        print("The recommended rooms are:")
        for site_id in recommendation:
            print(siteList[site_id-1]['name']+':')
            for room_key in siteList[site_id-1]['meetingRoom']:
                if meetingRoom[room_key]['id'] in recommendation[site_id]:
                    print(meetingRoom[room_key]['name'])
            print('')
    elif flag == 1:
        print("We have lowered the capacity to schedule the meeting.\n")
        print("The recommended rooms are:")
        for site_id in recommendation:
            print(siteList[site_id-1]['name']+':')
            for room_key in siteList[site_id-1]['meetingRoom']:
                if meetingRoom[room_key]['id'] in recommendation[site_id]:
                    print(meetingRoom[room_key]['name'])
            print('')

    # db_test()
    new_room = MeetingRoom.MeetingRoom(1)
    print(new_room.open_door(2, 20))
