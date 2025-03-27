def insertion_sort(Array):
    n = len(Array)
    for i in range (1, n):
        print("i={}".format(i))
        for j in range (i, 0, -1):
            print("j={}".format(j))
            if Array[j] <  Array[j-i]:
                Array[j],Array[j-i] = Array[j-i],Array[j]
            else:
                break
    return Array

A = [8, 5, 2, 9, 5, 6, 3]
print(insertion_sort(A))

# O(n^2)
# O(1)