import unittest
from engine.queues.queue_factory import QueueFactory
from engine.parsers.jenkins_zmq_event_parser import JenkinsZMQEventParser
import time

class JenkinsZMQEventParserTestRunner(unittest.TestCase):
    def setUp(self):
        self.queue_in = QueueFactory.create_inmemory_queue('queue_in')
        self.queue_out = QueueFactory.create_inmemory_queue('queue_out')
        self.parser = JenkinsZMQEventParser('parser', self.queue_in, self.queue_out)

    def test_parse(self):
        event = 'onCompleted {"name":"Execute_Foodcritic","url":"job/Execute_Foodcritic/",\
              "build":{"full_url":"http://172.16.1.7:8080/job/Execute_Foodcritic/462/",\
              "number":462,"phase":"COMPLETED","status":"FAILURE","url":"job/Execute_Foodcritic/462/",\
              "parameters":{"COOKBOOK_PATHS":"","SLI_DEV_BUILD_TO_DEPLOY":\
              "http://172.16.1.7:8080/job/Handle_SLI_Dev_Build_Published/7023/"},\
              "node_name":"","host_name":"192.168.122.1"}}'

        self.parser.start()
        self.queue_in.put(event)
        time.sleep(3)
        self.parser.stop()
        self.assertEqual(1,self.queue_out.get_queue_size())
