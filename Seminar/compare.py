from segment_tree.segment_tree import *
from BIT import *
import NaiveSolution
import random
import time 
import pandas as pd

input_sizes = [10, 100, 1000, 10000, 100000]
time_complexs = []
for size in input_sizes:
    input = [random.uniform(-100, 100) for i in range(size)]
    low = random.randint(0, size - 1)
    hi = random.randint(low, size - 1)
    cpl = []

    ns_start = time.time()
    ns = NaiveSolution.NaiveSum(input, low, hi)
    ns_end = time.time()
    cpl.append(round((ns_end - ns_start) * 10**3, 4 ))


    st_start = time.time()
    st = SegmentTree(input, 'sum').RangeQuery(low, hi)
    st_end = time.time()
    cpl.append(round((st_end - st_start) * 10**3, 4))


    fw_start = time.time()
    fw = FenwickTree(input).fw_sumRange(low, hi)
    fw_end = time.time()
    cpl.append(round((fw_end - fw_start) * 10**3, 4))

    time_complexs.append(cpl)

df = pd.DataFrame(time_complexs, index = input_sizes, columns=['Naive', 'SegmentTree', 'BIT'])
df.to_excel('compare.xlsx', sheet_name='time_complex')
