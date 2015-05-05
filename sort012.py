# Sort a list of 0's, 1's and 2's

def swap(l,x,y):
    temp = l[x]
    l[x] = l[y]
    l[y] = temp
    return l


l = [0,1,1,0,1,2,1,2,0,0,0,1]
l = [2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

left = 0
right = len(l) - 1

x = 0
while x < len(l): 
    y = l[x]
    if y == 0 and x > left:
        l = swap(l,x,left)
        left += 1
        x -= 1
    if y == 2 and x < right:
        l = swap(l,x,right)
        right -= 1
        x -= 1
    x += 1

print l
