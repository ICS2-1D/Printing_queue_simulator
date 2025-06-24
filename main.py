from collections import deque
import threading
import concurrent.futures
import time
import uuid

#<---(2) Priority and Aging System - KISILU JAKES --->
class PriorityManager:
    def __init__(self, aging_interval=5):
        self.aging_interval = aging_interval

    def apply_aging(self, jobs): #increments a job's priority if its wait_time is a multiple of the aging_interval
        for job in jobs:
            if job.wait_time > 0 and job.wait_time % self.aging_interval == 0:
                job.priority += 1

    def sort_by_priority(self, jobs): #sorts jobs in descending order of priority (higher priority first)
        return sorted(jobs, key=lambda j: (-j.priority, -j.wait_time))
# #EXAMPLE USAGE OF THIS:
# class Job:
#     def __init__(self, priority, wait_time):
#         self.priority = priority
#         self.wait_time = wait_time
#
# # Initialize jobs
# jobs = [Job(1, 3), Job(2, 5), Job(1, 6), Job(3, 2)]
#
# # Initialize PriorityManager
# manager = PriorityManager(aging_interval=5)
#
# # Apply aging (simulate jobs waiting)
# for job in jobs:
#     job.wait_time += 1  # Increment wait time
# manager.apply_aging(jobs)  # This will increment priority for jobs with wait_time % 5 == 0
#
# # Sort by priority
# sorted_jobs = manager.sort_by_priority(jobs)
# for job in sorted_jobs:
#     print(f"Priority: {job.priority}, Wait Time: {job.wait_time}")




#<---Job Expiry and Cleanup - DAVIS MUTUA --->
class PrintJob:
    """Represents a single print job in the queue."""
    def __init__(self, job_name, submission_time, expiry_time_seconds):
        self.job_id = str(uuid.uuid4())
        self.job_name = job_name
        self.submission_time = submission_time
        self.expiry_time = submission_time + expiry_time_seconds
        self.status = "waiting"

    def is_expired(self, current_time):
        """Checks if the job has expired."""
        return current_time > self.expiry_time

    def get_waiting_time(self, current_time):
        """Calculates the current waiting time for the job."""
        return current_time - self.submission_time

    def __str__(self):
        return (f"Job ID: {self.job_id}, Name: {self.job_name}, "
                f"Submitted: {time.ctime(self.submission_time)}, "
                f"Expires: {time.ctime(self.expiry_time)}, Status: {self.status}")

class PrintQueueSimulator:
    """Simulates a print queue with job expiry and cleanup."""
    def __init__(self, default_expiry_time_seconds=300): 
        self.queue = []
        self.default_expiry_time_seconds = default_expiry_time_seconds
        print(f"Print Queue Simulator initialized. Default job expiry: {self.default_expiry_time_seconds} seconds.")

    def add_job(self, job_name):
        """Adds a new print job to the queue."""
        current_time = time.time()
        job = PrintJob(job_name, current_time, self.default_expiry_time_seconds)
        self.queue.append(job)
        print(f"\n[JOB ADDED] {job.job_name} (ID: {job.job_id}) added to the queue at {time.ctime(current_time)}.")
        return job.job_id

    def _notify_expiry(self, job):
        """Notifies the system and users about an expired job."""
        print(f"\n[JOB EXPIRED] Job '{job.job_name}' (ID: {job.job_id}) has expired and been removed from the queue.")

    def clean_expired_jobs(self):
        """Removes expired jobs from the queue and notifies."""
        current_time = time.time()
        
        expired_jobs_to_notify = [job for job in self.queue if job.is_expired(current_time)]
        
        self.queue = [job for job in self.queue if not job.is_expired(current_time)]
        
        if expired_jobs_to_notify:
            print(f"\n--- Cleaning expired jobs ---")
            for job in expired_jobs_to_notify:
                 self._notify_expiry(job)
            print(f"--- {len(expired_jobs_to_notify)} job(s) removed due to expiry. ---")
        else:
            print("\nNo expired jobs to clean.")


    def print_next_job(self):
        """Simulates printing the next job in the queue."""
        if not self.queue:
            print("\nPrint queue is empty.")
            return None

        self.clean_expired_jobs()

        if not self.queue:
            print("No valid jobs left in the queue after cleanup.")
            return None

        job = self.queue.pop(0) 
        job.status = "printing"
        current_time = time.time()
        waiting_time = job.get_waiting_time(current_time)
        print(f"\n[PRINTING] Printing job: '{job.job_name}' (ID: {job.job_id}).")
        print(f"Time in queue: {waiting_time:.2f} seconds.")
        time.sleep(2) 
        job.status = "completed"
        print(f"[COMPLETED] Job '{job.job_name}' (ID: {job.job_id}) completed at {time.ctime(time.time())}.")
        return job.job_id

    def view_queue(self):
        """Displays all jobs currently in the queue."""
        if not self.queue:
            print("\nPrint queue is currently empty.")
            return

        print("\n--- Current Print Queue ---")
        for i, job in enumerate(self.queue):
            current_time = time.time()
            remaining_time = job.expiry_time - current_time
            status_info = "Expired" if job.is_expired(current_time) else f"Expires in: {max(0, remaining_time):.1f}s"
            current_waiting_time = job.get_waiting_time(current_time)
            print(f"{i+1}. {job} - Waiting Time: {current_waiting_time:.1f}s - {status_info}")
        print("--------------------------")




#<---Concurrent and Thread Handling - KOROS AMANI --->
def process_single_job(self,user_id,job_id,priority):

    enqueued_successfully = self.enqueue_job(user_id,job_id, priority)
    if enqueued_successfully:
        return f"Succesfully submitted job {job_id} for use {user_id}."
    else:
        return f"Failed to submit job {job_id} for user {user_id} (Queue full)."

def handle_simultaneous_submissions(self,jobs):
    all_submissions_outcomes = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for job in jobs:
            future = executor.submit(self.process_single_job, job[0], job [1], job[2])
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:

                result= future.result()
                all_submissions_outcomes.append(result)

            except Exception as exc:
                print(f"One of the jobs raised has an unhandled exception: {exc}")
                all_submissions_outcomes.append(f"Job failed with exception: {exc}")


    print("\n--- All concurrent job submission completed.---")
    return all_submissions_outcomes
