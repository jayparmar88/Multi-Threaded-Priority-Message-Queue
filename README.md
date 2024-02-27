# Multi-Threaded Priority Message Queue

This project implements a multi-threaded priority message queue system in Python, allowing threads to send messages to each other with varying priorities. The solution comprises three main components: Priority Message Queue, Thread Pool, and Message Sender. The system is designed to handle concurrent message processing and execution of actions associated with received messages.

## Table of Contents

- [Project Overview](#project-overview)
- [Components](#components)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Program](#running-the-program)
- [Test Cases](#test-cases)
- [License](#license)

## Project Overview

The project consists of the following components:

1. **Priority Message Queue:**
   - Implemented using Python's `queue.PriorityQueue`.
   - Supports operations like enqueue, dequeue, peek, and empty check.

2. **Thread Pool:**
   - Utilizes Python's `concurrent.futures.ThreadPoolExecutor`.
   - Manages a pool of threads for concurrent execution of tasks.
   - Includes features for submitting tasks, notifying waiting threads, and orderly shutdown.

3. **Message Sender:**
   - Coordinates the sending of messages between threads.
   - Utilizes the Priority Message Queue and Thread Pool for efficient message processing.

## Components

- [priority_message_queue.py](#) - Implementation of the priority message queue.
- [thread_pool.py](#) - Implementation of the thread pool.
- [message_sender.py](#) - Implementation of the message sending function.
- [main.py](#) - Main program with test cases demonstrating the functionality.

## Requirements

- Python 3.10 or upgraded version installed on system.

## Setup

1. Clone the Git repository.
2. Navigate to the directory containing the source code files.

## Running the Program

Execute the following command in the terminal or command prompt:

```bash
python main.py
```

## Test Cases

The test case in `main.py` simulates a scenario where multiple threads send messages to each other with different priorities. Messages are randomly generated and sorted by priority before sending. Expected outcomes include the display of messages being sent between threads, demonstrating the functionality of the priority message queue, thread pool, and message sender components.

I got below output after running main.py file.

Thread 0 sending message: gycLkfOsuEtDTHxsMTfB with priority 1 to Thread 1
Thread 0 sending message: wpkjhWisjoMNoXOjTScZ with priority 2 to Thread 0
Thread 0 sending message: OOOPAsPsdmjyFoCnMzYF with priority 4 to Thread 0
Thread 0 sending message: NDtWURusnzAFBYJZBlxm with priority 4 to Thread 0
Thread 0 sending message: iSfhXBxGOwQpjtOrXjIy with priority 4 to Thread 1
Thread 1 sending message: fobNCnfPlYJbTkqGFZkS with priority 1 to Thread 2
Thread 1 sending message: ICGcfvKowfVFdtsIDads with priority 2 to Thread 2
Thread 1 sending message: yXtcETNaIiaOpmesZKMA with priority 3 to Thread 0
Thread 1 sending message: VTcEiHeirXkttvfapifO with priority 4 to Thread 2
Thread 1 sending message: DPEAYHYlsxlggPvKDdhJ with priority 5 to Thread 1
Thread 2 sending message: ymfZpRMEraAecmcmWgkd with priority 1 to Thread 0
Thread 2 sending message: IzEThIbZXNsDUQWKsZWJ with priority 2 to Thread 1
Thread 2 sending message: KpgFMGJWtiQKzkDMXhQj with priority 3 to Thread 0
Thread 2 sending message: DkOCyGkYcmgZWEBEqQLj with priority 4 to Thread 1
Thread 2 sending message: VUQrdQdOFNPyhgbpuLua with priority 5 to Thread 2

## License

This project is licensed under the MIT License - see the [LICENSE](#) file for details.
