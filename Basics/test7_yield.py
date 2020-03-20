def multi_yield():
	yield_str = "This will print the first string"
	yield yield_str
	yield_str = "This will print the second string"
	yield yield_str

multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
#print(next(multi_obj))



'''
def new_yield(n):
    for num in range(n):
        yield num
        
l=list(new_yield(3))
'''