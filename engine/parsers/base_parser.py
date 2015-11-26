import threading


class BaseParser(threading.Thread):
    def __init__(self, name, queue_in, queue_out):
        threading.Thread.__init__(self, name=name)
        self._queue_in = queue_in
        self._queue_out = queue_out
        self._stopped = False

    def set_queue_in(self, queue_in):
        self._queue_in = queue_in

    def set_queue_out(self, queue_out):
        self._queue_out = queue_out

    def run(self):
        raise NotImplementedError

    def stop(self):
        self._stopped = True

    def parse(self):
        raise NotImplementedError
