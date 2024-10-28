b = [i**2 for i in range(10) if i>4]
print (b)

a = [m for m in range(8)]
print (a)

del (a[1])
print (a)

#append
a.append('a')
print(a)

#extend
a.extend(b)
print(a)

#insert
b.insert(2,55)
print(b)

#pop - removes last item
a.pop()
print(a)

a.remove(2)
print(a)

#sort -in place sort
b.sort()
print(b)

#set
z = set(b)
print(z)
print(z.pop(),z)
