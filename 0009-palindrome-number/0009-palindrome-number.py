class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        n = x
        reverse = 0
        while 0 < n:
            reminder = (n % 10)
            reverse = (reverse * 10) + reminder
            n = n // 10
        if reverse == x:
            return True
        else:
            return False


        