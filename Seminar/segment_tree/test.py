from segment_tree import *
import random
#from draw_tree import *

array_length = 10
number_of_queries = 100
array = [random.randint(-10, 30) for i in range(array_length)]
t = SegmentTree(array,'max')
#visualize(t.root)
print(array)
print(t.RangeQuery(2,5))