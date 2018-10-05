#BinarySearch
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

#LinearSearch
def linearSearch(seq, key):
    le = len(seq)
    for i in range(le):
        if key==seq[i]:
            return i
    return -1 
    
key = input("Enter element to find: ")
key = int(key)
seq = [4,5,7,8,9]
ch = input("Press 1 for Binary Search, 2 for Linear Search: ")
ch = int(ch)

if ch==1:
    res = binarySearch(seq, key)
if ch==2:
    res = linearSearch(seq, key)

if res > -1:
    print("Element found at index: ", res)
    print("Complexity of Linear Search is O(n)")
    print("Complexity of Binart Search is O(logn)")
else:
    print("Element not found")
