import threading

class MessageSender:
    def __init__(self, message_queue, thread_pool):
        self.message_queue = message_queue
        self.thread_pool = thread_pool

    def send_message(self, message, priority, target_thread):
        self.message_queue.enqueue_message(message, priority)
        if target_thread in self.thread_pool.running_threads:
            self.thread_pool.notify_thread(target_thread)