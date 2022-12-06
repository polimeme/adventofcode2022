f=open('input.txt','r')
r=f.readline()
print(r)
#per parte 2 sostituire i 4 con 14
def ez(r):
    for n in range(0,len(r)-4):
        if len(list(set(list(r[n:n+4]))))==4:
            return n+4
print(ez(r))
