import time

name = "Raspberry Pi Pico W"
count = 0

while count < 5:
    print(name, "Count:", count)
    count += 1
    time.sleep(1)

print("Program Completed")
