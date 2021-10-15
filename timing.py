import time
def calculate_time(funt):
    def timer():
        timing = time.time()
        funt()
        print("This took: %s seconds" % (time.time() - timing))
    return timer
@calculate_time
def sleep():
    time.sleep(2)
sleep()