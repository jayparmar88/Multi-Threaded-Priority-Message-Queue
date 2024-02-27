import queue
import threading

class PriorityMessageQueue:
    def __init__(self):
        self.queue_lock = threading.Lock()
        self.message_queue = queue.PriorityQueue()

    def enqueue_message(self, message, priority):
        with self.queue_lock:
            self.message_queue.put((priority, message))

    def dequeue_message(self):
        with self.queue_lock:
            if not self.message_queue.empty():
                return self.message_queue.get()[1]
            return None

    def peek_message(self):
        with self.queue_lock:
            if not self.message_queue.empty():
                return self.message_queue.queue[0][1]
            return None

    def is_empty(self):
        with self.queue_lock:
            return self.message_queue.empty()