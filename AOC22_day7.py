f=open('input.txt','r')
r=f.readlines()
for n in range(len(r)):
    r[n]=r[n].split()


def priority(r):
    d={}
    dir=[]
    x=False
    files=[]
    mem=["/"]
    for n in range(len(r)):
        if r[n][0]=='$':
            if r[n][1]=='cd':
                if r[n][2]=='..':
                    mem=mem[:-1]
                    current=mem[-1]
                else:
                    if r[n][2]=='/':
                        current = r[n][2]
                    else:
                        current =mem[-1]+'.'+r[n][2]
                    mem.append(current)
                    dir.append(current)

                    if current not in d.keys():
                        d[current] = []
                        
            if r[n][1]=='ls':
                x=True
            else:
                x=False

        elif x==True :
            r[n][1]=str(current)+'.'+r[n][1]
            d[current].append(r[n][1])
            if r[n][0]=='dir':
                dir.append(r[n][1])
            else:
                files.append(r[n][1])
            if r[n][1] not in d.keys() and r[n][0]!='dir':
                d[r[n][1]]=[]
                d[r[n][1]].append(r[n][0])
    return d,dir,files

def paz(elem,d,files,dir):
    s=0
    for k in d[elem]:
        if k in files:
            s+=int(d[k][0])
        else:
            s+=paz(k,d,files,dir)
    return s


def value(d,dir,files):
    h={}
    for elem in dir:
        h[elem]=paz(elem,d,files,dir)
    return h


df,dirf,filesf=(priority(r))

pt1=0
l=(value(df,dirf,filesf))
gg=[]
for elem in l.values():
    if elem<=100000:
        pt1+=elem

print('Parte 1:', pt1)

for elem in l.keys():
    gg.append([l[elem],elem])
gg=sorted(gg)
for elem in gg:
    if 70000000-(l['/']-elem[0])>=30000000:
        print('Parte 2:',elem)
        break



