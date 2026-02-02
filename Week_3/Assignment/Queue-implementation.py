class Queue:
    def __init__(self):
        self.__list1 = []

    def enqueue(self, element):
        self.__list1.append(element)

    def dequeue(self):
        try:
            return self.__list1.pop(0)
        except:
            print("End of Queue")

    def __str__(self):
        return f"{self.__list1}"


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
