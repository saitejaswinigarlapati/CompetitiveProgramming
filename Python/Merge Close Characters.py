from collections import Counter

class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        result = []
        lastk = Counter()

        for char in s:
            # If character already appeared in last k positions, skip it
            if lastk[char] > 0:
                continue

            # Add character to result
            result.append(char)
            lastk[char] += 1

            # Maintain only last k characters
            if len(result) > k:
                drop = result[-k - 1]
                lastk[drop] -= 1

        return "".join(result)


# Example run
s = "abacaba"
k = 2

sol = Solution()
print("Input:", s, "k =", k)
print("Output:", sol.mergeCharacters(s, k))