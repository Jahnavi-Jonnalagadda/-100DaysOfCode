def isAnagram(self, s, t):
        if(len(s) != len(t)):
            return False
        
        s = s.lower()
        t = t.lower()
        dct = {}
        for i in s:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        
        for i in t:
            if i in dct:
                dct[i] -= 1
                
        for item in dct:
            if(dct[item] != 0):
                return False
        return True
