import time
def calculate_time(func):
    def timer():
        timing = time.time()
        func()
        print("This took: %s seconds" % (time.time() - timing))
    return timer
@calculate_time
def sleep():
    time.sleep(2)
sleep()