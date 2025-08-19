def binary_search(arr,target):
    size=len(arr)
    end=size-1
    start=0
    while(start <=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return f"Found at index {mid}"
        elif arr[mid]<target:
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
        else:
            pass
    return -1
usr_input=input("Enter the numbers separeted by spaces:\n")
usr_list=list(map(int,usr_input.split()))
tar=int(input("Input the Number to find:\n"))
result=binary_search(usr_list,tar)
print(result)