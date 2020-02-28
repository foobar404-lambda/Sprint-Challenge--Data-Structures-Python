from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.old = None

    def append(self, item):
        if len(self.storage) >= self.capacity:
            if not self.old:
                self.old = self.storage.head
            self.storage.replace(self.old, item)
            self.old = self.old.next
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head

        while node:

            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# buff = RingBuffer(4)

# buff.append(1)
# buff.append(2)
# buff.append(3)
# buff.append(4)
# buff.append(5)
# buff.append(6)
# buff.append(7)
# buff.append(8)
# buff.append(9)


# print(buff.get())
