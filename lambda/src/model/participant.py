import json


class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email

    def __hash__(self):
        return id(self)

    def __getitem__(self, property):
        return getattr(self, property)
