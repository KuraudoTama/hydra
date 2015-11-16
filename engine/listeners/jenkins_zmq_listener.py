import zmq
from base_listener import BaseListener


class JenkinsZMQListener(BaseListener):
    def __init__(self, name, zmq_address, queue=None):
        BaseListener.__init__(self, name, queue)
        self.zmq_address = zmq_address
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)

    def run(self):
        self._setup_socket()
        while not self._stopped:
            self.listen()

    def stop(self):
        self._stopped = True
        if self._context:
            self._context.destroy()

    def listen(self):
        try:
            event = self._socket.recv()
            self._queue.put(event)
        except:
            if not self._stopped:
                self.stop()

    def _setup_socket(self):
        self._socket.connect(self.zmq_address)
        self._socket.setsockopt(zmq.SUBSCRIBE, '')
