from collections import deque
import threading
import concurrent.futures

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