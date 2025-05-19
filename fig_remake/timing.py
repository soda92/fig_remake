import subprocess
import time
from contextlib import ContextDecorator


class TimeSubprocess(ContextDecorator):
    """Times the execution of a subprocess command within a context manager."""

    def __init__(self, command, **kwargs):
        """
        Initializes the TimeSubprocess context manager.

        Args:
            command (list or str): The command to execute as a subprocess.
                                    If a string, it will be split into a list.
            **kwargs: Additional keyword arguments to pass to subprocess.run().
        """
        self.command = command
        self.kwargs = kwargs
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        self.process = None

    def __enter__(self):
        """Enters the context, starts the timer, and executes the subprocess."""
        self.start_time = time.perf_counter()
        try:
            self.process = subprocess.run(
                self.command, capture_output=True, text=True, check=True, **self.kwargs
            )
        except subprocess.CalledProcessError as e:
            self.end_time = time.perf_counter()
            self.elapsed_time = self.end_time - self.start_time
            print(f'Subprocess failed with error: {e}')
            print(f'Stdout: {e.stdout}')
            print(f'Stderr: {e.stderr}')
            raise  # Re-raise the exception to propagate the failure
        except FileNotFoundError as e:
            self.end_time = time.perf_counter()
            self.elapsed_time = self.end_time - self.start_time
            print(f'Error: Command not found: {e.filename}')
            raise
        return self.process  # Return the subprocess.CompletedProcess object

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exits the context, stops the timer, and prints the elapsed time."""
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        self._print_friendly_time(self.elapsed_time)

    def _print_friendly_time(self, seconds):
        if seconds < 60:
            print(f'Subprocess executed in {seconds:.4f} seconds.')
        elif seconds < 3600:
            minutes = int(seconds // 60)
            remaining_seconds = seconds % 60
            print(
                f'Subprocess executed in {minutes} minutes and {remaining_seconds:.4f} seconds.'
            )
        else:
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            remaining_seconds = seconds % 60
            print(
                f'Subprocess executed in {hours} hours, {minutes} minutes, and {remaining_seconds:.4f} seconds.'
            )
