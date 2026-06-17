arr=[1,2,3,1,6,7,2]
seen=[]

for num in arr:
    if num in seen :
        print("duplicate found : ",num)
       
    else:
        seen.append(num)
   
# PATTERN I LEARNT IN THIS :Remember previously seen elements 