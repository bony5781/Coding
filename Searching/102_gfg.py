def valueEqualToIndex(arr, n):
    ans = []
    for i in range(n):
        if (arr[i] == i+1):
            ans.append(i+1)
    return ans

print(valueEqualToIndex([15,2,3,12,7],5))