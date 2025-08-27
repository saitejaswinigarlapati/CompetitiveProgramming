'''
A Perfect Number is a positive integer equal to the sum of its proper divisors (excluding itself).

Examples:

6 → Divisors = 1, 2, 3 → Sum = 6 ✅ Perfect

28 → Divisors = 1, 2, 4, 7, 14 → Sum = 28 ✅ Perfect

12 → Divisors = 1, 2, 3, 4, 6 → Sum = 16 ❌ Not Perfect

'''

def isPerfectNumber(n: int) -> bool:
    if n <= 1:
        return False
    
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Avoid adding sqrt twice
                divisors_sum += n // i
    
    return divisors_sum == n


# Test cases
numbers = [6, 28, 12, 496, 97]
for num in numbers:
    print(f"{num}: {'Perfect Number' if isPerfectNumber(num) else 'Not a Perfect Number'}")
