def isPowerOfThree( n: int) -> bool:
        if n <=0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
    
n=int(input("Enter a number : "))
print(f"{n} is power of 3 : {isPowerOfThree(n)}")