import unittest
from engine.listeners import base_listener
from engine.listeners import jenkins_zmq_listener
from engine.queues import queue_factory
import zmq
import time


class JenkinsZMQListenerTestRunner(unittest.TestCase):
    def setUp(self):
        self.zmq_addr = 'tcp://127.0.0.1:5555'

        # self.context = zmq.Context()
        # self.socket = self.context.socket(zmq.PUB)
        # self.socket.bind(self.zmq_addr)
        #
        # self.queue = queue_factory.QueueFactory.create_inmemory_queue('test_queue')
        # self.listener = jenkins_zmq_listener.JenkinsZMQListener('test listener', self.zmq_addr, self.queue)
        # self.listener.start()
        # msg = 'test message'
        # self.socket.send_string(msg)

    def test_recv(self):
        queue = queue_factory.QueueFactory.create_inmemory_queue('test_queue')
        listener = jenkins_zmq_listener.JenkinsZMQListener('test listener', self.zmq_addr,queue)
        listener.start()
        time.sleep(3)
        msg = 'test message'
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind(self.zmq_addr)
        socket.send_string(msg)

        time.sleep(3)
        listener.stop()
        context.destroy()

        self.assertEqual(queue.get_queue_size(), 1)

    def tearDown(self):
        pass

