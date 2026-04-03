class Solution(object):
    def isAnagram(self, s, t):

        if (len(s) != len(t)):
            return False

        seen = {}

        for w in s:
            if w not in seen:
                seen[w] = 1
            else:
                seen[w] += 1
        


        for w in t:
            if w not in seen:
                return False

            seen[w] -= 1

            if seen[w] < 0 :
                return False

            
        return True


        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        