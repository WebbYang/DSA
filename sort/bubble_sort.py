import sys
import re
import time
import random

def performance(method):
    def timed(data):
        start = time.perf_counter()
        result = method(data)
        diff = time.perf_counter() - start
        print(f"Consume: {diff}")

        return result
    return timed
    
@performance
def bubble(data):
    
    total_len = len(data)
    #print(f'0: {data}')
    for k in range(1, total_len):
        switch_cnt = 0
        for i in range(1, total_len):
            if data[i-1]>data[i]:
                smaller = data.pop(i)
                data.insert(i-1, smaller)
                switch_cnt += 1
        #print(f'{k}: {data}')
        if switch_cnt==0:
            print('Early stop')
            return data
    print('Whole process')
    return data

if __name__=='__main__':
    args = sys.argv
    if len(args)>1:
        if len(args)>2:
            for item in args[2:]:
                args[1]+=f' {item}'
        data = [int(item) for item in re.split('\s|,',args[1])]
        bubble(data)
    else:
        random.seed(100)
        randomlist = random.sample(range(1, 10000), 1000)
        bubble(randomlist)
    print('complete')