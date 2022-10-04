def NaiveSum(arr, low, hi):
    sum = 0
    if low < hi:
        for i in [low,hi+1]:
            sum += arr[i]
    else:
        return
    
    return sum