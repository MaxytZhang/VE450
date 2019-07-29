#!/usr/bin/python3
import datetime
import pymysql


class MeetingRoom:
    def __init__(self, id, site, capacity, occupancy, remote, hardware):
        self.id = id
        self.site = site
        self.capacity = capacity
        self.occupancy = occupancy
        self.remote = remote
        self.schedule = {}
        self.hardware = hardware
        self.db = pymysql.connect(
            host='127.0.0.1',  # host
            port=3306,  # 默认端口，根据实际修改
            user='root',  # 用户名
            passwd='123123',  # 密码
            # passwd='HHLK148',  # 密码
            db='lbs_db',  # DB name
            charset='utf8',
        )
        self.cursor = self.db.cursor()
        
        cursor.execute("Select SiteID from meetingroom where MeetingRoomID = %s",(id,))
        siterecord = cursor.fetchone()
        self.site = siterecord[0]
        
        cursor.execute("Select Capacity from meetingroom where MeetingRoomID = %s",(id,))
        caprecord = cursor.fetchone()
        self.capacity = caprecord[0]
        
        cursor.execute("Select Occupancy from meetingroom where MeetingRoomID = %s",(id,))
        occurecord = cursor.fetchone()
        self.occupancy = occurecord[0]

        cursor.execute("Select Remote from meetingroom where MeetingRoomID = %s",(id,))
        remoterecord = cursor.fetchone()
        self.remote = remoterecord[0]
        
        cursor.execute("Select Schedule from meetingroom where MeetingRoomID = %s",(id,))
        schrecord = cursor.fetchone()
        self.schedule = schrecord[0]
        
        cursor.execute("Select Hardware from meetingroom where MeetingRoomID = %s",(id,))
        hwrecord = cursor.fetchone()
        self.hardware = hwrecord[0]

    def __del__(self):
        self.db.close()
        self.cursor.close()

    @property
    def is_empty(self):
        return self.occupancy

    def open_door(self, employee, time_slot):
        try:
            self.cursor.execute("select * from test_data where time = %d and bg_id = %d" % (time_slot, employee))
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
        for interval in range(start_time, end_time):
            self.schedule[datetime.date][interval] = meeting_id
        return self.schedule

    def cancel_schedule(self, meeting_id):
        del self.schedule[meeting_id]

    def change_schedule(self, meeting_id, new_end_time):
        self.schedule[meeting_id][1] = new_end_time

    def meet_requirements(self, number, requires, start_time, end_time, date):
        if number <= self.capacity and requires < self.hardware:
            for time_id in self.schedule[date][start_time:end_time]:
                if time_id != 0:
                    return False
            return True
        return False
