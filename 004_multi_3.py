import time
import multiprocessing

def do_something():
    print('Sleeping 1 second(s)...')
    time.sleep(1)
    print('Done Sleeping...')


if __name__ == '__main__':

    start = time.perf_counter()

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        # We cannot do a p.join() inside the loop. It will
        # be same as synchronous.
        processes.append(p)
    
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')

# Even if there are more processes than cores, it was still able to finish. Why?