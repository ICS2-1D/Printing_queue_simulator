# printQueue.py

from main import PrintQueueManager
import time # Ensure time is imported, even if time.sleep() is commented in main.py

def main():
    """
    Main function to set up and run a condensed print queue simulation.
    This version provides a clear flow to demonstrate all main functionalities.
    """
    print("DEBUG: main() function started.") # DEBUG PRINT
    # Initialize the Print Queue Manager with a small capacity for quicker testing
    # Capacity: 5 jobs
    # Default Expiry Time: 60 seconds (simulated)
    # Aging Interval: 10 seconds (simulated)
    pq_manager = PrintQueueManager(capacity=5, default_expiry_time_seconds=60, aging_interval=10)
    print("DEBUG: PrintQueueManager instance created.") # DEBUG PRINT

    # Define a streamlined sequence of events for the simulation
    # Each event is a tuple: (event_type, *args)
    simulation_events = [
        ("comment", "--- Phase 1: Initial Enqueues & Queue Status ---"),
        ("enqueue", "Alice", "Document A (P3)", 3), # Enqueue with priority 3
        ("enqueue", "Bob", "Document B (P1)", 1),   # Enqueue with highest priority 1
        ("enqueue", "Charlie", "Document C (P5)", 5),# Enqueue with lowest priority 5
        ("show_status",), # Display the initial queue state

        ("comment", "\n--- Phase 2: Time Progression, Aging, & First Dequeue ---"),
        ("tick", 10), # Simulate 10 seconds. Jobs will age (priority might decrease by 1).
        ("show_status",),
        ("print_job",), # Dequeue the highest priority job (should be Bob's - Document B)
        ("show_status",),

        ("comment", "\n--- Phase 3: Concurrent Submissions ---"),
        ("simultaneous_submit", [ # Simulate multiple users submitting jobs at the same time
            ("David", "Document D (P4)", 4),
            ("Eve", "Document E (P2)", 2),
            ("Frank", "Document F (P5)", 5),
        ]),
        ("show_status",),

        ("comment", "\n--- Phase 4: Extended Time & Job Expiry ---"),
        ("tick", 55),
        ("show_status",),

        ("comment", "\n--- Phase 5: Final Dequeues & Empty Queue ---"),
        ("print_job",),
        ("show_status",),
        ("print_job",),
        ("show_status",),
        ("print_job",),
        ("show_status",),

        ("comment", "\n--- Phase 6: Final Check (Empty Queue) ---"),
        ("tick", 10),
        ("show_status",),
    ]
    print("DEBUG: Simulation events defined.") # DEBUG PRINT

    # Run the simulation with the defined events
    pq_manager.run_simulation(simulation_events)
    print("DEBUG: pq_manager.run_simulation() call completed.") # DEBUG PRINT

    print("\n--- Simulation Complete ---")
    print("DEBUG: main() function finished.") # DEBUG PRINT

# This ensures main() is called only when the script is executed directly
if __name__ == "__main__":
    print("DEBUG: Script started (__name__ == '__main__').") # DEBUG PRINT
    main()
    print("DEBUG: Script finished.") # DEBUG PRINT
