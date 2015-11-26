from queues.queue_factory import QueueFactory
from listeners.jenkins_zmq_listener import JenkinsZMQListener
from parsers.jenkins_zmq_event_parser import JenkinsZMQEventParser
import time
import sys



queue_in = QueueFactory.create_inmemory_queue('queue_in')
queue_out = QueueFactory.create_inmemory_queue('queue_out')

zmq_addr = 'tcp://9.114.104.210:5555'

listener = JenkinsZMQListener('jenkins_zmq_listener', zmq_addr, queue_in)
listener.start()

parser = JenkinsZMQEventParser('jenkins_zmq_parser', queue_in, queue_out)
parser.start()


# while True:
#     elem = queue_out.get()
#     print elem
#     sys.stdout.flush()


parser.stop()
listener.stop()

