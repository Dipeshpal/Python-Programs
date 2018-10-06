#BubbleSort

#List of Element
ele = [7,2,4,8,5]

#Bubble Sort Start
def bubbleSort(ele):
    length = len(ele)
    for i in range(0,length-1):
        if ele[i]>ele[i+1]:
            ele[i], ele[i+1] = swap(ele[i], ele[i+1])
            
def swap(x,y):
    return y, x
    
#function calling
bubbleSort(ele)
print("Sorted List: ", ele)