arr=[1,2,3,4,5,6]
largest=arr[0]
smallest =arr[0]
for num in arr:
    if num>largest:
        largest=num


for num in arr:
    if num<smallest:
        smallest = num 

print(largest-smallest)