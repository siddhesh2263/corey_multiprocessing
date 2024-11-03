import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

# We don't want to execute the function. We created 2
# process objects.
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# Error:

# RuntimeError:
#         An attempt has been made to start a new process before the
#         current process has finished its bootstrapping phase.

#         This probably means that you are not using fork to start your
#         child processes and you have forgotten to use the proper idiom
#         in the main module: