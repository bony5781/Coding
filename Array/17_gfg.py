def merge(arr1,arr2):
    i,j=len(arr1)-1,0
    while i>=0 and j<len(arr2):
        if(arr1[i]>arr2[j]):
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i -= 1
            j += 1
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1,arr2

arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
print(merge(arr1,arr2))