
import threading
import time

def count_numbers():
    for i in range(1, 6):
        print("Counting:", i)
        time.sleep(1)

def calculate_square():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(1)
def calculate_cube():
    for i in range(1, 6):
        print("Cube of", i, "=", i * i * i)
        time.sleep(1)

t1 = threading.Thread(target=count_numbers)
t2 = threading.Thread(target=calculate_square)
t3 = threading.Thread(target=calculate_cube)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print("All tasks completed successfully!")
