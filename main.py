from collections import deque
import threading
import concurrent.futures


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
