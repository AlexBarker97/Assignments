#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A2_3

######## Your Code Below ########
import assignment2_a2_2 as a22
ListofElements = [0,46,92,52,68,22,64,62,1,2,3,18,19,108,105,104,61]
ListofElements.sort()
print(ListofElements)
x = float(input("Give number: "))
n = len(ListofElements)
F = a22.fibonacci(n)
p = len(F)
k = F[p-1]

def fibonacciAlgorithm(x,k=k,p=p,F=F,ListofElements=ListofElements,offset=0):

    if k == 0:
        print("not in list")
    elif F[p-2]+offset > len(ListofElements)-1:
        p = p - 1
        k = F[p - 1]
        fibonacciAlgorithm(x,k,p,F,ListofElements,offset)
    else:
        index = ListofElements[F[p-2] + offset]
    if x == index:
            print(x,"found at: ",F[p-2] + offset)
    elif x < index:
        p = p - 1
        k = F[p - 1]
        fibonacciAlgorithm(x,k,p,F,ListofElements,offset)
    elif x > index:
        offset+=F[p-2]
        p = p - 2
        if p>0:
          k = F[p - 1]
        else:
          k=0
        fibonacciAlgorithm(x,k,p,F,ListofElements,offset)

fibonacciAlgorithm(x)