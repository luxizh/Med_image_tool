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
'''
with open('A.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    rows= [row for row in reader]
with open('A.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[2] for row in reader]
with open('A.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row for row in reader]
'''
'''
import csv
filnename='/Users/luxi/Desktop/Tencent-intern/med_image/test1/summary.csv'
with open(filnename) as f:
    f_reader=csv.reader(f)
    h=next(f_reader)
    rows=[row for row in f_reader]
    print(h)
    print(rows)
    '''
'''
import os
root='/Users/luxi/Desktop/Tencent-intern/med_image/test1'
print(os.path.basename(root))
'''
'''
l=[['a','b','1','3'],['c','b','1','2'],['z']]
l.sort()
print(l)
'''
import pickle
f=open('todo.pkl','rb')
print(pickle.load(f))
f.close()