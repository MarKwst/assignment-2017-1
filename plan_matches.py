import sys
input_filename = "example_graph_1.txt"

g = {} # fteiaxnw arxika ton graph mou apo to .txt se ena dictionairy
with open(input_filename) as graph_input:
    for line in graph_input:
        nodes = [str(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in g: g[nodes[0]] = []
        if nodes[1] not in g: g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
        
pairs = [] # mia lista me ta zevgaria paiktwn
for node in g:
    for neighbour in g[node]:
        pairs.append((node, neighbour))

S ={}# edw 8a ekxwrw ws value ta zevgh sth mera p 8a paizoun mera=key
for i in range(len(pairs)):
    for z in pairs[i]:
        if (pairs[i] not in S.values()):
            S[i]=pairs[i]
        else:
            S[i+1]=pairs[i]

for day, pair in S.items():
    print('{0} {1}'.format(pair,day))
