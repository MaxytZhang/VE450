#!/usr/bin/python3
import datetime


class Meeting:
    def __init__(self, meeting_id, meeting_name, meeting_topic, meeting_room_id, start_time, end_time, is_routine,
                 requires):
        self.id = meeting_id
        self.meeting_name = meeting_name
        self.meeting_topic = meeting_topic
        self.meeting_room_id = meeting_room_id
        self.date = datetime.date
        self.start_time = start_time
        self.end_time = end_time
        self.attendees = []
        self.priority = 0
        self.status = -1
        self.is_routine = is_routine
        self.requires = requires
        self.sites = []

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
                my_meeting_room = meeting_room_list[room_id]
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

    def recommend(self):
        site_attendees = {}

        # Count the number of people in each site
        for member in self.attendees:
            if member['site'] in site_attendees:
                site_attendees[member['site']] += 1
            else:
                site_attendees[member['site']] = 1

        site_recommend_list = {}
        for site_id in self.sites:
            site_recommend_list[site_id] = []
            for room_id in meeting_room_list[site_id]:
                if room_id.meet_requirements(len(site_attendees[site_id]), self.requires, self.start_time,
                                             self.end_time):
                    site_recommend_list[site_id].append(room_id.id)
        return site_recommend_list

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
