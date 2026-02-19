
def block_list(length):
    # creates a list of all non-increasing blocks.  
    # a block will form a block of voids in one corner of a puzzle.
    # a block is non-increasing if the number of voids in each subsequent row is less than or equal to the previous
    d=length #here we set the length to the dimension of the puzzle minus the minimum word length
    c=0  #this is a counter to terminate the run if it goes too long
    L=[] #the element being generated at any point
    K=[] #the list of all of the elements
    i=d-1
    for k in range(d):
        L.append(d)
    while i>-1 and c<10000 and L[0]>0:
        if L[i]==0:
            i-=1
            c+=1
        if L[i]>1:
            #print(L,'a',i)
            K.append([L[z] for z in range(d)])
            L[i]-=1
            for j in range(i,d):
                L[j]=L[i]
            i=d-1
            c+=1
        if L[i]==1:
            #print(L,'b',i)
            K.append([L[z] for z in range(d)])
            L[i]-=1
            #print(L,'c',i,L[i-1])
            K.append([L[z] for z in range(d)])
            if L[0]==0:
                break
            if L[i-1]>1:
                L[i-1]-=1
                for j in range(i-1,d):
                    L[j]=L[i-1]
                c+=1
                i=d-1
            else:
                L[i-1]-=1
                #print(L,'d',i,L[i-1])
                K.append([L[z] for z in range(d)])
                L[i-2]-=1    
                for j in range(i-2,d):
                    L[j]=L[i-2]    
                if L[0]==0:
                    #print(L,'e',i)
                    K.append([L[z] for z in range(d)])
                    break
                else:
                    i=d-1
                    c+=1
            c+=1
    return K


##Example counting https://oeis.org/A000984
#for i in range(1,7):
#    print(i,len(block_list(i)))

def nonzero(L): #counts the non-zero elements in a list
    return sum(x != 0 for x in L)

def list_pairs(d): #lists all compatible pairs of blocks for size d
    c=1
    for x in block_list(d):
        for y in block_list(d):
            if x[0]+y[0]<=d and nonzero(x)+nonzero(y)<=d:
                print(c,x,y)
                c+=1
               
def count_pairs(d): #counts all compatible pairs of blocks for size d
    c=0
    for x in block_list(d):
        for y in block_list(d):
            if x[0]+y[0]<=d and nonzero(x)+nonzero(y)<=d:
                c+=1
    print(c)
   
# Example counting https://oeis.org/A092443
for i in range(1,7):
    count_pairs(i)
