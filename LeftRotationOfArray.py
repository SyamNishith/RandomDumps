def Reverse (arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
arr=list(map(int,input().split()))
Rotations=int(input("Enter the Rotations Required:"))
Rotations=Rotations%len(arr)
print("Before Rotation:",arr)
Reverse(arr, 0, Rotations-1)
Reverse(arr,Rotations, len(arr)-1)
Reverse(arr, 0, len(arr)-1)
print("After Rotation:",arr)

