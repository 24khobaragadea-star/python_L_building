arr1=[1,2,3,4,9]
arr2=[1,2,6,7,9]
seen=[]

for num in arr1:
    seen.append(num)
print(seen)

for num in arr2:
    if num not in seen:
        seen.append(num)
    else:
        print(num)
