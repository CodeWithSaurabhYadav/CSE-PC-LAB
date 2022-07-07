#/bin/python3

def fun(*x):
    print(type(x))
    print(len(x))
    for i in range(len(x)):
        print(x[i])
    sum(x[0],x[2])
def sum(a,b):
    print(f"The sum of {a} and {b} is {a+b}")
    
fun(3,4,5)

# Anonmyous Function
a = lambda x:x*2
print(a(2))

b = lambda m,n: m*n
print(b(2,3))

lst =[1,2,3,4,5]
print(list(filter(lambda p : (p%2==0),lst)))
print(list(filter(lambda p : (p+2),lst)))