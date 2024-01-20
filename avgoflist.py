fh=open('output4.txt','w')
abc=[1,2,3,4,6,7,89]
sum=0
i=0
while(i<len(abc)):
    sum=sum+abc[i]
    i=i+1
avg=int(sum/len(abc))
print('the average is:', avg)
fh.write(f'the average of abc {avg}')