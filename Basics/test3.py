def my_func():
	x = 10
	print("Value inside function:",x)

#global x
x = 50
my_func()
print("Value outside function:",x)

'''
def my_func2(l):
    l.append("CCCC")

l=["aaa","BBBB"]
my_func2(l)
for item in l:
    print(item)
'''

'''
def my_func3(x):
    x=3
    
my_int = 33
my_func3(my_int)
print(my_int)
'''