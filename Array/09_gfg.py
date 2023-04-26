def sort012(arr,n):
        if(n==0 or n==1):
            return arr;
            
        c0 = 0 ; c1 = 0; c2 = 0;
        #Count no. of 0's and 1 and 2's
        for i in range(0,n):
            print(arr[i])
            if(arr[i]==0):
                c0 += 1;
            elif arr[i]==1:
                c1 += 1;
            else:
                c2 += 1;
        
        #Modify array
        temp = 0;
        for p in range(0,c0):
            arr[p] = 0;
            temp = p;
        
        temp = temp + 1;
        for q in range(0,c1):
            arr[temp] = 1;
            temp += 1;
            
        
        for r in range(0,c2):
            arr[temp] = 2;
            temp += 1;

        return arr;

arr = [0,2,1,2,1,0];
print(sort012(arr,len(arr)));