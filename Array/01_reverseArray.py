a = [3,2,7,2,78,1]
# print(a[::-1]) Easy Sol
i = 0 
j = len(a)-1
while i < j:
    (a[i],a[j])=(a[j],a[i])
    i += 1
    j -= 1
print(a)