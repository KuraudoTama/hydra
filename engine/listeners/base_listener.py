import threading


class BaseListener(threading.Thread):
    def __init__(self, name, queue=None):
        threading.Thread.__init__(self, name=name)
        self._queue = queue
        self._stopped = False

    def set_queue(self, queue):
        self._queue = queue

    def run(self):
        raise NotImplementedError

    def listen(self):
        raise NotImplementedError

    def stop(self):
        self._stopped = True
