class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_data -= 1

        return pop_data

    def first(self):
        if self.num_of_data == 0:
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data

    def cnt(self):
        return self.current.data


if __name__ == '__main__':
    link = Linkedlist()
    link.append(1)
    link.append(2)
    link.append(3)
    link.append(4)
    link.append(5)

    print(link.first())
    print(link.next())
    print(link.delete())
    print(link.cnt())
    print(link.tail.data)

    data = link.first()
    print('----')
    for _ in range(link.num_of_data):
        print(data)
        data = link.next()

    print(link.cnt())