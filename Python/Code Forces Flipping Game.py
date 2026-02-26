n, t = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
current_sum = 0
max_books = 0

for right in range(n):
    current_sum += arr[right]
    
    # Shrink window if sum exceeds t
    while current_sum > t:
        current_sum -= arr[left]
        left += 1
    
    # Update max books
    max_books = max(max_books, right - left + 1)

print(max_books)


# Input:
# 4 5
# 3 1 2 1

# Output:
# 3