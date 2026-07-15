class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = s.lower()
        i, j = 0, len(c) - 1

        while i < j:
            while i < j and not c[i].isalnum():
                i += 1
            while i < j and not c[j].isalnum():
                j -= 1

            if c[i] != c[j]:
                return False

            i += 1
            j -= 1

        return True
