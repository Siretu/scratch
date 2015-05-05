# Check if a string can be rearranged to a palindrome.

def check_anadrome(s):
    char_count = {}
    for c in s:
        if c not in char_count:
            char_count[c] = 0
        char_count[c] = char_count[c] + 1
    odd = len([1 for x in char_count.values() if x % 2 == 1])
    if len(s) % 2  == 0:
        return odd == 0
    return odd == 1
        
    
        
        
