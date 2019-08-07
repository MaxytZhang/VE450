#!/usr/bin/python3
import datetime
import time
import json
import pymysql
from Models.MeetingRoom import MeetingRoom
from Models.DatabaseOperator import DatabaseOperator


def convert_date(tstp):
    time = datetime.datetime.fromtimestamp(tstp)
    return time.date()


def convert_time(tstp):
    time = datetime.datetime.fromtimestamp(tstp)
    # convert the time slots to 0-95
    return time.hour * 4 + time.minute / 15


def meet_requirements(room_id, number, requires, start_time, end_time, meeting_date):
    room = MeetingRoom(room_id)
    if number <= room.capacity and requires <= room.hardware:
        if meeting_date in room.schedule:
            for slot_id in room.schedule[meeting_date][start_time:end_time]:
                if slot_id != '':
                    return False, room.capacity
            return True, room.capacity
        else:
            return True, room.capacity
    return False, room.capacity


class Meeting:
    def __init__(self, meeting_info):
        # meeting id = timestamp + initiator id
        self.meeting_id = 'meeting_' + str(meeting_info['initiator']) + '_' + str(int(time.time()))
        self.meeting_name = meeting_info['meeting_name']
        self.meeting_topic = meeting_info['meeting_topic']
        self.meeting_room_id = None
        if 'meeting_room' in meeting_info:
            self.meeting_room_id = [x[1] for x in meeting_info['meeting_room']]
        self.date = convert_date(int(meeting_info['start_timestamp']) / 1000)
        self.start_time = convert_time(int(meeting_info['start_timestamp']) / 1000)
        self.end_time = convert_time(int(meeting_info['end_timestamp']) / 1000)
        self.attendees = meeting_info['attendees']
        self.attendees = []
        for attendee in meeting_info['attendees']:
            attendee_info = {
                'id': attendee[1],
                'site': attendee[0],
                'feedback': None,
                'status': None,
            }
            if attendee[1] == meeting_info['initiator']:
                attendee_info['role'] = 'initiator'
            else:
                attendee_info['role'] = 'staff'
            self.attendees.append(attendee_info)
        self.priority = 0
        self.status = -1  # before, during, after
        self.is_routine = meeting_info['is_routine']
        self.requires = meeting_info['need_hw_support']
        self.sites = list(set([attendee['site'] for attendee in self.attendees]))
        self.outline = meeting_info['meeting_outline']
        self.initiator = meeting_info['initiator']
        self.memo = {}

        self.db = pymysql.connect(
            host = 'gdm64397110.my3w.com',  # host
            port = 3306,  # 默认端口，根据实际修改
            user = 'gdm64397110',  # 用户名
            passwd = 'VE450Team7',  # 密码
            db = 'gdm64397110_db',  # DB name
            charset = 'utf8mb4'
        )
        self.cursor = self.db.cursor()

    @staticmethod
    def reminder(self):
        for attendees in self.attendees:
            send_reminder(attendees.id)

    def memo(self):
        for attendees in self.attendees:
            send_memo(attendees.id)

    def outline(self):
        for attendees in self.attendees:
            send_outline(attendees.id)

    def init_db(self):
        db = DatabaseOperator()
        db.init_meeting(self)

    def update_db(self):
        db = DatabaseOperator()
        db.modify_meeting(self)

    @staticmethod
    def release(self, button_pressed, room_is_empty, current_time):
        if button_pressed:
            for room_id in self.meeting_room_id:
                self.cursor.execute("UPDATE meetingroom SET Occupancy = 0 WHERE MeetingRoomID = %s", room_id)
                self.db.commit()
                if self.end_time != current_time:
                    room = MeetingRoom.MeetingRoom(room_id)
                    room.change_schedule(self.meeting_id, current_time)
        else:
            for empty_id in room_is_empty:
                if empty_id:
                    self.cursor.execute("UPDATE meetingroom SET Occupancy = 0 WHERE MeetingRoomID = %s", empty_id)
                    self.db.commit()
                    if self.end_time != current_time:
                        room = MeetingRoom.MeetingRoom(empty_id)
                        room.change_schedule(self.meeting_id, current_time)
        self.end_time = current_time
        self.end_meeting()

    def recommend(self):
        site_attendees = {}
        # Count the number of people in each site
        for member in self.attendees:
            if str(member['site']) in site_attendees:
                site_attendees[str(member['site'])] += 1
            else:
                site_attendees[str(member['site'])] = 1
        for site_id in site_attendees:
            print(str(site_attendees[site_id]) + ' people in site ' + site_id + ' need to attend the meeting.')

        site_recommend_list = {}
        limitation_flag = False  # see if the solution can be find
        for site_id in self.sites:
            site_recommend_list[str(site_id)] = []
            self.cursor.execute("SELECT MeetingRoom FROM site WHERE SiteID = %d" % site_id)
            result = self.cursor.fetchone()
            site_list = json.loads(result[0])
            for room_id in site_list:
                if meet_requirements(room_id, site_attendees[str(site_id)], self.requires, self.start_time, self.end_time,
                                     self.date)[0]:
                    site_recommend_list[str(site_id)].append(room_id)
            if not site_recommend_list[str(site_id)]:
                print('\nThere\'s no meeting room available for site ' + str(site_id))
                limitation_flag = True

        # if no recommendation, try again without capacity restriction
        if limitation_flag:
            for site_id in self.sites:
                if site_recommend_list[str(site_id)] == []:
                    room_flag = ''
                    flag_cap = -1
                    self.cursor.execute("SELECT MeetingRoom FROM site WHERE SiteID = %d" % site_id)
                    result = self.cursor.fetchone()
                    site_list = json.loads(result[0])
                    for room_id in site_list:
                        require_flag, room_cap = meet_requirements(room_id, self.requires, site_attendees[str(site_id)],
                                                                   self.start_time, self.end_time, self.date)
                        if require_flag:
                            if room_flag == '':
                                room_flag, flag_cap = room_id, room_cap
                            elif room_cap > flag_cap:
                                room_flag, flag_cap = room_id, room_cap
                    site_recommend_list[str(site_id)].append(room_id)
                    if not site_recommend_list[str(site_id)]:
                        return [], True
        trans_list = []
        for i in site_recommend_list:
            self.cursor.execute("SELECT SiteName FROM site WHERE SiteID = %d" % int(i))
            s_name = self.cursor.fetchone()[0]
            trans_item = {'value': int(i), 'label': s_name, 'children': []}
            c_list = []
            for c in site_recommend_list[i]:
                c_list.append({'value': c, 'label': 'room_' + str(c)})
            trans_item['children'] = c_list
            trans_list.append(trans_item)
        return trans_list, limitation_flag

    def submit(self):
        # try:
        #     self.init_db()
        # except:
        #     self.update_db()
        self.init_db()
        for room_id in self.meeting_room_id:
            room = MeetingRoom(room_id)
            room.set_schedule(self.meeting_id, self.start_time, self.end_time)
        for employee in self.attendees:
            self.cursor.execute("SELECT MeetingHistory FROM employee WHERE EmployeeID = {}".format(employee['id']))
            e = json.loads(self.cursor.fetchone()[0])
            e['future'].append(self.meeting_id)
            self.cursor.execute(
                "UPDATE employee SET MeetingHistory = \'{}\' WHERE EmployeeID = {}".format(json.dumps(e), employee['id']))
            self.db.commit()


    def modify(self, meeting_name, meeting_topic, date, start_time, end_time, attendees, is_routine):
        flag = self.start_time == start_time and self.end_time == end_time and self.attendees == attendees
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_name = meeting_name
        self.meeting_topic = meeting_topic
        self.date = date
        self.attendees = attendees
        self.is_routine = is_routine
        if flag:
            self.release(True, [])
            self.recommend()

    def extend(self, extend_time):
        for room_id in self.meeting_room_id:
            if not meet_requirements(room_id, False, 0, self.end_time, self.end_time + extend_time)[0]:
                return False
        for room_id in self.meeting_room_id:
            room = MeetingRoom.MeetingRoom(room_id)
            room.set_schedule(self.meeting_id, self.end_time, self.end_time + extend_time)
        self.end_time = self.end_time + extend_time
        return True

    def start_meeting(self):
        self.cursor.execute("SELECT Attendee FROM meeting WHERE MeetingID = {}".format(self.meeting_id))
        attendee_list = json.loads(self.cursor.fetchone()[0])
        for employee in attendee_list:
            self.cursor.execute("SELECT MeetingHistory FROM employee WHERE EmployeeID = {}".format(employee[0]))
            e = json.loads(self.cursor.fetchone()[0])
            e['future'].remove(self.meeting_id)
            e['present'].append(self.meeting_id)
            self.cursor.execute("UPDATE employee SET MeetingHistory = \'{}\' WHERE EmployeeID = {}".format(json.dumps(e), employee[0]))
            self.db.commit()

    def end_meeting(self):
        self.cursor.execute("SELECT Attendee FROM meeting WHERE MeetingID = {}".format(self.meeting_id))
        attendee_list = json.loads(self.cursor.fetchone()[0])
        for employee in attendee_list:
            self.cursor.execute("SELECT MeetingHistory FROM employee WHERE EmployeeID = {}".format(employee[0]))
            e = json.loads(self.cursor.fetchone()[0])
            e['present'].remove(self.meeting_id)
            e['past'].append(self.meeting_id)
            self.cursor.execute("UPDATE employee SET MeetingHistory = \'{}\' WHERE EmployeeID = {}".format(json.dumps(e), employee[0]))
            self.db.commit()
