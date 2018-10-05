def binarySearch(seq,key):
    lo = 0
    hi = len(seq)-1
    le = len(seq)
   
    
    while hi>=lo:
        mid = lo+(hi-lo)/2
        mid = int(mid)
        if key<seq[mid]:
            hi=mid-1
        if key>seq[mid]:
            lo=mid+1
        if key == seq[mid]:
            return mid
    return -1

        
key = input("Enter element to find: ")
key = int(key)
seq = [4,5,7,8,9]
res = binarySearch(seq, key)
if res>-1:
    print("Element found at index: ",res)
else:
    print("Element not found")