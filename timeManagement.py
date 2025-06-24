##constructor method
def __init__(self):
    self.queue =[]
    self.current_time = 0

##PLACEHOLDER FUNCTIONS
#module 2 - Priority and aging system
def apply_priority_aging(self):
    print("Aging jobs...")
    for job in self.queue:
        if job.waiting_time > 5:
            job.priority += 1
            print(f"Job {job.job_id} priority increased to {job.priority}")

##reminder to check waiting list and age every 10 min
def should_age_now(self):
    return self.current_time % 5 == 0
