import time
import sys
from itertools import permutations

def permutation_sort(arr):
    new_arr = permutations(arr)
    for ls in new_arr:
        is_sorted = True

        for i in range(1,len(ls)):
            if ls[i-1] > ls[i]: sorted = False
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
    return quick_sort(left) + quick_sort(right)

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
    else:
        while i < len(left):
            result.append(left[i])
    
    return result

