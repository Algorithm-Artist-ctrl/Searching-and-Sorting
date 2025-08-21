def Selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if (arr[j]<arr[min_index]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
usr_input=input("Input numbers separeted by spaces: ")
usr_list=list(map(int,usr_input.split()))
result=Selection_sort(usr_list)
print(result)
    