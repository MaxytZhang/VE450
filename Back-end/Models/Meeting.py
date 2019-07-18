#!/usr/bin/python3
import datetime
import json

class Meeting:
    def __init__(self):
        self.id = -1
        self.meeting_name = ''
        self.meeting_topic = ''
        self.meeting_room_id = {}
        self.date = datetime.date
        self.start_time = 1911653999
        self.end_time = 1911653999
        self.attendees = {}
        self.priority = 0
        self.status = -1  # before, during, after
        self.is_routine = False
        self.requires = False
        self.sites = []
        self.outline = []  # list of strings
        self.initiator = 450
        self.memo = {}

    @staticmethod
    def reminder(self):
        for attendees in self.attendees:
            send_reminder(attendees.id)

    def memo(self):
        for attendees in self.attendees:
            send_memo(attendees.id)

    def outline(self):
        for attendees in self.attendees:
            send_outline(attendees.id)

    @staticmethod
    def release(self, button_pressed, room_is_empty):
        if button_pressed:
            for room_id in self.meeting_room_id:
                my_meeting_room = meeting_room_list[self.meeting_room_id[room_id]]
                my_meeting_room.occupancy = False
                if self.end_time != current_time:
                    my_meeting_room.change_schedule(self.id, current_time)
        else:
            for empty_id in range(len(room_is_empty)):
                if empty_id:
                    my_meeting_room = meeting_room_list[self.meeting_room_id[empty_id]]
                    my_meeting_room.occupancy = False
                    if self.end_time != current_time:
                        my_meeting_room.change_schedule(self.id, current_time)
        self.end_time = current_time

    def recommend(self, meeting_room_list, site_list):
        site_attendees = {}

        # Count the number of people in each site
        for member in self.attendees:
            if self.attendees[member]['site'] in site_attendees:
                site_attendees[self.attendees[member]['site']] += 1
            else:
                site_attendees[self.attendees[member]['site']] = 1
        for site_id in site_attendees:
            print('' + str(site_attendees[site_id]) + ' people in site ' + str(site_id) + ' need to attend the meeting.')

        site_recommend_list = {}
        limitation_flag = False  # see if the solution can be find
        for site_id in self.sites:
            site_recommend_list[site_id] = []
            for room_id in site_list[site_id-1]['meetingRoom']:
                # if room_id.meet_requirements(len(site_attendees[site_id]), self.requires, self.start_time,
                #                              self.end_time):
                #     site_recommend_list[site_id].append(room_id.id)
                if meeting_room_list[room_id]['hardware'] == 1 and meeting_room_list[room_id]['capacity'] >= site_attendees[site_id]:
                    site_recommend_list[site_id].append(meeting_room_list[room_id]['id'])
            if not site_recommend_list[site_id]:
                print('\nThere\'s no meeting room available for site ' + str(site_id))
                limitation_flag = True

        # if no recommendation, try again without capacity restriction
        if limitation_flag:
            for site_id in self.sites:
                if site_recommend_list[site_id] == []:
                    room_flag = ''
                    for room_id in site_list[site_id-1]['meetingRoom']:
                        # if room_id.meet_requirements(0, self.requires, self.start_time,
                        #                              self.end_time):
                        #     site_recommend_list[site_id].append(room_id.id)
                        if meeting_room_list[room_id]['hardware'] == 1 and meeting_room_list[room_id]['capacity'] >= 0:
                            if room_flag == '':
                                room_flag = room_id
                            else:
                                if meeting_room_list[room_id]['capacity'] > meeting_room_list[room_flag]['capacity']:
                                    room_flag = room_id
                    site_recommend_list[site_id].append(meeting_room_list[room_flag]['id'])
                    if not site_recommend_list[site_id]:
                        return {}, True
        return site_recommend_list, limitation_flag

    def modify(self, meeting_name, meeting_topic, date, start_time, end_time, attendees, is_routine):
        flag = self.start_time == start_time and self.end_time == end_time and self.attendees == attendees
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_name = meeting_name
        self.meeting_topic = meeting_topic
        self.date = date
        self.attendees = attendees
        self.is_routine = is_routine
        if flag:
            self.release(True, [])
            self.recommend()

    def extend(self, extend_time):
        for room_id in meeting_room_id:
            if not meeting_room_list[room_id].meet_requirements(0, False, self.end_time, self.end_time + extend_time):
                return False
        for room_id in meeting_room_id:
            meeting_room_list[room_id].set_schedule(self.id, self.end_time, self.end_time + extend_time)
        self.end_time = self.end_time + extend_time
        return True
