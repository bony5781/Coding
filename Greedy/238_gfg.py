#Activity Selector algorithm

#Finshing time must be sorted
def maxJobs(n,start,end):
    #first job always counts
    i=0
    # If this activity has start time greater than
    # or equal to the finish time of previously
    # selected activity, then select it
    for j in range(1,n):
        if start[j]>=end[i]:
            print(f"{j} ",end="")
            i=j

def maximumMeetings(n,start,end):
        meeting=[(start[i],end[i]) for i in range(n)]
        
        meeting.sort(key=lambda a:a[1])
        
        count=1
        ansEnd=meeting[0][1]
        
        for i in range(1,n):
            if meeting[i][0]>ansEnd:
                count+=1
                ansEnd=meeting[i][1]
        return count

N = 6
start = [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]
maxJobs(N,start,end)
print(maximumMeetings(N,start,end))
