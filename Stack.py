def createStack():
    stack = []
    size = input("Enter the size of stack: ")
    size = int(size)
    return size,stack
    
def insertStack(stack, s):
    le = len(stack)
    if le == s:
        print("Stack is full")
        return stack
    else:
        top = le+1
        n = input("Enter no of element: ")
        n = int(n)
        if n>s:
            print("Number of element is more than size of stack")
            return stack
        else:    
            x = le+n
            if x<=s:
                for j in range(le,x):
                    p = input("Enter element: ")
                    p = int(p)
                    stack.append(p)   
                return stack

def deleteStack(stack, s):
    le = len(stack)
    if le==0 or le=='None':
        print("Stack is already empty")
        return stack
    if le>0:
        val = input("Enter element you want to delete: ")
        val = int(val)
        if val in stack:
            index = stack.index(val)
            del(stack[index])
            return stack
        else:
            print("Element not found")
            return stack

def printStack(stack):
    return stack

while True:
    print("Enter your choice")
    print("1 for insert, 2 for delete, 3 for create new Stack, 4 for print Stack")
    x = input()
    x = int(x)
    if x==1:
        stack = insertStack(stack, s)
    if x==2:
        stack = deleteStack(stack, s)
    if x==3:
        s , stack = createStack()
    if x==4:
        stack = printStack(stack)
    
    if stack is None:
        print("Empty Stack")
    else:
        print("Stack", stack)
