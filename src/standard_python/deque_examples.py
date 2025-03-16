"""
deque from collections module is a good and performant implementation of queue data structure.
"""
from collections import deque

def deque_examples():
    people_in_queue = deque(["Alice", "Bob", "Charlie"])
    print(people_in_queue)

    people_in_queue.append("Diana")
    people_in_queue.append("Eve")
    print(people_in_queue)

    print(people_in_queue.popleft())
    print(people_in_queue.popleft())
    print(people_in_queue.popleft())
    print(people_in_queue.popleft())

    print(people_in_queue)


if __name__ == '__main__':
    deque_examples()