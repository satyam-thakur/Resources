def sort(numbers):
    non_zero = sorted(a for a in numbers if a !=0)
    zeros = numbers.count(0)
    return non_zero + [0] * zeros

numbers = [1,2,5,6,0,0,2,3,4]
sort_number = sort(numbers)
print(sort(sort_number))

