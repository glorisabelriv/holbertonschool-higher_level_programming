#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = 0
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

    def get_count(self):
        return self.counter
