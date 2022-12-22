def basic_decorator(func):        # Basic decorator
    """A decorator that wraps a function return the original function result
    """
    def wrapper(*args, **kwargs):
        print("started")
        value = func(*args, **kwargs)
        print(value)
        print("done")
        return value
    return wrapper



def decorator_with_log(func):
    """A decorator that wraps a function, return the original function result and write all of this in a log file with more information about the runtime
    """
    from datetime import datetime
    import time
    import os
    def wrapper(*args, **kwargs):
        with open(os.getcwd() + '/' + "logs.txt", "a") as f:     # open the log file
            start = (datetime.now(),time.time())                    # defines the time at which the program starts to run
            print("started")
            value = func(*args, **kwargs)               #get the func result
            f.write(f"Function '{func.__name__}' called with {[arg for arg in args]} at {start[0]}  return {value} and done in {time.time() - start[1]} seconds" + "\n") #write the informations in the logs.txt file
            print("done")
            return value    # return the func result
    return wrapper




if __name__ == "__main__":     #Example to test
    @decorator_with_log
    def f(*args):
        print("hello world")
    f(1,8,5,6)

    