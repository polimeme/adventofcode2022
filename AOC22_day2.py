f=open('input.txt','r')
r=f.readlines()


def rules(x1, x2):
    d = {}
    # if x1+x2 in ['AX','BY','CZ']:
    #   return 0
    pt = 0
    pt2=0
    if x2 == 'X':

        pt += 1
        pt2+=0
        if x1 == 'A':
            return pt + 3,pt2+3
        elif x1 == 'B':
            return pt + 0, pt2+1
        elif x1 == 'C':
            return pt + 6, pt2+2

    elif x2 == 'Y':
        pt += 2
        pt2 += 3
        if x1 == 'A':

            return pt + 6, pt2+1

        elif x1 == 'B':
            return pt + 3, pt2+2
        elif x1 == 'C':
            return pt + 0, pt2+3
    elif x2 == 'Z':
        pt += 3
        pt2+=6
        if x1 == 'A':
            return pt + 0,pt2+2
        elif x1 == 'B':
            return pt + 6,pt2+3
        elif x1 == 'C':
            return pt + 3,pt2+1
    return pt, pt2
x=0
x2=0
for n in range(len(r)):

    r[n]=r[n].replace('\n','').split()
    a,b=rules(r[n][0],r[n][1])
    x+=a
    x2+=b

print(x,x2)




