import unittest
from src.queue import Node, Queue


class TestQueue(unittest.TestCase):
    def test_node(self):
        """тест класса Node"""
        node1 = Node(5, None)
        self.assertEqual(node1.data, 5)
        self.assertEqual(node1.next_node, None)
        self.assertIsInstance(node1, Node)
        self.assertIsInstance(node1.data, int)

    def test_enqueue(self):
        """тест push класса Queue"""
        new_queue = Queue()
        self.assertEqual(new_queue.__str__(), '')
        new_queue.enqueue('data1')
        new_queue.enqueue('data2')
        self.assertEqual(new_queue.head.data, 'data1')
        self.assertEqual(new_queue.head.next_node.data, 'data2')

    def test_str(self):
        test_stack = Queue()
        self.assertEqual(test_stack.__str__(), test_stack.all_nodes)
