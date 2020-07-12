def print_rangoli(size):
    # your code goes here
    x=2*size-1
    y=(4*size-3)//2
    z=1
    for i in range(x):
        if(i<x//2):
            print(("-"*y),string2(96+size,i),("-"*y),sep="")
            y=y-2
        elif i==x//2:
            print(string2(96+size,i))
            z=(x//2)-1
        else:
            y=y+2
            #print(z)
            print(("-"*y),string2(96+size,z),("-"*y),sep="")
            z=z-1



def string2(n,n1):
    s=[chr(n)]
    for i in range(1,n1+1):
        s.append(chr(n-i))
    s.sort()
    x="-".join(s)
    s.reverse()
    y=s.copy()
    z="-".join(y)
    z=z+x[1:]
    return z
    
    
    #CALL THIS FUNCTION IN PROPER WAY IN MAIN PROGRAM
