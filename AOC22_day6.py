f=open('input.txt','r')
r=f.readline()
print(r)
#per parte 2 sostituire i 4 con 14
def ez(r):
    for n in range(0,len(r)-14):
        if len(list(set(list(r[n:n+14]))))==14:
            return n+14
print(ez(r))
