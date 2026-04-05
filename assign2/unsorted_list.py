import random
import sys

MIN = -sys.maxsize - 1
MAX = sys.maxsize
k = 10000


unsorted_list = [random.randint(MIN, MAX) for _ in range(k)]

with open("./assign2/#2_Assignment/unsorted_list.txt", "w") as f:
    f.write(",".join(map(str, unsorted_list)))