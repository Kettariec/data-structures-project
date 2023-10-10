import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    """тест класса Node"""
    def test_node(self):
        node1 = Node(5, None)
        node2 = Node('test', node1)
        self.assertEqual(node1.data, 5)
        self.assertEqual(node2.data, 'test')
        self.assertEqual(node1.next_node, None)
        self.assertEqual(node2.next_node, node1)
        self.assertIsInstance(node1, Node)
        self.assertIsInstance(node1.data, int)
        self.assertIsInstance(node2.data, str)

    def test_stack_push(self):
        """тест push класса Stack"""
        stack = Stack()
        stack.push('test1')
        stack.push('test2')
        stack.push('test3')
        self.assertEqual(stack.top.data, 'test3')
        self.assertEqual(stack.top.next_node.data, 'test2')
        self.assertEqual(stack.top.next_node.next_node.data, 'test1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.next_node.data
