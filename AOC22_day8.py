f=open('input.txt','r')
r=f.readlines()
for n in range(len(r)):
    r[n]=list(r[n].replace('\n',''))
    for k in range(len(r[n])):
        r[n][k]=int(r[n][k])


def scenic(n,k,r):
    h=[]
    left = r[n][:k][::-1]
    top = [int(r[i][k]) for i in range(n)][::-1]
    right = r[n][k + 1:]
    down = [int(r[i][k]) for i in range(n + 1, len(r))]
    for elem1 in [left,top,right,down]:
        x=0
        for elem2 in elem1:
            x+=1
            if r[n][k]<=elem2:
                break
        h.append(int(x))
    i=1
    for elem in h:
        i*=elem
    return i




def visible(n,k,r):
    left=r[n][:k]
    top=[int(r[i][k]) for i in range(n)]
    right=r[n][k+1:]
    down=[int(r[i][k]) for i in range(n+1,len(r))]
    for elem1 in [left,top,right,down]:
        v=True
        for elem2 in elem1:
            if elem2>=r[n][k]:
                v=False
        if v==True:
            return True
    return False

def eight(r):
    h=[]
    gg=[]
    for n in range(len(r)):
        if n>0 and n<len(r)-1:
            for k in range(len(r)):
                if k>0 and k<len(r)-1:
                    if visible(n,k,r)==True:
                        h.append(r[n][k])
                    gg.append(scenic(n,k,r))
    return h,gg

print('Parte 1:',len(eight(r)[0])+(len(r)-1)*4)
print('Parte 2:',max(eight(r)[1]))
