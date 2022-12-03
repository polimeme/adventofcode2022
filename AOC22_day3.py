f=open('input.txt','r')
r=f.readlines()
for n in range(len(r)):
    r[n]=r[n].replace('\n','')
t=[]
for n in range(0,len(r)-1,3):

    t.append([r[n+0],r[n+1]])
    t.append([r[n+1],r[n+2]])
    t.append([r[n+2],r[n+0]])

for n in range(len(r)):
    r[n].replace('\n', '')
    r[n] = [r[n][:int(len(r[n]) / 2)], r[n][int(len(r[n]) / 2):]]



def side(l):
        v=0
        mem = []
        if len(l[0]) > len(l[1]):
            best = l[1]
            mirror = l[0]
        else:
            best = l[0]
            mirror = l[1]
        for elem in best:
            if elem in mirror and elem not in mem:
                if elem.lower() == elem:
                    v += (ord(elem) - 96)
                else:
                    v += (ord(elem) - 38)
                mem.append(elem)
        return v,mem
y=0
for elem in r:
    y+=side(elem)[0]
print('Parte 1:',y)


i=0
m=[]
mem2=[]
for elem in t:
    mem2=[]
    m.append(side(elem)[1])
    if len(m)==3:
        for k in m[0]:
            if k in m[1] and k in m[2] and k not in mem2:
                if k.lower() == k:
                    i += (ord(k) - 96)
                else:
                    i += (ord(k) - 38)
                mem2.append(k)
        m=[]

print('Parte 2:',i)



