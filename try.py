from sys import maxsize

def maxSubArraySum(arr,N):
    sum=-maxsize-1; tempSum=0;
    for i in range(N):
        tempSum += arr[i]
        if(tempSum < 0):
            tempSum = 0
        if(tempSum > sum):
            sum = tempSum
    return sum

arr=[1,2,3,-2,5]
print(maxSubArraySum((arr),len(arr)-1))