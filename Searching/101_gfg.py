def find(arr, n, x):
    if n == 0:
        return [-1, -1]

    res = []
    for i in range(n):
        if (arr[i] == x):
            res.append(i)

    if (len(res) == 0):
        return [-1, -1]

    return [res[0], res[-1]]


l = [1, 3, 5, 5, 5, 5, 67, 123, 125]
print(find(l,len(l),5))