#write a function to perform counting sort
def countingSort(arr):
    max_element = int(max(arr))
    count_arr = [0 for _ in range(max_element + 1)]
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    output_arr = [0 for i in range(len(arr))]
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    for i in range(len(arr)):
        arr[i] = output_arr[i]
    return arr

#Linked List implementation from scratch
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self, head:Node):
        self.head = head
        self.size = 0
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def remove_node(self, data: int|float):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False
    
    def insert_start(self, data:int|float):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def remove_start(self)->Node:
        current = self.head
        self.head = current.next
        self.size -= 1
        return current
    
    def insert_at_index(self, index: int, data: int | float):
        if index == 0:
            self.insert_start(data)
        elif index >= self.size:
            self.insert(data)
        else:
            new_node = Node(data)
            current = self.head
            previous = None
            for _ in range(index):
                previous = current
                current = current.next
            previous.next = new_node
            new_node.next = current
            self.size += 1
    


if __name__=='__main__':
    arr = [1, 4, 1, 2, 7, 5, 2]
    print(countingSort(arr))