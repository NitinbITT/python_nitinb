class Queue:
    def __init__(self):
        self._list1 = []

    def enqueue(self, element):
        self._list1.append(element)

    def dequeue(self):
        if self.is_empty():
            return self._list1.pop(0)
        else:
            print("Queue is empty")

    def is_empty(self):
        if len(self._list1) == 0:
            return True
        return False

    def __str__(self):
        return_string = ""
        for value in self._list1:
            return_string += str(value) + "\n"
        return f"\n{return_string}"


queue1 = Queue()

queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
queue1.enqueue(40)
queue1.enqueue(50)
print("Current Queue:", queue1)
print("Dequeued item:", queue1.dequeue())
print("Dequeued item:", queue1.dequeue())
print("Updated Queue:", queue1)
