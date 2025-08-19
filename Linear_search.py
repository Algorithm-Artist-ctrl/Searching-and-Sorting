def linear_search(arr, target):
    size=len(arr)
    for i in range(0,size):
        if arr[i]==target:
            return f"The input is find on {i} index"
    return f"Not found"
usr_input=input("Enter numbers separted by spaces:\n")
usr_list=list(map(int,usr_input.split()))
tar=int(input("Input the Number to search:\n"))
result=linear_search(usr_list,tar)
print(result)