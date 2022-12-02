from queues import Queue


class Stack(Queue):
    # not necessarily the correct inheritance just for convenience
    def dequeue(self):
        return self._elements.pop()


lifo = Stack()
lifo.enqueue("1st")
lifo.enqueue("2nd")
lifo.enqueue("3rd")
lifo.enqueue("4th")
lifo.enqueue("5th")

print(lifo._elements)

print(lifo.dequeue())
print(lifo.dequeue())
print(lifo.dequeue())
print(lifo._elements)

for i in lifo:
    print(i)
