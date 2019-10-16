def decorator(func):
    def inner(*args,**kwargs):
        return 10 * func(*args, **kwargs)
    return inner

@decorator
def adder(x,y,z):
	return x + y + z

x=int(input("enter number"))
y=int(input("enter number"))
z=int(input("enter number"))

print(adder(x,y,z))