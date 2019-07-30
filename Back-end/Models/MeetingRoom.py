#!/usr/bin/python3
import datetime
import pymysql


class MeetingRoom:
    def __init__(self, room_id):
        self.db = pymysql.connect(
            host='127.0.0.1',  # host
            port=3306,  # 默认端口，根据实际修改
            user='root',  # 用户名
            passwd='123123',  # 密码
            db='lbs_db',  # DB name
            charset='utf8',
        )
        self.cursor = self.db.cursor()

        self.room_id = room_id

        self.cursor.execute("SELECT SiteID FROM meetingroom WHERE MeetingRoomID = %s", room_id)
        siterecord = self.cursor.fetchone()
        self.site = siterecord[0]

        self.cursor.execute("SELECT Capacity FROM meetingroom WHERE MeetingRoomID = %s", room_id)
        caprecord = self.cursor.fetchone()
        self.capacity = caprecord[0]

        self.cursor.execute("SELECT Occupancy FROM meetingroom WHERE MeetingRoomID = %s", room_id)
        occurecord = self.cursor.fetchone()
        self.occupancy = occurecord[0]

        self.cursor.execute("SELECT Remote FROM meetingroom WHERE MeetingRoomID = %s", room_id)
        remoterecord = self.cursor.fetchone()
        self.remote = remoterecord[0]

        # self.cursor.execute("SELECT Schedule FROM meetingroom WHERE MeetingRoomID = %s", room_id)
        # schrecord = self.cursor.fetchone()
        # self.schedule = schrecord[0]
        self.schedule = {}

        self.cursor.execute("SELECT Hardware FROM meetingroom WHERE MeetingRoomID = %s", room_id)
        hwrecord = self.cursor.fetchone()
        self.hardware = hwrecord[0]

    def __del__(self):
        self.db.close()
        self.cursor.close()

    @property
    def is_empty(self):
        return self.occupancy

    def open_door(self, employee, time_slot):
        try:
            self.cursor.execute("SELECT * FROM test_data WHERE time = %d and bg_id = %d" % (time_slot, employee))
            data = self.cursor.fetchone()
            print(data)
            if data[2] == 1:
                return True
            else:
                return False
        except:
            print("Error!")

        # if employee.id in get_meeting_attendees(self.schedule[len(self.schedule) - 1][0]):
        #     return True
        # else:
        #     return False

    def get_schedule(self):
        return self.schedule

    def set_schedule(self, meeting_id, start_time, end_time):
        self.cursor.execute("SELECT Date FROM meeting WHERE MeetingID = %s", meeting_id)
        meeting_record = self.cursor.fetchone()
        meeting_date = meeting_record[4]

        if meeting_date not in self.schedule:
            self.schedule[meeting_date] = [''] * 96
        for interval in range(start_time, end_time):
            self.schedule[meeting_date][interval] = meeting_id
        return self.schedule

    def cancel_schedule(self, meeting_id):
        self.cursor.execute("SELECT Date FROM meeting WHERE MeetingID = %s", meeting_id)
        meeting_record = self.cursor.fetchone()
        meeting_date = meeting_record[4]

        for slot_id in range(96):
            if self.schedule[meeting_date][slot_id] == meeting_id:
                self.schedule[meeting_date][slot_id] = ''

    def change_schedule(self, meeting_id, new_end_time):
        self.cursor.execute("SELECT Date FROM meeting WHERE MeetingID = %s", meeting_id)
        meeting_record = self.cursor.fetchone()
        meeting_date = meeting_record[4]

        slot_id = new_end_time - 1
        while slot_id >= 0 and self.schedule[meeting_date][slot_id] != meeting_id:
            if self.schedule[meeting_date][slot_id] != '':
                print('Time slot already been taken!')
                break
            else:
                self.schedule[meeting_date][slot_id] = meeting_id
                slot_id -= 1

    def meet_requirements(self, number, requires, start_time, end_time, meeting_date):
        if number <= self.capacity and requires < self.hardware:
            for slot_id in self.schedule[meeting_date][start_time:end_time]:
                if slot_id != '':
                    return False
            return True
        return False
