import pymysql
import json


class DatabaseOperator:

    def __init__(self):
        self.DBName = 'gdm64397110_db'
        self.Database = pymysql.connect(
            host = 'gdm64397110.my3w.com',  # host
            port = 3306,  # 默认端口，根据实际修改
            user = 'gdm64397110',  # 用户名
            passwd = 'VE450Team7',  # 密码
            db = 'gdm64397110_db',  # DB name
            charset = 'utf8mb4'
        )
        self.Cursor = self.Database.cursor()

    def __del__(self):
        self.Cursor.close()
        self.Database.close()

    def validate(self, user):
        print(user)
        sql = 'select * from gdm64397110_db.employee where EmployeeName = "{}" and Password = {}'.format(
            user['name'],
            user['password']
        )
        print(sql)
        res = self.Cursor.execute(sql)
        info = self.Cursor.fetchone()
        print(info)
        return res, info

    def init_meeting(self, meeting):
        sql = "INSERT INTO meeting values(\'{id}\', \'{name}\', \'{topic}\', \'{room_list}\', \'{meeting_date}\'," \
              "{start_t}, {end_t}, \'{attendees}\', {status}, {routine}, {hw_requires}, \'{site_json}\', \'{{}}\'," \
              "{initiator}, \'{{}}\')"
        sql = sql.format(
            id = meeting.meeting_id,
            name = meeting.meeting_name,
            topic = meeting.meeting_topic,
            room_list = json.dumps(meeting.meeting_room_id),
            meeting_date = str(meeting.date),
            start_t = meeting.start_time,
            end_t = meeting.end_time,
            attendees = json.dumps(meeting.attendees),
            status = meeting.status,
            routine = meeting.is_routine,
            hw_requires = meeting.requires,
            site_json = json.dumps(meeting.sites),
            initiator = meeting.initiator,
        )
        self.Cursor.execute(sql)
        self.Database.commit()

    def modify_meeting(self, meeting):
        sql = "UPDATE meeting SET Name = \'{name}\', MeetingTopic = \'{topic}\', MeetingRooms = \'{room_list}\', " \
              "Date = \'{meeting_date}\', StartTime = {start_t}, EndTime = {end_t}, Attendee = \'{attendees}\', " \
              "Status = {status}, IsRoutine = {routine}, Requires = {hw_requires}, Sites = \'{site_json}\', " \
              "Initiator = {initiator} WHERE MeetingID = \'{meeting_id}\'".format(
            meeting_id = meeting.meeting_id,
            name = meeting.meeting_name,
            topic = meeting.meeting_topic,
            room_list = json.dumps(meeting.meeting_room_id),
            meeting_date = str(meeting.date),
            start_t = int(meeting.start_time),
            end_t = int(meeting.end_time),
            attendees = json.dumps(meeting.attendees),
            status = meeting.status,
            routine = meeting.is_routine,
            hw_requires = meeting.requires,
            site_json = json.dumps(meeting.sites),
            initiator = meeting.initiator,
        )
        self.Cursor.execute(sql)
        self.Database.commit()

    def site_list(self):
        sql = 'SELECT SiteID, SiteName FROM site'
        self.Cursor.execute(sql)
        result = self.Cursor.fetchall()
        keys = ['siteId', 'siteName']
        site_json = [dict(zip(keys, item)) for item in result]
        return site_json

    # return: (dict) attendees in site
    def selection_list_site(self, site_id):
        sql = 'SELECT EmployeeID, EmployeeName FROM employee WHERE SiteID = {}'.format(site_id)
        self.Cursor.execute(sql)
        result = self.Cursor.fetchall()
        keys = ['value', 'label']
        list_json = [dict(zip(keys, item)) for item in result]
        sql = 'SELECT SiteID, SiteName FROM site WHERE SiteID = {}'.format(site_id)
        self.Cursor.execute(sql)
        result = self.Cursor.fetchone()
        site_json = dict()
        site_json['value'] = result[0]
        site_json['label'] = result[1]
        site_json['children'] = list_json
        return site_json

    # return: (dict) attendees of a meeting
    def selection_list_history(self, meeting_id):
        sql = 'SELECT Attendee FROM meeting WHERE meetingID = \'{}\''.format(meeting_id)
        self.Cursor.execute(sql)
        result = json.loads(self.Cursor.fetchone()[0])
        list_json = [dict(zip(('value', 'label'), (item['id'], item['name']))) for item in result]
        site_json = {'value': 'history', 'label': 'Recent Selection', 'children': list_json}
        return site_json

    # return: (list of dict) attendees of all site and all past meeting
    def selection_list_meeting(self, employee):
        attendee_list = []
        for item in self.site_list():
            attendee_list.append(self.selection_list_site(item['siteId']))

        sql = 'SELECT JSON_EXTRACT(MeetingHistory, \'$.past\') FROM employee WHERE employeeID = \'%s\'' % employee
        self.Cursor.execute(sql)
        fetch_result = self.Cursor.fetchone()[0]
        if fetch_result:
            result = json.loads(fetch_result)
            item = result[0]
            attendee_list.append(self.selection_list_history(item))
        return attendee_list

    def meeting_history(self, employee_id):
        sql = 'SELECT MeetingHistory FROM employee WHERE employeeID = {}'.format(employee_id)
        self.Cursor.execute(sql)
        result = json.loads(self.Cursor.fetchone()[0])
        # print(result)
        list_meeting = '\'' + '\', \''.join(result) + '\''
        sql = 'SELECT MeetingID, Name, Status FROM meeting WHERE meetingID in ({})'.format(list_meeting)
        # print(sql)
        self.Cursor.execute(sql)
        result = self.Cursor.fetchall()
        return result

    def create_door_access(self, badge_id, employee_id, has_access):
        sql = 'INSERT INTO dooraccess(EmployeeID, BadgeID, Access) VALUES (%f, %f, %f)'
        data = (employee_id, badge_id, has_access)
        self.Cursor.execute(sql % data)
        self.Database.commit()
        result = self.Cursor.fetchall()
        print(result)

    def delete_door_access(self, employee_id):
        sql = 'DELETE FROM dooraccess WHERE EmployeeID = {}'.format(employee_id)
        self.Cursor.execute(sql)
        self.Database.commit()
        result = self.Cursor.fetchall()
        print(result)

    def update_door_access(self, badge_id, door_access):
        sql = 'UPDATE dooraccess SET Access = %f WHERE BadgeID = %f'
        data = (badge_id, door_access)
        self.Cursor.execute(sql % data)
        self.Database.commit()
        result = self.Cursor.fetchall()
        print(result)

    def get_door_access(self, employee_id):
        sql = 'SELECT door_access FROM dooraccess WHERE EmployeeID = %f'
        data = (employee_id)
        self.Cursor.execute(sql % data)
        result = self.Cursor.fetchall()
        print(result)
        return result

    def left_meeting_room(self, badge_id, geo_fence_id):
        sql = 'SELECT GEO_FENCE_ID FROM 20190801_pos_event_list WHERE BG_ID = %f'
        data = (badge_id)
        self.Cursor.execute(sql % data)
        result = self.Cursor.fetchall()[-1]
        print(result)
        if result != geo_fence_id:
            return True
        else:
            return False

    def badge_to_employee(self, badge_id):
        sql = 'SELECT EmployeeID FROM employee WHERE BG_ID = %f'
        data = (badge_id)
        self.Cursor.execute(sql % data)
        employee_id = self.Cursor.fetchall()
        print(result)
        return employee_id

    def check_if_has_access(self, employee_id):
        #check future meetings and get the latest one
        sql = 'SELECT MeetingHistory FROM employee WHERE EmployeeID = %f'
        data = employee_id
        self.Cursor.execute(sql % data)
        if MeetingHistory["present"] != []:
            target = MeetingHistory["present"][0]
        else:
            for mt_id in MeetingHistory["future"]:
                sql = 'SELECT MeetingID FROM meeting WHERE Date = {}'
                data = mt_id
                self.Cursor.execute(sql % data)
                result = self.Cursor.fetchall()

    def meeting_history(self, employee_id):
        sql = 'SELECT MeetingHistory FROM employee WHERE EmployeeID = {}'.format(employee_id)
        self.Cursor.execute(sql)
        result = json.loads(self.Cursor.fetchone()[0])
        print(result['past'])
        return_history = {'past': [], 'future': [], 'present': []}
        for i in result['past']:
            sql = 'SELECT * FROM meeting WHERE MeetingID = \'{}\''.format(i)
            self.Cursor.execute(sql)
            result2 = list(self.Cursor.fetchone())
            a = ['MeetingID', 'Name', 'MeetingTopic', 'MeetingRooms', 'Date', 'StartTime', 'EndTime', 'Attendee',
                 'Status', 'IsRoutine', 'Requires', 'Sites', 'Outline', 'Initiator', 'Memo']
            a = dict(zip(a, result2))
            return_history['past'].append(a)
        for i in result['present']:
            sql = 'SELECT * FROM meeting WHERE MeetingID = \'{}\''.format(i)
            self.Cursor.execute(sql)
            result2 = list(self.Cursor.fetchone())
            a = ['MeetingID', 'Name', 'MeetingTopic', 'MeetingRooms', 'Date', 'StartTime', 'EndTime', 'Attendee',
                 'Status', 'IsRoutine', 'Requires', 'Sites', 'Outline', 'Initiator', 'Memo']
            a = dict(zip(a, result2))
            return_history['present'].append(a)
        for i in result['future']:
            sql = 'SELECT * FROM meeting WHERE MeetingID = \'{}\''.format(i)
            self.Cursor.execute(sql)
            result2 = list(self.Cursor.fetchone())
            a = ['MeetingID', 'Name', 'MeetingTopic', 'MeetingRooms', 'Date', 'StartTime', 'EndTime', 'Attendee',
                 'Status', 'IsRoutine', 'Requires', 'Sites', 'Outline', 'Initiator', 'Memo']
            a = dict(zip(a, result2))
            return_history['future'].append(a)
        return return_history
