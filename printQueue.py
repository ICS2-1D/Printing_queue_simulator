import time


class PrintQueue:

    def __init__(self, capacity=10, expiry_time=30):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.expiry_time = expiry_time
        self.job_counter = 0

    def enqueue_job(self,user_id,job_id, job):
        if self.size == self.capacity:
            print("Queue is full")
            return
        self.queue[self.rear] = {
            "user_id": user_id,
            "job_id": job_id,
            "job": job,
            "timestamp": time.time()
        }
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue_job(self):
        if self.size == 0:
            print("Queue is empty")
            return None
        job = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return job

    def get_queue_status(self):
        return {
            "size": self.size,
            "capacity": self.capacity,
            "jobs": [job for job in self.queue if job is not None]
        }




    def show_Status(self):