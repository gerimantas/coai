class ProgressTracker:
    def __init__(self):
        # Initialize progress storage (e.g., in-memory dictionary or database connection)
        self.progress = {}

    def set_progress(self, task_id, status):
        """Set the progress status for a specific task."""
        self.progress[task_id] = status

    def get_progress(self, task_id):
        """Get the progress status for a specific task."""
        return self.progress.get(task_id, "Not Started")

    def get_all_progress(self):
        """Get the progress status for all tasks."""
        return self.progress

# Example usage
if __name__ == "__main__":
    tracker = ProgressTracker()
    tracker.set_progress("12.2", "In Progress")
    print(tracker.get_progress("12.2"))
    print(tracker.get_all_progress())
