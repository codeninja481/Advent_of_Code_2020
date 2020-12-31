map = open("AdventofCode_Day3_Input.txt").read().split('\n')

xPos = 1
yPos = 1

mCount = 0
treeCount1 = 0

sList = [(3,1)]

xPos = 1
yPos = 1
for s in sList:
	for x in map:
		#if mCount > 21: break
		print(x)
		print(str(xPos) + ", " + str(yPos))
		if x[xPos-1] == "#": treeCount1 += 1
		xPos += s[0]
		yPos += s[1]
		if xPos > 31: xPos = xPos -31
	
	
	
		mCount += 1
	
print(treeCount1)
