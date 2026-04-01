class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        mystr = ""
        for i in range(len(s)):
            if s[i] in "abcdefghijklmnopqrstuvwxyz" or s[i] in "1234567890":
                mystr += s[i];
            else:
                 continue;
        palin = mystr[::-1]
        if palin == mystr:
            return True
        else: return False