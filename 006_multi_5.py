import time
import concurrent.futures

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'


if __name__ == '__main__':

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # The submit function schedules the target function to be run,
        # and return it as a future object. It allows to encapsulate the
        # execution of the function, and allows us to check on it after it
        # is scheduled.
        f1 = executor.submit(do_something, 1)
        print(f1.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')

# Even if there are more processes than cores, it was still able to finish. Why?
# The CPU has a way to switch between cores.