def diagonalDifference(arr):
    l = sum(arr[i][i] for i in range(n))
    r = sum(arr[i][n-i-1] for i in range(n))
    return abs(l - r)
