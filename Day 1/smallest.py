arr=[1,2,3,5,9,6]

smallest=arr[0]
for num in arr:
    if num<smallest:
        smallest=num
print(smallest)