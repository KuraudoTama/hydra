from inmemory_queue import InMemoryQueue


class QueueFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def create_inmemory_queue(name):
        return InMemoryQueue(name)
