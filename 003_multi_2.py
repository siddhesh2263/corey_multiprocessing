import time
import multiprocessing

def do_something():
    print('Sleeping 3 second...')
    time.sleep(3)
    print('Done Sleeping...')


if __name__ == '__main__':

    start = time.perf_counter()

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')


# The error faced in 002 was resolved by using the above code
# construct.