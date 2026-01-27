###################################################################################################

# Design a Python application where multiple threads update a shared variable.

# Use a Lock to avoid race conditions.

# Each thread should increment the shared counter multiple times.

# Display the final value of the counter after all threads complete execution.

###################################################################################################


import threading

counter = 0

lock = threading.Lock()

def increment_counter(times):
    global counter
    for value in range(times):
            lock.acquire()
            counter = counter + 1
            lock.release()


def main():
    num = int(input("Enter number of threads: "))
    threads = []

    for value in range(num):          
        thread = threading.Thread(target=increment_counter, args=(1000,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final Counter Value:", counter)

if __name__ == "__main__":
    main()