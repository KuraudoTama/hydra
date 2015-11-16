from six.moves import queue

from base_queue import BaseQueue


class InMemoryQueue(BaseQueue):
    def __init__(self, name):
        BaseQueue.__init__(self, name)
        self._queue = queue.Queue()

    def put(self, data):
        self._queue.put(data)

    def get(self):
        return self._queue.get()

    def is_empty(self):
        return self._queue.empty()

    def get_queue_size(self):
        return self._queue.qsize()
