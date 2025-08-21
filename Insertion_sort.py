def Insertion_sort(arr):
    size=len(arr)
    for i in range(1,size):
        t=arr[i]
        j=i-1
        while(j>=0 and t<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=t
    return arr
usr_input=input("Input numbers separeted by spaces: ")
usr_list=list(map(int,usr_input.split()))
result=Insertion_sort(usr_list)
print(result)
    