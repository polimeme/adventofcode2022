f = open('input.txt', 'r')
r = f.readlines()
for n in range(len(r)):
    r[n] = r[n].replace('    ', ' ')
    r[n] = r[n].split(' ')
    if r[n] == ['\n']:
        x = n
l = r[:x - 1][::-1]
print(l)
h = []
for n in range(9):
    h.append([])
for n in range(len(l)):
    for k in range(len(l[n])):
        l[n][k] = l[n][k].replace('[', '').replace(']', '').replace('\n', '')
        if l[n][k] != '':
            h[k].append(l[n][k])

ist = r[x + 1:]

for n in range(len(ist)):
    q = int(ist[n][1])
    part = int(ist[n][3]) - 1
    dest = int(ist[n][5][0]) - 1
    cargo = h[part][-q:][::-1]  # FOR PART2 JUST REMOVE [::-1]
    h[part] = h[part][:-q]
    h[dest] += cargo

s = ''
for elem in h:
    if len(elem) > 0:
        s += elem[-1]
print(s)



