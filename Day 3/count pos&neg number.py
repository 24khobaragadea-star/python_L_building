arr=[-1,3,4,-2,5,1,2,-9]

positive=0
negative=0
for num in arr:
    if num>0:
        positive=positive+1
    else:
        num<0
        negative=negative+1

print("positive count is : ",positive)
print("negative count is : ",negative)
