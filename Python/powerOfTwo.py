def isPowerOfTwo( n: int) -> bool:
    if n <=0:
        return False
    while n%2==0:
        n//=2
    return n==1

n=int(input("Enter a number : "))
print(f'{n} is power of 2 : {isPowerOfTwo(n)}')