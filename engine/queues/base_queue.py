class BaseQueue(object):
    def __init__(self, name):
        self.name = name

    def put(self, data):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def get_queue_size(self):
        raise NotImplementedError
