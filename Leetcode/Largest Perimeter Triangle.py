def largestPerimeter(A):
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i] < A[i+1] + A[i+2]:
            return A[i] + A[i+1] + A[i+2]
    return 0

print(largestPerimeter([1,2,1,10]))