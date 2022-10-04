from copy import copy
import random

def LSB(i):
    return i & -i

class FenwickTree(object):

    def __init__(self,nums):
        self.size = len(nums)

        tmp = copy(nums)
        for i in range(self.size):
            j = i + LSB(i+1)
            if j < self.size:
                tmp[j] += tmp[i]

        self.vals = tmp

    def fw_sumRange(self, start, end):
        total = 0
        while start < end:
            total += self.vals[end-1]
            end -= LSB(end)

        while start > end:
            total -= self.vals[start-1]
            start -= LSB(start)


        return total

    def update(self, idx, val):
        while idx < self.size:
            self.vals[idx] += val
            i += LSB(i+1)

    def get_index_val(self, idx):
        return self.fw_sumRange(self, idx, idx + 1)

        