def check_for_duplicates(s): #True means there are duplicate characters in the string
    characters = [False] * 256

    for c in s:
        val = ord(c)
        if characters[val] != False: return True
        characters[ord(c)] = True
            
    return False


print(check_for_duplicates("abcdefghijklmnopqrstuvxwyz"))
print(check_for_duplicates("açojehfoweuytoyoutysiugtiusgi"))
print(check_for_duplicates("237875926579346597364563974"))
print(check_for_duplicates("aAbBcCdD"))
