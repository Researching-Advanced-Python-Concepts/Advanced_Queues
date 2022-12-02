from collections import deque
from priority_queues.queues import IterableMixin


class Queue(IterableMixin):
    def __init__(self, *elements) -> None:
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


if __name__ == "__main__":

    fifo = Queue()
    fifo.enqueue("1st")
    fifo.enqueue("2nd")
    fifo.enqueue("3rd")
    fifo.enqueue("4th")
    fifo.enqueue("5th")

    print(fifo._elements)

    print(fifo.dequeue())
    print(fifo.dequeue())
    print(fifo.dequeue())
    print(fifo._elements)

    for i in fifo:
        print(i)
