#!/usr/bin/python3

class Task():
    def __init__(self, name, priority = 'low'):
        self.name = name
        self.__priority = priority

        @property
        def priority(self):
            return self.__priority
        
        @priority.setter
        def priority(self, value):
            self.priority = value

        def __str__(self):
            return f"{self.__name} {self.__priority}"
        def __repr__(self):
            return f"{self.__name} {self.__priority}"
        