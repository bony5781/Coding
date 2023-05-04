#Kadanes Algorithm Pseudocode
# Initialize:
#     max_so_far = INT_MIN
#     max_ending_here = 0

# Loop for each element of the array

#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
#   (c) if(max_ending_here < 0)
#             max_ending_here = 0
# return max_so_far
from sys import maxsize
def maxSubArraySum(arr,N):
        maxSum = -maxsize -1;
        maxTempSum = 0;
        for i in range(0,N):
            maxTempSum += arr[i];
            
            if(maxSum<maxTempSum): maxSum=maxTempSum;
            if(maxTempSum<0): maxTempSum=0;
            
        return maxSum;

arr = [1,2,3,-2,5]
print(maxSubArraySum(arr,5))