import unittest
from src.linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):
    def test_node(self):
        """тест класса Node"""
        node1 = Node(5, None)
        self.assertEqual(node1.data, 5)
        self.assertEqual(node1.next_node, None)
        self.assertIsInstance(node1, Node)
        self.assertIsInstance(node1.data, int)

    def test_insert_beginning(self):
        """тесты класса LinkedList"""
        new_list = LinkedList()
        new_list.insert_beginning('data1')
        new_list.insert_beginning('data2')
        self.assertEqual(new_list.head.data, 'data2')
        self.assertEqual(new_list.head.next_node.data, 'data1')

    def test_insert_at_end(self):
        new_list = LinkedList()
        new_list.insert_at_end('data1')
        new_list.insert_at_end('data2')
        self.assertEqual(new_list.head.data, 'data1')
        self.assertEqual(new_list.head.next_node.data, 'data2')

    def test_str(self):
        new_list = LinkedList()
        self.assertEqual(new_list.__str__(), 'None')
        new_list.insert_beginning('data1')
        new_list.insert_beginning('data2')
        self.assertEqual(new_list.__str__(), 'data2 -> data1 -> None')
