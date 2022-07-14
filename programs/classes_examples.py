class Queue(object):
    count = 0
    def __init__(self,name):
        self.name = name
        self._queue = []
        Queue.count += 1
    def push(self,obj):
        self._queue.append(obj)

    def pop(self):
        return self._queue.pop(0)

print(Queue.count)
q1 = Queue("q1")
print(Queue.count)
q2 = Queue("q2")
print(Queue.count)
print(value = q1.count)