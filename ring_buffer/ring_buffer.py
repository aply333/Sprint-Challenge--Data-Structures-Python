class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None

    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        if not self.head.next:
            new_node.next = self.head
            self.head.next = new_node
        else:
            count = 1
            current = self.head
            while current.next != self.head:
                print(count)
                count += 1
                current = current.next
            print(f"Final Count {count}")
            if count < self.capacity:
                new_node.next = self.head
                current.next = new_node
            else:
                current.next = new_node
                new_node.next = self.head.next
                self.head = self.head.next

    def get(self):
        current = self.head
        current_list = []
        while current:
            current_list.append(current.value)
            current = current.next
            if current == self.head:
                break
        return current_list

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.volume = 0
#         self.head = None

#     def append(self, item):
#         new_node = Node(item)
#         if self.volume == 0:
#             self.volume += 1
#             new_node.next = new_node
#             self.head = new_node
#         elif 0 < self.volume < self.capacity:
#             self.volume += 1
#             current = self.head
#             while current.next != self.head:
#                 current = current.next
#             new_node.next = self.head
#             current.next = new_node
#         else:
#             new_node.next = self.head.next
#             self.head = new_node

#     def get(self):
#         current = self.head.next
#         current_list = []
#         current_list.append(self.head.value)
#         while current.next != self.head:
#             current_list.append(current.value)
#             current = current.next 
#         return current_list