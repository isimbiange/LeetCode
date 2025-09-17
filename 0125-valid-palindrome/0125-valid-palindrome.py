class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []

        for char in s:
            if char.isalnum():
                filtered.append(char.lower())
        cleaned = "".join(filtered)

        return cleaned == cleaned[::-1]
        
        