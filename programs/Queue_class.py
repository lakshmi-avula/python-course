class Queue(object):
    def __init__(self, name):
        self.name = name
        self._queue = []

    def push(self, obj):
        self._queue.append(obj)

    def pop(self):
        return self._queue.pop


q1 = Queue("q1")
q1_push = q1.push
print(Queue.push.__self__)