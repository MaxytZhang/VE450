#!/usr/bin/python3


class Site:
    def __init__(self, name, meeting_room):
        self.name = name
        self.meeting_room = meeting_room

    def get_room_list(self):
        return self.meeting_room
