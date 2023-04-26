fname = input("Enter a name ")
fname = list(fname)
i = 0
j = len(fname)-1
while i < j:
    (fname[i],fname[j])=(fname[j],fname[i])
    i += 1
    j -= 1
print(fname)