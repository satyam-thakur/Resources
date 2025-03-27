import cProfile
def bubble_sort(A):
    n = len(A)
    print (n)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            # print (i-1,i,A[i-1],A[i])
            if A[i]<A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                flag = True
    return A
# cProfile.run('bubble_sort')
# print(A[7])
A = [-2,1, 1,3,-1, 8, 6, 7, 2]

print(bubble_sort(A))

#Time Complexity: O(n^2)
#Space Complexity: O(1)
print (A)

#https://www.youtube.com/watch?v=xli_FI7CuzA&list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl&index=3
