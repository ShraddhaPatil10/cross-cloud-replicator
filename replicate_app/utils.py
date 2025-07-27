# replicate_app/utils.py
import time

def retry_on_exception(func):
    def wrapper(*args, **kwargs):
        retries = 3
        delay = 2
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retry {attempt+1}: {e}")
                time.sleep(delay)
        raise Exception("Max retries exceeded")
    return wrapper

