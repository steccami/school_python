'''l = [num**2 for num in range(5)]

for item in l:
    print(item)

for item in l:
    print(item)
'''

g = (num**2 for num in range(5))

#print(next(g))

for item in g:
    print(item)


'''
for item in g:
    print(item)
'''

'''
import sys
l = [i * 2 for i in range(10000)]
print(sys.getsizeof(l))
g = (i ** 2 for i in range(10000))
print(sys.getsizeof(g))
'''