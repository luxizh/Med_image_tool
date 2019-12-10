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

for '.DS_Store' in l:
     l.remove('.DS_Store')
len(l)