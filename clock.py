import time

start_time = time.time()

# Your code here
for i in range(1000000):
    pass

end_time = time.time()

execution_time = end_time - start_time
print(f"Time taken to execute: {execution_time} seconds")
import time

print("Starting...")
time.sleep(3)
print("Delay complete.")
import time

current_time = time.gmtime()

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

print(formatted_time)