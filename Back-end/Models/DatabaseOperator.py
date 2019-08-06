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
        sql = 'select * from gdm64397110_db.employee where EmployeeName = "{}" and Password = {}'.format(user['name'],
                                                                                                         user[
                                                                                                             'password'])
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
            attendees = json.dumps(meeting.attendees),
            room_list = json.dumps(meeting.meeting_room_id),
            start_t = meeting.start_time,
            end_t = meeting.end_time,
            status = meeting.status,
            routine = meeting.is_routine,
            hw_requires = meeting.requires,
            initiator = meeting.initiator,
            meeting_date = str(meeting.date),
            site_json = json.dumps(meeting.sites)
        )
        self.Cursor.execute(sql)
        self.Database.commit()

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

    def selection_list_history(self, meeting_id):
        sql = 'SELECT Attendee FROM meeting WHERE meetingID = \'{}\''.format(meeting_id)
        self.Cursor.execute(sql)
        result = json.loads(self.Cursor.fetchone()[0])
        list_json = [dict(zip(('value', 'label'), (item['id'], item['name']))) for item in result]
        site_json = {'value': 'history', 'label': 'Recent Selection', 'children': list_json}
        return site_json

    def selection_list_meeting(self, employee):
        sql = 'SELECT JSON_EXTRACT(MeetingHistory, \'$.past\') FROM employee WHERE employeeID = \'%s\'' % employee
        self.Cursor.execute(sql)
        result = json.loads(self.Cursor.fetchone()[0])
        history = []
        for item in result:
            history.append(self.selection_list_history(item))
        return history

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
        print(result)

    def create_door_access(self, badge_id, employee_id, has_access):
        sql = 'INSERT INTO dooraccess(EmployeeID, BadgeID, Access) VALUES (employee_id, badge_id, has_access)'
        self.Cursor.execute(sql)
        self.Database.commit()
        result = self.Cursor.fetchall()
        print(result)

    def update_door_access(self, badge_id, door_access):
        sql = 'UPDATE dooraccess SET Access = door_access WHERE BadgeID = badge_id'
        self.Cursor.execute(sql)
        self.Database.commit()
        result = self.Cursor.fetchall()
        print(result)

    def get_door_access(self, employee_id):
        sql = 'SELECT door_access FROM dooraccess WHERE EmployeeID = {}'.format(employee_id)
        self.Cursor.execute(sql)
        result = self.Cursor.fetchall()
        print(result)


