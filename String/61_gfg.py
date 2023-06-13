def validShuffle(str1,str2):
    n = len(str1)
    m = len(str2)

    if(n > m):
        return False
    
    str1 = sorted(str1)
    for i in range(m):
        if (i + n - 1 >= m):
            return False
        
        str = ""
        for j in range(n):
            str += str2[i+j]

        str = sorted(str)
        if(str == str1):
            return True
    
if(validShuffle("onetwofour","hellofourtwooneworld")):
    print("Valid Shuffle")
else:
    print("Not a valid shuffle")
        
    