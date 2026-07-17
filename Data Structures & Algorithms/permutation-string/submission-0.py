class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        freq = defaultdict(int)

        for ch in s1: 
            freq[ch] += 1

        for i in range(len(s2)):
            freq[s2[i]] -= 1

            if i-len(s1) >= 0:
                freq[s2[i-len(s1)]] += 1

            if all([t==0 for t in freq.values()]):
                return True
        return False