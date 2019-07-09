#!/usr/bin/python3
import datetime


class MeetingRoom:
    def __init__(self, id, location, size, capacity, occupancy, remote, hardware):
        self.id = id
        self.location = location
        self.size = size
        self.capacity = capacity
        self.occupancy = occupancy
        self.remote = remote
        self.schedule = {}
        self.hardware = hardware

    @property
    def is_empty(self):
        return self.occupancy

    @staticmethod
    def open_door(self, employee):
        if employee.id in get_meeting_attendees(self.schedule[len(self.schedule) - 1][0]):
            return True
        else:
            return False

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
        if number <= self.size and requires < self.hardware:
            for time_id in self.schedule[date][start_time:end_time]:
                if time_id != 0:
                    return False
            return True
        return False
