import requests
import re
import json
import urllib
import datetime
from Models.DatabaseOperator import DatabaseOperator as DB


def convert_pytime(time):
    return time.hour * 4 + time.minute / 15


badge_id = 2;
db = DB()
employee_id = db.badge_to_employee(badge_id)
print(employee_id)
currentT = datetime.datetime.now()
current_date = currentT.date()
current_time = convert_pytime(currentT.time())
has_access = db.check_if_has_access(employee_id, current_date, current_time)



if has_access != 0:
    db.create_door_access(badge_id, employee_id, has_access)
    x = y = 0
    url = "http://localhost:8891/LBSCore/BadgeItems"
    data = {"Method": "GetByIDs", "Data": {"IDs": [badge_id]}}
    html_post = requests.post(url = url, json = data, auth = ('admin', 'admin'))
    x = html_post.json()[0]['Position']['X']
    while True:
        html_post = requests.post(url = url, json = data, auth = ('admin', 'admin'))
        if x != html_post.json()[0]['Position']['X']:
            break
        x = html_post.json()[0]['Position']['X']

    old_fence = 0
    flag = True
    while True:
        html_post = requests.post(url = url, json = data, auth = ('admin', 'admin'))
        if flag == True and html_post.json()[0]['Position']['GEO_FENCE_ID'] in [5, 6, 7]:
            flag = False
            #print('Access Granted.')
            db.update_door_access(badge_id, 2)
        if html_post.json()[0]['Position']['GEO_FENCE_ID'] == 5 and old_fence != 5:
            #print('In Region.')
            db.delete_door_access(employee_id)
        if html_post.json()[0]['Position']['GEO_FENCE_ID'] != 5 and old_fence == 5:
            #print('Leave Region.')
            flag = True
        old_fence = html_post.json()[0]['Position']['GEO_FENCE_ID']
