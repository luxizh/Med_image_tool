'''
a='1.1'
b='1'
l1=a.partition('.')
l2=b.partition('.')
print(l1)
print(l2)
c='new'
print(c+l1[1]+l1[2])
print(c+l2[1]+l2[2])
'''

'''
while '.DS_Store' in l:
     l.remove('.DS_Store')
len(l)
'''
'''
import csv
f=open('sum.csv','rt')
f_csv=csv.reader(f)
print(type(f_csv))
h=next(f_csv)
print(h)
for r in f_csv:
    print(r)
f.close()

t='a'
f=open('sum.csv',t,newline='')
w_csv=csv.writer(f)
#l=[[col*row for col in range(4)] for row in range(5)]
#w_csv.writerows(l)
w_csv.writerow([1,2,3,4])
f.close()
'''
import os
root='/Users/luxi/Desktop/Tencent-intern/med_image/test1'
print(os.path.basename(root))