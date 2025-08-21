import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        r = func(*args, **kwargs)
        e = time.time()
        print(f"'{func.__name__}' ran in {e - s:.4f} secs.")
        return r
    return wrapper

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

@timing_decorator
def process_file_data(n, file_name):
    print(f"Processing data for {n} iterations.")
    with FileManager(file_name, "w") as f:
        for i in range(n):
            f.write(f"Line {i}\n")
            time.sleep(0.00005)
    print("File processing complete.")

process_file_data(2000, "simple_sample.txt")

with FileManager("simple_sample.txt", "r") as f:
    print("\nFile content preview:")
    for i, line in enumerate(f):
        if i >= 5: break
        print(line.strip())
