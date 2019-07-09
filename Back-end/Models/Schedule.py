#!/usr/bin/python3


class Schedule:
    def __init__(self):
        self.slots = {}

    def clear(self, date):
        del self.slots[date]