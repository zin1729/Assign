import time
import sys
from itertools import permutations

def permutation_sort(arr, time_limit = 10):
    new_arr = permutations(arr)
    start_time = time.time()
    for ls in new_arr:
        if time.time() - start_time > time_limit:
            print(f"Permutation sorting: More than {time_limit} secs.")
            return None
        is_sorted = True

        for i in range(1,len(ls)):
            if ls[i-1] > ls[i]: 
                is_sorted = False
                break
        if is_sorted: return ls
    return None
        


def selection_sort(arr):
    new_arr = arr.copy()

    for i in range(len(new_arr)):
        min_idx = i
        for j in range(i+1, len(new_arr)):
            if new_arr[j] < new_arr[min_idx]:
                min_idx = j
        new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]
    
    return new_arr

def insertion_sort(arr):
    new_arr = arr.copy()

    for i in range(1,len(new_arr)):
        value = new_arr[i]
        j = i-1
        while j>=0 and value < new_arr[j]:
            new_arr[j+1] = new_arr[j]
            j -= 1
        new_arr[j] = value
    
    return new_arr

def bubble_sort(arr):
    new_arr = arr.copy()
    length = len(new_arr)

    for i in range(length):
        for j in range(length - i - 1):
            if new_arr[j] > new_arr[j+1]:
                new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]
    return new_arr

def quick_sort(arr):
    if len(arr) <= 1: return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1: return arr

    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j += 1
    if i == len(left):
        while j < len(right):
            result.append(right[j])
            j += 1
    else:
        while i < len(left):
            result.append(left[i])
            i += 1
    
    return result

if __name__ == "__main__":


    with open("./assign2/#2_Assignment/unsorted_list.txt", "r") as f:
        data = f.read()
    unsorted_list = list(map(int, data.split(",")))
    
    test_list = unsorted_list.copy()
    start = time.time()
    sorted_arr = permutation_sort(test_list)
    end = time.time()
    print("Execution Time for Permutation Sort:", end - start, "seconds")


    start = time.time()
    sorted_arr = selection_sort(unsorted_list)
    end = time.time()
    print("Execution Time for Selection Sort:", end - start, "seconds")


    start = time.time()
    sorted_arr = insertion_sort(unsorted_list)
    end = time.time()
    print("Execution Time for Insertion Sort:", end - start, "seconds")


    start = time.time()
    sorted_arr = quick_sort(unsorted_list)
    end = time.time()
    print("Execution Time for Quick Sort:", end - start, "seconds")


    start = time.time()
    sorted_arr = merge_sort(unsorted_list)
    end = time.time()
    print("Execution Time for Merge Sort:", end - start, "seconds")