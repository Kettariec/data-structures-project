class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f'first:{self.data} next:{self.next_node}'


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.all_nodes = ''

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        # Если нет ни одного узла
        if self.head is None:
            self.head = Node(data, None)
            self.all_nodes += f'{self.head.data}'
        # Если только один элемент
        elif self.tail is None and self.head:
            new_node = Node(data, None)
            self.head.next_node = new_node
            self.tail = new_node
            self.all_nodes += f'\n{self.tail.data}'
        else:
            new_node = Node(data, None)
            self.tail.next_node = new_node
            self.tail = new_node
            self.all_nodes += f'\n{self.tail.data}'

    def dequeue(self):
        """
        Метод для удаления элемента из очереди.

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            del_node = self.head
            self.head = self.head.next_node
            return del_node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return f'{self.all_nodes}'
