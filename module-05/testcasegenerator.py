import math
import random as r
#___________________________________________________________
#|  Test Case Generator for Wiring Lab                     |
#|                                                         |
#|  Input: "Num_of_veticies Num_of_edges"                  |
#|  Example Input: "4 5" or "25 31"                        |
#|                                                         |
#|  Output: A valid wiring testcase to try on your code    |
#|                                                         |
#|  Make sure you send output to a file when using         |
#|  Example: "python3 wiring.py > output.txt"              |
#l_________________________________________________________|

testcase = input().split(' ')
verticies = int(testcase[0])
edges = int(testcase[1])
if (verticies < 2):
    print('Enter more than 1 edges for a valid test case')
    quit()
if (edges > int(((verticies)*(verticies-1))/2)):
    print('Too many edges. Maximum edges for', verticies,'verticies is', int(((verticies)*(verticies-1))/2))
    quit()

names = []
names.append("b1 breaker")

box = 1
outlet = 1
switch = 1
light = 1
i = 0
while i < verticies-1:
    case = r.randrange(1,4,1)
    if (case == 1):
        names.append(("o"+str(outlet)+" outlet"))
        outlet += 1
        i += 1
    if (case == 2):
        names.append(("j"+str(box)+" box"))
        outlet += 1
        i += 1
    if (case == 3):
        names.append(("s"+str(switch)+" switch"))
        switch += 1
        i += 1
        lightNum = min(r.randrange(1,verticies-i+1,1),r.randrange(1,10,1))
        for j in range(lightNum):
            if (i >= verticies-1):
                break
            names.append(("l" + str(light) + " light"))
            light += 1
            i += 1
    

duplicates = set()
connections = []
namesLen = len(names)
finalEdges = 0
for e in range (edges):
    cost = r.randrange(1,10,1)
    n1 = r.randrange(0,namesLen,1)
    n2 = r.randrange(0,namesLen,1)
    if (n1 == n2):
        continue

    node1 = (names[n1].split(' '))[0]
    node2 = (names[n2].split(' '))[0]
    if ((node1, node2) in connections or (node2, node1) in connections):
        continue
    connections.append((node1 + " " + node2 + " "+ str(cost)))
    finalEdges += 1
print(verticies, finalEdges)
for name in names:
    print(name)
for connection in connections:
    print(connection)