from six.moves import queue


class InMemoryQueue(object):
    def __init__(self, name):
        self.name = name
        self._queue = queue.Queue()

    def put(self, data):
        self._queue.put(data)

    def get(self):
        return self._queue.get()

    def is_empty(self):
        return self._queue.empty()

    def get_queue_size(self):
        return self._queue.qsize()
