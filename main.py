#Ray
from datetime import datetime

class PrintJob:
    def __init__(self, user_id, title, priority=5):
        self.user_id = user_id      # Who submitted the job
        self.title = title           # Name of document
        self.priority = priority     # Lower number = higher urgency
        self.created_at = None       # Will be set when enqueued
        self.job_id = -1             # Will be assigned when enqueued


# Circular array-based queue to manage print jobs
class CircularPrintQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.jobs = [None] * capacity
        self.front = 0         # Points to oldest job
        self.rear = -1         # Points to newest job slot
        self.count = 0         # Current number of jobs
        self.next_job_id = 1   # Auto-incremented job ID

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0

    def enqueue(self, job):
        if self.is_full():
            print("Error: Queue is full. Cannot add more jobs.")
            return False

        self.rear = (self.rear + 1) % self.capacity
        job.job_id = self.next_job_id
        job.created_at = datetime.now()
        self.jobs[self.rear] = job
        self.next_job_id += 1
        self.count += 1
        print(f"✅ Job '{job.title}' added to queue (ID: {job.job_id})")
        return True

    def dequeue(self):
        if self.is_empty():
            print("❌ No jobs in queue to print.")
            return None

        removed_job = self.jobs[self.front]
        self.jobs[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"🖨️ Printing job: '{removed_job.title}' (User: {removed_job.user_id}, Priority: {removed_job.priority})")
        return removed_job

    def display_queue(self):
        print("\n📋 Current Print Queue:")
        print("-" * 60)
        print(f"{'ID':<4} | {'User':<6} | {'Title':<20} | {'Priority':<8} | {'Submitted At':<19}")
        print("-" * 60)

        for i in range(self.count):
            idx = (self.front + i) % self.capacity
            job = self.jobs[idx]
            if job:
                print(f"{job.job_id:<4} | {job.user_id:<6} | {job.title:<20} | {job.priority:<8} | {job.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)

if __name__ == "__main__":
    # Create a new print queue with space for 3 jobs
    queue = CircularPrintQueue(capacity=3)

    job1 = PrintJob(user_id="U1", title="Report.pdf")
    job2 = PrintJob(user_id="U2", title="Slides.pptx", priority=2)
    job3 = PrintJob(user_id="U3", title="Data.xlsx")

    queue.enqueue(job1)
    queue.enqueue(job2)
    queue.enqueue(job3)

    queue.display_queue()

    queue.dequeue()

    queue.display_queue()