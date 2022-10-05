#Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = 0
        self.left = None
        self.right = None
        

class SegmentTree(object):
    def __init__(self, nums, operation):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #helper function to create the tree from input array
        self.operation = operation

        def createTree(nums, l, r):
            
            #base case
            if l > r:
                return None
                
            #leaf node
            if l == r:
                n = Node(l, r)
                n.value = nums[l]
                return n
            
            mid = (l + r) // 2
            
            root = Node(l, r)
            
            #recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            
            #Total stores the sum of all leaves under root
            #i.e. those elements lying between (start, end)
            if self.operation == 'sum':
                root.value = root.left.value + root.right.value
            elif self.operation == 'min':
                root.value = root.left.value if root.left.value < root.right.value else root.right.value
            elif self.operation == 'max':
                root.value = root.left.value if root.left.value > root.right.value else root.right.value        
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateVal(root, i, val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.value = val
                return val
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)
            
            #Propogate the changes after recursive call returns
            if self.operation == 'sum':
                root.value = root.left.value + root.right.value
            elif self.operation == 'min':
                root.value = root.left.value if root.left.value < root.right.value else root.right.value
            elif self.operation == 'max':
                root.value = root.left.value if root.left.value > root.right.value else root.right.value  
            
            return root.value
        
        return updateVal(self.root, i, val)

    def RangeQuery(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def rangeQuery(root, i, j):

            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.value
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return RangeQuery(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return RangeQuery(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                if self.operation == 'sum':
                    return RangeQuery(root.left, i, mid) + RangeQuery(root.right, mid+1, j)
                elif self.operation == 'min':
                    return RangeQuery(root.left, i, mid) if RangeQuery(root.left, i, mid) < root.value else RangeQuery(root.right, mid+1, j)
                else:
                    return RangeQuery(root.left, i, mid) if RangeQuery(root.left, i, mid) > root.value else RangeQuery(root.right, mid+1, j)
        
        return rangeSum(self.root, i, j)
                
