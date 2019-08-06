import pymysql
import datetime, time


if __name__ == '__main__':
	db2 = pymysql.connect(
		host='localhost',
		port=3306,
		user='root',
		passwd='123123',
		db='lbs_db',
		charset='utf8'
		)
	cursor2 = db2.cursor()
	cursor2.execute('select * from 20190801_pos_event_list')
	result2 = cursor2.fetchall()

	db = pymysql.connect(
		host='gdm64397110.my3w.com',
		port=3306,
		user='gdm64397110',
		passwd='VE450Team7',
		db='gdm64397110_db',
		charset='utf8mb4'
		)
	cursor = db.cursor()
	sql_text = "INSERT INTO 20190801_pos_event_list values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %f, %f, %s, %s, %s, %s)"
	cursor.execute(sql_text,result2)
	db.commit()