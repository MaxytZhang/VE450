#import requests
#import re
#import json
#import urllib
headers = {}
x = y = 0
url = "http://localhost:8891/LBSCore/BadgeItems"
data = {"Method":"GetByIDs","Data":{"IDs":[4]}}
#html_post = requests.post(url = url,data = data,auth=('admin','admin'))
# html_get = requests.get(url = url, auth=('admin','admin'))
#html_post = requests.post(url = url,json = data,auth=('admin','admin'))
#x = html_post.json()[0]['Position']['X']
#while True:
#	html_post = requests.post(url = url,json = data,auth=('admin','admin'))
#	if x != html_post.json()[0]['Position']['X']:
#		break
#	x = html_post.json()[0]['Position']['X']
#
#old_fence = 0
#flag = True
#while True:
#	html_post = requests.post(url = url,json = data,auth=('admin','admin'))
#	if flag == True and html_post.json()[0]['Position']['GEO_FENCE_ID'] in [5, 6, 7]:
#		flag = False
#		print('Access Granted.')
#	if html_post.json()[0]['Position']['GEO_FENCE_ID'] == 5 and old_fence !=5:
#		print('In Region.')
#	if html_post.json()[0]['Position']['GEO_FENCE_ID'] != 5 and old_fence == 5:
#		print('Leave Region.')
#		flag = True
#	old_fence = html_post.json()[0]['Position']['GEO_FENCE_ID']
import time
start = time.clock()
flag = 0
while True:
	end = time.clock()
	if (end - start) > 7 and flag == 0:
		print('Access Granted.')
		flag = 1
	if (end - start) > 9 and flag == 1:
		flag = 2
		print('In Region')
	if (end - start) > 17 and flag == 2:
		print('Leave Region')
		flag = 3