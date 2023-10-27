class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.data_list = []

    def insert_beginning(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел
        с этими данными в начало связанного списка
        """
        new_node = Node(data, self.head)
        self.head = new_node
        self.data_list.insert(0, data)

    def insert_at_end(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел
        с этими данными в конец связанного списка
        """
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node:
                if node.next_node is None:
                    node.next_node = Node(data)
                    break
                node = node.next_node
        self.data_list.append(data)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        return self.data_list

    def get_data_by_id(self, mean_id):
        for data in self.data_list:
            try:
                for key, item in data.items():
                    if key == 'id' and item == mean_id:
                        return data
            except AttributeError:
                print("Данные не являются словарем или в словаре нет id.")
