class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        else:
            sl = s.lower();
            tl = t.lower();
            for i in range(len(sl)):
                if sl[i] in tl:
                    tl = tl.replace(sl[i], '', 1);
                    continue;
                else:
                    return False;
                    break;
            return True;