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

        self.cursor.execute("SELECT * FROM meetingroom WHERE MeetingRoomID = %d" % room_id)
        result = self.cursor.fetchone()
        self.capacity = result[1]
        self.occupancy = result[2] #0 empty 1 occupy
        self.remote = result[3]
        self.schedule = json.loads(result[4])
        self.site = result[5]
        self.hardware = result[6]

    def __del__(self):
        self.db.close()
        self.cursor.close()

    @property
    def is_empty(self):
        if self.occupancy : 
            current_date = datetime.datetime.now().date()
            current_slot = datetime.datetime.now().time().hour * 4 + datetime.datetime.now().time().minute / 15
            if self.schedule[current_date][current_slot] != '' :
                meeting_id = self.schedule[current_date][current_slot]
                self.cursor.execute("SELECT Attendee FROM meeting WHERE MeetingID = %s", meeting_id)
                data = self.cursor.fetchone()
                all_left = true
                for item in data:
                    self.cursor.execute("SELECT BadgeID FROM dooraccess WHERE EmployeID = %d", item["id"])
                    badge_id =self.cursor.fetchone()
                    self.cursor.execute("SELECT GEO_FENCE_ID FROM 20190801_pos_event_list WHERE BG_ID = %f", badge_id)
                    geo_fence_id = self.cursor.fetchone()[-1]
                    if geo_fence_id == 5 :
                        all_left = false
                        break
                if all_left : 
                    self.occupancy = 0
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
        start_time = int(start_time)
        end_time = int(end_time)
        self.cursor.execute("SELECT Date FROM meeting WHERE MeetingID = %s", meeting_id)
        meeting_record = self.cursor.fetchone()
        meeting_date = str(meeting_record[0])

        if meeting_date not in self.schedule:
            self.schedule[meeting_date] = [''] * 96
        print(start_time, end_time)
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
