class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        left = 0
        best = 0

        for right, char in enumerate(s):

            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right

            current_len = (right - left) + 1

            best = max(current_len, best)

        return best
        