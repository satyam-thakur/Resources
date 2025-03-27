def selection_sort(Array):
    n = len(Array)
    # print(n)
    for i in range (1, n):
        # print(i)
        for j in range(i,0,-1):
            # print(i,j-1,j)
            if Array[j-1] > Array[j]:
                Array[j], Array[j-1] = Array[j-1], Array[j]
            else:
                break
    return Array

A = [2, -2, 4, 6, 7, 9, 3]
print (selection_sort(A))

#Time: O(n^2)
#Space: O(1)
