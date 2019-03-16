def isSubstring(s1,s2):
    return s1 in s2

def isRotation(s1,s2):
    return isSubstring(s2,s1+s1)

print(isRotation("waterbottle","erbottlewat"))
