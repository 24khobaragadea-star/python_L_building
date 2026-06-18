arr=[1,2,3,5,6]

index=0

for num in arr[:-1]:
    if arr[index]+1!=arr[index+1]:
        
        break
    index=index+1

print("missing value : ", arr[index]+1)
