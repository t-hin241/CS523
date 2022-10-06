from segment_tree.segment_tree import *
from BIT import *
from NaiveSolution import *
import random
import timeit 
import pandas as pd

input_sizes = [10, 100, 1000, 10000, 100000, 1000000]
query_size = 5
time_complexs = []
for size in input_sizes:
    input = [random.uniform(-1000, 1000) for i in range(size)]
    low = random.randint(0, size//2 -1)
    hi = low + query_size
    cpl = []
    cpl.append(size)
    cpl.append(query_size)

    ns = NaiveSolution(input)
    ns_start = timeit.default_timer()
    ns.NaiveSum(low, hi)
    ns_end = timeit.default_timer()
    cpl.append((ns_end - ns_start) * 10**3)
    
    st = SegmentTree(input,'sum')
    st_start = timeit.default_timer()
    st.RangeQuery(low, hi)
    st_end = timeit.default_timer()
    cpl.append((st_end - st_start) * 10**3)

    fw = FenwickTree(input)
    fw_start = timeit.default_timer()
    fw.fw_sumRange(low, hi)
    fw_end = timeit.default_timer()
    cpl.append((fw_end - fw_start) * 10**3)

    time_complexs.append(cpl)
    query_size = query_size*10

df = pd.DataFrame(time_complexs, columns=['Input size', 'Query size', 'Naive', 'SegmentTree', 'BIT'])
df.to_excel('compare.xlsx', sheet_name='time_complex(ms)', index=False)
