import threading
import queue
import time


class Producer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        for i in range(5):
            item = f"item-{i}"
            self.q.put(item)  
            print(f"Producer produced {item}")
            time.sleep(1)



class Consumer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            try:
                item = self.q.get(timeout=3) 
                print(f"Consumer consumed {item}")
                time.sleep(2)
            except queue.Empty:
                break


if __name__ == "__main__":
    q = queue.Queue()

    producer = Producer(q)
    consumer = Consumer(q)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("All tasks finished.")
