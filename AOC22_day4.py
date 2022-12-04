f=open('input.txt','r')
r=f.readlines()
for n in range(len(r)):
    r[n]=r[n].replace('\n','').split(',')
    for k in range(len(r[n])):
        r[n][k]=r[n][k].split('-')
        r[n][k][0]=int(r[n][k][0])
        r[n][k][1] = int(r[n][k][1])


def spadaro(l):
    pt1,pt2=0,0
    l=list(sorted(l))
    l1,l2=l[0],l[1]
    if l1[0]==l2[0]:
        if l2[1]>l1[1]:
            l1=l[1]
            l2=l[0]

    if l1[0]<=l2[0] and l1[1]>=l2[1]:
        pt1=1

    if l1[0]<l2[0] and l2[0]>l1[1]:
        pt2=1
    return pt1,pt2
i=0
i2=0
for elem in r:
    i+=(spadaro(elem))[0]
    i2+=(spadaro(elem))[1]

print('Parte 1:',i)
print('Parte 2:',1000-i2)



