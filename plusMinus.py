def plusMinus(arr):
    print(len([arr[i] for i in range(0,len(arr)) if arr[i]>0 ])/len(arr))
    print(len([arr[i] for i in range(0,len(arr)) if arr[i]<0 ])/len(arr))
    print(len([arr[i] for i in range(0,len(arr)) if arr[i]==0 ])/len(arr))
    
