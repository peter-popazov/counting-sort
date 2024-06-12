import random
import time
import psutil


def counting_sort(arr):
    # record memory usage before sorting
    process = psutil.Process()
    before_memory = process.memory_info().rss

    # determine range of values
    max_num = max(arr)
    min_val = min(arr)
    range_val = max_num - min_val + 1

    # initialize the count and output arrays
    count = [0] * range_val
    output = [0] * len(arr)

    # counts the occurrences of each value
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    # calculate cumulative counts
    for i in range(1, range_val):
        count[i] += count[i - 1]

    # place elements in their sorted position in the output array staring from the end
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    # updates the original array with sorted values
    for i in range(len(arr)):
        arr[i] = output[i]

    # records the memory usage after sorting and returns the difference
    after_memory = process.memory_info().rss
    return after_memory - before_memory


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# function to measure sorting time
def measure_sorting_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


input_sizes_str = input("Enter a comma-separated list of input sizes: ")
input_sizes = [int(size) for size in input_sizes_str.split(',')]
min_val = int(input("Enter the minimum value (e.g., 1): "))
max_num = int(input("Enter the maximum value (e.g., 1000000): "))


# function to compare  algorithms
def compare_sorting_algorithms():
    counting_sort_times = []
    insertion_sort_times = []

    for size in input_sizes:
        arr = [random.randint(min_val, max_num) for _ in range(size)]

        # worst case for  insertion_sort
        # arr = sorted(arr, reverse=True)

        arr_copy_counting = arr.copy()
        arr_copy_counting_memory = arr.copy()
        counting_sort_time = measure_sorting_time(counting_sort, arr_copy_counting)
        used_memory = counting_sort(arr_copy_counting_memory)

        arr_copy_insertion = arr.copy()
        insertion_sort_time = measure_sorting_time(insertion_sort, arr_copy_insertion)

        counting_sort_times.append(counting_sort_time)
        insertion_sort_times.append(insertion_sort_time)

        print(f"\n Input Size: {size}")
        print(f"Counting Sort Time: {counting_sort_time:.8f} seconds")
        print(f"Insertion Sort Time: {insertion_sort_time:.8f} seconds")
        print(f"Counting Sort Memory Usage: {used_memory / 1024} KB")
        print("___________________________________________________")


if __name__ == "__main__":
    compare_sorting_algorithms()
