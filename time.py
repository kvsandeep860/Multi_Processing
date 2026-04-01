# import multiprocessing
# import time

# def do_something():
#     print("Sleeping for a second")
#     time.sleep(1)
#     print("Done Sleeping")

# if __name__ == "__main__":
#     start = time.perf_counter()

#     processes = []

#     for _ in range(10):
#         p = multiprocessing.Process(target=do_something)
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()

#     finish = time.perf_counter()

#     print(f"time taken to complete the code is {finish-start}")

import concurrent.futures
import time


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')