#!/usr/bin/python3
import datetime
import json
import pymysql
import MeetingRoom


def convert_date(tstp):
    time = datetime.datetime.fromtimestamp(tstp)
    return time.date()


def convert_time(tstp):
    time = datetime.datetime.fromtimestamp(tstp)
    # convert the time slots to 0-95
    return time.hour * 4 + time.minute / 15


def meet_requirements(room_id, number, requires, start_time, end_time, meeting_date):
    room = MeetingRoom.MeetingRoom(room_id)
    if number <= room.capacity and requires <= room.hardware and meeting_date in room.schedule:
        for slot_id in room.schedule[meeting_date][start_time:end_time]:
            if slot_id != '':
                return False, room.capacity
        return True, room.capacity
    return False, room.capacity


class Meeting:
    def __init__(self, meeting_info):
        # meeting id = timestamp + initiator id
        self.meeting_id = 'meeting_' + str(meeting_info['initiator']) + '_' + str(meeting_info['start_timestamp'])
        self.meeting_name = meeting_info['meeting_name']
        self.meeting_topic = meeting_info['meeting_topic']
        self.meeting_room_id = list(meeting_info['meeting_rooms'])
        self.date = convert_date(int(meeting_info['start_timestamp']) / 1000)
        self.start_time = convert_time(int(meeting_info['start_timestamp']) / 1000)
        self.end_time = convert_time(int(meeting_info['end_timestamp']) / 1000)
        self.attendees = meeting_info['attendees']
        self.priority = 0
        self.status = -1  # before, during, after
        self.is_routine = meeting_info['is_routine']
        self.requires = meeting_info['need_hw_support']
        self.sites = list(meeting_info['sites'])
        self.outline = meeting_info['meeting_outline']
        self.initiator = meeting_info['initiator']
        self.memo = {}

        self.db = pymysql.connect(
            host='gdm64397110.my3w.com',  # host
            port=3306,  # 默认端口，根据实际修改
            user='gdm64397110',  # 用户名
            passwd='VE450Team7',  # 密码
            db='gdm64397110_db',  # DB name
            charset='utf8mb4'
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
        sql = "INSERT INTO meeting values(\'%s\', \'%s\', \'%s\', \'{room_list}\', \'{meeting_date}\', %d, %d, \'{attendees}\', %d, %d, %d, \'{site_json}\', \'{{}}\', %d, \'{{}}\')" % (
            self.meeting_id, self.meeting_name, self.meeting_topic, self.start_time, self.end_time, self.status,
            self.is_routine, self.requires, self.initiator)
        sql = sql.format(
            attendees=json.dumps(self.attendees),
            room_list=json.dumps(self.meeting_room_id),
            meeting_date=str(self.date),
            site_json=json.dumps(self.sites)
        )
        self.cursor.execute(sql)
        self.db.commit()

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

    def recommend(self):
        site_attendees = {}
        # Count the number of people in each site
        for member in self.attendees:
            if self.attendees[member]['site'] in site_attendees:
                site_attendees[self.attendees[member]['site']] += 1
            else:
                site_attendees[self.attendees[member]['site']] = 1
        for site_id in site_attendees:
            print(str(site_attendees[site_id]) + ' people in site ' + site_id + ' need to attend the meeting.')

        site_recommend_list = {}
        limitation_flag = False  # see if the solution can be find
        for site_id in self.sites:
            site_recommend_list[site_id] = []
            self.cursor.execute("SELECT MeetingRoom FROM site WHERE SiteID = %s", site_id)
            result = self.cursor.fetchone()
            site_list = json.loads(result[0])
            for room_id in site_list:
                if meet_requirements(room_id, self.requires, site_attendees[site_id], self.start_time, self.end_time, self.date)[0]:
                    site_recommend_list[site_id].append(room_id)
            if not site_recommend_list[site_id]:
                print('\nThere\'s no meeting room available for site ' + str(site_id))
                limitation_flag = True

        # if no recommendation, try again without capacity restriction
        if limitation_flag:
            for site_id in self.sites:
                if site_recommend_list[site_id] == []:
                    room_flag = ''
                    flag_cap = -1
                    self.cursor.execute("SELECT MeetingRoom FROM site WHERE SiteID = %s", site_id)
                    result = self.cursor.fetchone()
                    site_list = json.loads(result[0])
                    for room_id in site_list:
                        require_flag, room_cap = meet_requirements(room_id, self.requires, site_attendees[site_id], self.start_time, self.end_time, self.date)
                        if require_flag:
                            if room_flag == '':
                                room_flag, flag_cap = room_id, room_cap
                            elif room_cap > flag_cap:
                                room_flag, flag_cap = room_id, room_cap
                    site_recommend_list[site_id].append(room_id)
                    if not site_recommend_list[site_id]:
                        return {}, True
        return site_recommend_list, limitation_flag

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
