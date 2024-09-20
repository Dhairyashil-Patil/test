
list=[1,2,3,4,5]
len=len(list)
avg=sum(list)/len
count=0
for i in list:
    
    if i > avg:
        
        count= count+1
print(count)
        
