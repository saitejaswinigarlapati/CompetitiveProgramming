# Find the Fibonacci series upto n terms.

def fibonacci(n):
    if n==0:
        return [0]
    if n==1:
        return [1]
    l=[]
    for i in range(2,n):
        l.append(l(-1) - l(-2))
    return l

print(fibonacci(5))
    
