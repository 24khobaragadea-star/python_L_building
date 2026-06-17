arr=[2,3,4,8,7,6,1]

sorted_arr=True
index=0
for num in arr[:6]:
    if arr[index]>arr[index+1]:
        sorted_arr=False
    index=index+1
        

if sorted_arr:
    print("array is sorted",sorted_arr)
else:
    print("unsorted")