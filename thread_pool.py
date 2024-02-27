import threading
from concurrent.futures import ThreadPoolExecutor

class ThreadPool:
    def __init__(self, num_threads):
        self.executor = ThreadPoolExecutor(max_workers=num_threads)
        self.thread_condition = threading.Condition()
        self.running_threads = set()
        self.exit_flag = False

    def submit_task(self, task, *args):
        with self.thread_condition:
            if self.exit_flag:
                return None  # Gracefully ignore new tasks if the thread pool is shutting down
            future = self.executor.submit(task, *args)
            future.add_done_callback(lambda future: self.notify_all_waiting_threads())
            return future

    def notify_all_waiting_threads(self):
        with self.thread_condition:
            self.thread_condition.notify_all()

    def sleep_thread(self, thread_id):
        with self.thread_condition:
            while thread_id in self.running_threads:
                self.running_threads.remove(thread_id)
                self.thread_condition.wait()

    def notify_thread(self, thread_id):
        with self.thread_condition:
            self.running_threads.add(thread_id)
            self.thread_condition.notify()

    def shutdown(self):
        with self.thread_condition:
            self.exit_flag = True
            self.thread_condition.notify_all()
        self.executor.shutdown()