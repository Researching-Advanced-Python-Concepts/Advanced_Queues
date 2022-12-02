from heapq import heappop, heappush
from itertools import count
from dataclasses import dataclass


class IterableMixin:
    # mixin aren't useful by their own
    # but can be used with unrelated classes by taking out
    # the least common denominator
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()


class PriorityQueue(IterableMixin):
    def __init__(self) -> None:
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        # python compares tuples element-wise
        # heap is min-heap so putting -ve works
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]


@dataclass
class Message:
    # out of the box allows: instantiate, print and compare data class
    # instances
    event: str


CRITICAL = 3
IMPORTANT = 2
NORMAL = 1

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")
brakes = Message("Brake pedal depressed")

messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, brakes)
messages.enqueue_with_priority(IMPORTANT, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)
messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))


print(messages._elements)
for msg in messages:
    print(msg.event)
