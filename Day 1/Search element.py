arr=[6,5,4,3,2,7]
target=3
found=False
index=0
for num in arr:
    if num==target:
        found=True
        print(index)
    index=index+1
if found:
    print("element found")
else:
    print("element not found")

