def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(a[i]-a[i+1]) for i in range(inputArray - 1)])
    
