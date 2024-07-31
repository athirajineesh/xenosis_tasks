
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


List = [3,5,2,1,7]
sorted_numbers = bubble_sort(List)
print(sorted_numbers)
List1= [5,3,9,2,0]
insertion = insertion_sort(List1)
print(insertion)
List2=[32,89,76,54,65]
quick_sorted = insertion_sort(List2)
print(quick_sorted)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


def main():
    # Create a linked list
    ll = LinkedList()

    # Insert some nodes
    ll.insert(16)
    ll.insert(87)
    ll.insert(98)
    ll.insert(54)

    print("Linked List after inserts:")
    ll.traverse()

    # Delete a node
    ll.delete(87)

    print("Linked List after deleting 20:")
    ll.traverse()


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def main():
    # Create a stack
    s = Stack()

    # Push some elements
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack after pushes:")
    print("Top element (peek):", s.peek())
    print("Stack size:", s.size())

    # Pop an element
    print("Popped element:", s.pop())

    print("Stack after pop:")
    print("Top element (peek):", s.peek())
    print("Stack size:", s.size())

    # Check if stack is empty
    print("Is stack empty?", s.is_empty())

    # Pop remaining elements
    s.pop()
    s.pop()

    print("Stack after popping all elements:")
    print("Is stack empty?", s.is_empty())



main()


