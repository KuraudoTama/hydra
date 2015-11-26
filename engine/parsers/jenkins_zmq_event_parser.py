import json
from base_parser import BaseParser


class JenkinsZMQEventParser(BaseParser):
    def __init__(self, name, queue_in, queue_out):
        BaseParser.__init__(self, name, queue_in, queue_out)
        self._event_source = 'jenkins_zmq'

    def run(self):
        while not self._stopped:
            self.parse()

    def parse(self):
        event_origin = self._queue_in.get()
        event_type = event_origin.split(None)[0]
        event_data = json.loads(event_origin.lstrip(event_type).lstrip())
        event_parsed = {'event_source': self._event_source, 'event_type': event_type, 'event_data': event_data}
        self._queue_out.put(event_parsed)

