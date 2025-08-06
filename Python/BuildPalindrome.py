# Build the shortest palindrome by adding characters at the end

def is_palindrome(s):
    return s == s[::-1]

def build_palindrome(s):
    for i in range(len(s)):
        if is_palindrome(s[i:]):
            return s + s[:i][::-1]


s=input("Enter string : ")
print(build_palindrome(s))

# Input : abc
# Output : abcba

# Intput :race
# Output :racecar

