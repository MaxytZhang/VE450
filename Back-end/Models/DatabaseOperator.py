import pymysql

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

    def close(self):
        self.Cursor.close()
        self.Database.close()

    def validate(self, user):
        print(user)
        sql = 'select * from gdm64397110_db.employee where EmployeeName = "{}" and Password = {}'.format(user['name'], user['password'])
        print(sql)
        res = self.Cursor.execute(sql)
        info = self.Cursor.fetchone()
        print(info)
        return res, info
