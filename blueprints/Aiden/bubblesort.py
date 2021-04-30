import numpy


def bubble(array_sort):
    n = len(array_sort)
    for i in range(n):
        for j in range(0, n -i- 1):
            if array_sort[j] > array_sort[j + 1]:
                array_sort[j], array_sort[j + 1] = array_sort[j + 1], array_sort[j]

print("Please enter 10 numbers!")
num_array = numpy.empty(10)
for i in range(10):
    x = float(input("Number:"))
    num_array[i] = x
bubble(num_array)
print(num_array)
