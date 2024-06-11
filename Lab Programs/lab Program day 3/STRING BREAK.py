def checkIfCanBreak(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    
    def canBreak(a, b):
        return all(x >= y for x, y in zip(a, b))
    
    return canBreak(s1, s2) or canBreak(s2, s1)


s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2))  
