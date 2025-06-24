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

#module 3 - Job expiry and cleanup
def remove_expired_jobs(self):
    print("checking for expired jobs")
    expired_jobs = []

    #finding jobs that have waited for too long 
    for job in self.queue:
        if job.waiting_time > 10:
            expired_jobs.append(job)
    #removing them
    for job in expired_jobs:
        self.queue.remove(job)
        print(f"Job {job.job_id} expired and removed")
    
    return len(expired_jobs)
