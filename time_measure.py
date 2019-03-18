import functools
import time

def get_time(func):
    @functools.wraps(func)
    def wrapper(*args):
        start = time.time()
        x = func(*args)
        end = time.time()
        return x, end - start
    return wrapper

if __name__ == "__main__":
    f = get_time(lambda n: n*(n+1)//2)
    for i in range(100):
        print(f"{f(i)[0]} took {f(i)[1]} seconds.")
