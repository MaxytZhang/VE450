#!/usr/bin/python3
import Meeting
import json
import MeetingRoom
import pymysql
import datetime
import DatabaseOperator
import random


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
        host='gdm64397110.my3w.com',  # host
        port=3306,  # 默认端口，根据实际修改
        user='gdm64397110',  # 用户名
        passwd='VE450Team7',  # 密码
        db='gdm64397110_db',  # DB name
        charset='utf8mb4'
    )
    cursor = db.cursor()
    cursor.execute("SELECT version()")
    result = cursor.fetchone()
    print(result[0])
    sql = 'SELECT * FROM dooraccess'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    employee_id, badge_id, has_access = 1,1,0
    sql = 'INSERT INTO dooraccess(EmployeeID, BadgeID, Access) VALUES (%f, %f, %f)'
    data = (employee_id, badge_id, has_access)
    cursor.execute(sql % data)
    db.commit()
    sql = 'SELECT * FROM dooraccess'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    badge_id, has_access = 1,1
    sql = 'UPDATE dooraccess SET Access = %f WHERE BadgeID = %f'
    data = (badge_id, has_access)
    cursor.execute(sql % data)
    db.commit()
    sql = 'SELECT * FROM dooraccess'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    employee_id = 1
    sql = 'DELETE FROM dooraccess WHERE EmployeeID = %f'
    data = (employee_id)
    cursor.execute(sql % data)
    db.commit()
    sql = 'SELECT * FROM dooraccess'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)


if __name__ == '__main__':
    # i = random.randint(1, 20)
    # print(i)
    # select_list = range(1, 41)
    # a = random.sample(select_list, i)
    # print(a)
    # db = DatabaseOperator.DatabaseOperator()
    # for i in a:
    #     db.Cursor.execute('SELECT EmployeeName, SiteID FROM employee WHERE EmployeeID = %d' % i)
    #     result = db.Cursor.fetchone()
    #     k = {'id': i, 'name': result[0], 'site': result[1], 'status': -1, 'feedback': 'coming', 'role': 'staff'}
    json_meeting = json.loads('{"type": "meeting", "meeting_name": "asdas", "meeting_topic": "assa", "is_routine": 0, "date": "2019-08-06", "startTime": "01:00", "endTime": "03:15", "sites": ["SiteA"], "attendees": [[1, 1], [1, 4], [1, 13], [1, 20], [1, 21], [1, 24], [1, 31], [1, 34], [1, 35], [1, 37], [1, 39], [1, 40]], "need_hw_support": 0, "initiator": 1, "start_timestamp": 1565024400000, "end_timestamp": 1565032500000, "meeting_outline": ["asdasd"], "outline_descriptions": [\"\"], "meeting_room": [[1, 5]]}')
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
    currentMeeting = Meeting.Meeting(json_meeting)
    # currentMeeting.submit()
    # currentMeeting.id = 1
    # currentMeeting.meeting_name = generate_name(1)
    # currentMeeting.meeting_topic = 'test meeting'
    # currentMeeting.meeting_room_id = {}
    # currentMeeting.date = convert_date(1564469999)
    # currentMeeting.start_time = convert_time(1564469999)
    # currentMeeting.end_time = convert_time(1564498799)
    # currentMeeting.attendees = attendeeList
    # currentMeeting.status = 3  # before, during, after
    # currentMeeting.is_routine = False
    # currentMeeting.requires = False
    # currentMeeting.sites = [1, 2, 3]
    # currentMeeting.outline = []  # list of strings
    # currentMeeting.initiator = 1
    # currentMeeting.memo = {}
    # print(currentMeeting.id)
    # print(currentMeeting.attendees)
    # currentMeeting.update_db()

    # recommendation, flag = currentMeeting.recommend()
    # if recommendation == {}:
    #     print("No recommendation available, please try some other time.")
    # elif flag == 0:
    #     print("The recommended rooms are:")
    #     for site_id in recommendation:
    #         print(site_id+':')
    #         for room_key in recommendation[str(site_id)]:
    #             print(room_key, end=' ')
    #         print('')
    # elif flag == 1:
    #     print("We have lowered the capacity to schedule the meeting.\n")
    #     print("The recommended rooms are:")
    #     for site_id in recommendation:
    #         print(site_id+':')
    #         for room_key in recommendation[str(site_id)]:
    #             print(room_key, end=' ')
    #         print('')

    # DatabaseOperator.DatabaseOperator().selection_list(3)
    # DatabaseOperator.DatabaseOperator().selection_list_history('meeting_21_15324409580000')
    print(DatabaseOperator.DatabaseOperator().fetch_meeting_history(1))
    # print(DatabaseOperator.convert_back(35))

    # db_test()
    # new_room = MeetingRoom.MeetingRoom("room_1")
    # print(new_room.set_schedule('meeting_158_1532440958', 3, 8))

    # db_test()
    


