'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# Stack is empty when top is -1
def isEmpty():    
    #---- complete the code
    return top == -1 

# Stack is full when top reaches stack_size-1
def isFull():
    #---- complete the code
    return top ==stack_size-1 


# Function to add an item to stack. It increases size by 1
def push(item):
    global stack, top           #required in Python if we're modifying a global variable
    
    #---- complete the code      
    if isFull():
        print("Error: Stack is full.")      
    else:
        top = top+1
        stack[top]=item
        print(f'Pushed {item} OK!')  

# Function to remove an item from stack. It decreases size by 1
def pop():
    global top
    #---- complete the code
    if isEmpty():
        print('Error: Nothing to pop. Stack is already empty.')
        return None
    else:
        temp=stack[top]
        top = top - 1 
    return temp
 

# Function to return the top from stack without removing it
def peek():    
    if isEmpty():
        return None
    return stack[top]


# Function to print the stack contents with last item on top
def printStack():
    if isEmpty():
        print('Stack is empty')
    else:
        print(f'| {stack[top]} |<-TOP')    
        for i in range(top-1, -1, -1):
            print(f'| {stack[i]} |')    
    print()


'''
Global variables
'''
stack_size = 5                  #set stack_size here
stack = [None]*stack_size       #stack is a global variable
top = -1                        #top pointing to the current top item, initially -1


'''
Driver code - test the stack operations here
'''
push('a')
push('b')
push('c')
printStack()

print('Removing:', pop())
printStack()

push('d')
push('e')
push('f')
push('g')
printStack()

pop()
pop()
printStack()

push('g')
printStack()

pop()
pop()
pop()
printStack()

pop()
printStack()

pop()