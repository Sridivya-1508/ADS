def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        m=a[i]
        j=i-1
        while(j>=0 and a[j]>m):
            a[j+1]=a[j]
            j-=1
        a[j+1]=m    
    return a    


n=int(input("Enter no.of Elements:"))
a=[]
c=0
while c<n:
    try:
        t= int(input())
        a.append(t)
        c+=1
    except:
        print("enter input value")
sortedArray=insertionSort(a)
print(sortedArray)
