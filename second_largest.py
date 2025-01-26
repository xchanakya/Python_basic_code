def second_largest(arr):
    n=len(arr)
    arr.sort()

    for i in range(n-2,1,-1):
        if arr[i]!=arr[n-1]:
            return arr[i]


arr = [1, 2, 3, 4, 5]
print(second_largest(arr)) # 4



def third_largest(arr):
    n=len(arr)

    first=arr[0]
    for i in range(1,n):
        if arr[i]>first:
            first=arr[i]
    
    second=arr[0]
    for i in range(1,n):
        if arr[i]>second and arr[i]<first:
            second=arr[i]

    third_largest=arr[0]
    for i in range(1,n):
        if arr[i]>third_largest and arr[i]<second:
            third_largest=arr[i]

    return third_largest


        
arr = [1, 2, 3, 4, 5]
print(third_largest(arr)) # 3