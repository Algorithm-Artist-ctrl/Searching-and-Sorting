def bubble_sort(arr):
    size=len(arr)
    for i in range(size):
        for j in range(size-i-1):
            if arr[j]>arr[j+1]:
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
    return arr
usr_input=input("Input numbers separeted by spaces: ")
usr_list=list(map(int,usr_input.split()))
result=bubble_sort(usr_list)
print(result)
    