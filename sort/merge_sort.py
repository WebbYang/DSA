import sys
import re
from collections import deque
import itertools
import time
import random

def sort_2(left, right):
    if left>right:
        return [right, left]
    return [left, right]
def is_empty(data):
    return len(data)==0

def merge_sort(data, dtype='deque'):
    total_len = len(data)
    if dtype=='deque':
        data = deque(data)
    #print(total_len)
    if total_len>1:
        if total_len==2:
            if dtype=='deque':
                return deque(sort_2(data[0], data[1]))
            return sort_2(data[0], data[1])
        half = int(total_len/2)
        if dtype=='deque':
            sort_L = merge_sort(list(itertools.islice(data,0,half)),dtype)
            sort_R = merge_sort(list(itertools.islice(data,half,total_len+1)),dtype)
        else:
            sort_L = merge_sort(data[:half],dtype)
            sort_R = merge_sort(data[half:],dtype)
    else:
        return(data)
    if dtype=='deque':
        merge_data = deque([])
    else:
        merge_data = []
    #print(f"L:{sort_L}, R:{sort_R}")
    for _ in range(total_len):
        if dtype=='deque':
            left = sort_L.popleft()
            right = sort_R.popleft()
        else:
            left = sort_L.pop(0)
            right = sort_R.pop(0)
        if left<right:
            merge_data.append(left)
            if dtype=='deque':
                sort_R.appendleft(right)
            else:
                sort_R.insert(0, right)            
            if is_empty(sort_L):
                #merge_data+=sort_R
                merge_data.extend(sort_R)
                break
        else:
            merge_data.append(right)
            if dtype=='deque':
                sort_L.appendleft(left)
            else:
                sort_L.insert(0, left)
            if is_empty(sort_R):
                #merge_data+=sort_L
                merge_data.extend(sort_L)
                break
    #print(f'Merge: {merge_data}')
    return merge_data

if __name__=='__main__':
    args = sys.argv
    if len(args)>1:
        if len(args)>2:
            for item in args[2:]:
                args[1]+=f' {item}'
        data = [int(item) for item in re.split('\s|,',args[1])]
        merge_sort(data)
    else:
        random.seed(100)
        randomlist = random.sample(range(1, 10000), 1000)
        start = time.perf_counter()
        merge_sort(randomlist,dtype='list')
        diff = time.perf_counter() - start
        print(f"Consume: {diff}")
    print('complete')
