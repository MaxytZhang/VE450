#!/usr/bin/python3
import datetime
import json
import pymysql


class MeetingRoom:
    def __init__(self, room_id):
        self.db = pymysql.connect(
            host='gdm64397110.my3w.com',  # host
            port=3306,  # 默认端口，根据实际修改
            user='gdm64397110',  # 用户名
            passwd='VE450Team7',  # 密码
            db='gdm64397110_db',  # DB name
            charset='utf8mb4'
        )
        self.cursor = self.db.cursor()

        self.room_id = room_id

        self.cursor.execute("SELECT * FROM meetingroom WHERE MeetingRoomID = %s", room_id)
        result = self.cursor.fetchone()
        self.capacity = result[1]
        self.occupancy = result[2]
        self.remote = result[3]
        self.schedule = json.loads(result[4])
        self.site = result[5]
        self.hardware = result[6]

    def __del__(self):
        self.db.close()
        self.cursor.close()

    @property
    def is_empty(self):
        return self.occupancy

    def update_schedule(self):
        sql_update = "UPDATE meetingroom SET Schedule = \'{json_sch}\' WHERE MeetingRoomID = \"%s\"" % self.room_id
        sql_update = sql_update.format(
            json_sch=json.dumps(self.schedule)
        )
        self.cursor.execute(sql_update)
        self.db.commit()

    def open_door(self, employee, time_slot):
        try:
            self.cursor.execute("SELECT * FROM test_data WHERE time = %d and bg_id = %d" % (time_slot, employee))
            data = self.cursor.fetchone()
            print(data)
            self.cursor.execute(
                "UPDATE test_data SET permission = 4 WHERE time = %d and bg_id = %d" % (time_slot, employee))
            self.db.commit()
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
        meeting_date = str(meeting_record[0])

        if meeting_date not in self.schedule:
            self.schedule[meeting_date] = [''] * 96
        for interval in range(start_time, end_time):
            self.schedule[meeting_date][interval] = meeting_id
        self.update_schedule()
        return self.schedule

    def cancel_schedule(self, meeting_id):
        self.cursor.execute("SELECT Date FROM meeting WHERE MeetingID = %s", meeting_id)
        meeting_record = self.cursor.fetchone()
        meeting_date = meeting_record[4]

        for slot_id in range(96):
            if self.schedule[meeting_date][slot_id] == meeting_id:
                self.schedule[meeting_date][slot_id] = ''
        self.update_schedule()

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
        self.update_schedule()
