coor = (10,20)

print(coor[0])
print(coor[1])

corlist = list(coor)
corlist[0] = 50
coor = tuple(corlist)
print(coor)