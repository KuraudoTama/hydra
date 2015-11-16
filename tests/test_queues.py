import unittest

from engine.queues import inmemory_queue
from engine.queues import queue_factory


class InMemoryQueueTestRunner(unittest.TestCase):
    def setUp(self):
        self.queue_name = 'in-memory queue'
        self.queue = queue_factory.QueueFactory.create_inmemory_queue(self.queue_name)

    def test_create_inmemory_queue(self):
        assert self.queue.name == self.queue_name
        assert self.queue.__class__ == inmemory_queue.InMemoryQueue
        self.assertTrue(self.queue.is_empty(), 'The queue is not initialized as empty')

    def test_inmemory_queue_put(self):
        size_before = self.queue.get_queue_size()
        self.queue.put('data 1')
        size_after = self.queue.get_queue_size()
        self.assertEqual(size_after - size_before, 1, 'Incorrect queue size')

    def test_inmemory_queue_get(self):
        testdata = 'testdata'
        self.queue.put(testdata)
        size_before = self.queue.get_queue_size()
        data = self.queue.get()
        size_after = self.queue.get_queue_size()
        self.assertEqual(data, testdata, 'Incorrect queue data')
        self.assertEqual(size_before - size_after, 1, 'Incorrect queue size')

