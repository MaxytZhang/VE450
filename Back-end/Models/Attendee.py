#!/usr/bin/python3


class Attendee:
    def __init__(self, attendee_id, status, feedback, role, site):
        self.id = attendee_id
        self.status = status
        self.feedback = feedback
        self.role = role
        #self.file = []
        self.site = site

    def get_feedback(self, feedback):
        self.feedback = feedback
