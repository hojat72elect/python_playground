import numpy
import time

array1 = numpy.random.rand(1_000_000)

# time of operation for first method
start_time = time.time()
result1 = numpy.sum(array1**2)
end_time = time.time()
time1 = end_time - start_time

start_time = time.time()
result2=0
for x in array1:
    result2 += x**2
end_time = time.time()
time2 = end_time - start_time


print("Method 1 (NumPy):", time1, "seconds")
print("Method 2 (loop):", time2, "seconds")