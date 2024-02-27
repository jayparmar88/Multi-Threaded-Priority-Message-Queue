import random
import string
import threading
import time
from priority_message_queue import PriorityMessageQueue
from thread_pool import ThreadPool
from message_sender import MessageSender

def main():
    message_queue = PriorityMessageQueue()
    thread_pool = ThreadPool(num_threads=3)
    message_sender = MessageSender(message_queue, thread_pool)

    # Function to generate random message
    def generate_random_message(length=20):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def send_messages(thread_id):
        messages = [(generate_random_message(), random.randint(1, 5), random.choice(range(3))) for _ in range(5)]
        messages.sort(key=lambda x: x[1])  # Sort messages by priority
        for message, priority, target_thread in messages:
            print(f"Thread {thread_id} sending message: {message} with priority {priority} to Thread {target_thread}")
            message_sender.send_message(message, priority, target_thread)

    # Start multiple threads
    threads = []
    for thread_id in range(3):
        thread = threading.Thread(target=send_messages, args=(thread_id,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join(timeout=10)

    # Shutdown the thread pool
    thread_pool.shutdown()

if __name__ == "__main__":
    main()