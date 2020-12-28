map = open("AdventofCode_Day3_Input.txt").read().split('\n')

#sList = [(1,1), (3,1), (5,1), (7,1), (1,2)]
sList = [(3,1)]

treeCounter = 0

treeCount = []
treeCount = [0 for i in range(5)]
#print(treeCount)

mCount = 0
print(len(map))

def FindTrees(slope, linelen):
	x_motion = 2
	y_motion = 1
	x_pos = 0
	y_pos = 0
	trees = 0
	while x_pos < len(slope):
		if y_pos >= linelen:
			y_pos = y_pos - linelen
		currentline = slope[x_pos]
		pathchar = currentline[y_pos]
		x_pos += x_motion
		y_pos += y_motion
		if pathchar == '#':
			trees += 1
	return trees
	
current = FindTrees(map, len(map[0]))
print(current)

"""
for s in sList:
	treeCount[treeCounter] = 0
	xPos = yPos = 0
	print("Stage " + str(treeCounter) + ": R" + str(s[0]) + "D" + str(s[1]))
	for x in map:
		#if mCount > 21: break
		if yPos != 1: next
		#print(x)
		#print("length: " + str(len(x)))
		print(str(xPos) + ", " + str(yPos))
		if x[xPos-1] == "#": treeCount[treeCounter] += 1
		xPos += s[0]
		yPos += s[1]
		if xPos > 31: xPos = xPos -31
		if yPos > len(map): break
		#if xPos > 66: xPos = xPos -66
		#print(x[xPos-1])
		#print(xPos-1)
		#print(treeCount[treeCounter])

		mCount += 1
	treeCounter += 1

print("Tree Count1: " + str(treeCount[0]))
print("Tree Count2: " + str(treeCount[1]))
print("Tree Count3: " + str(treeCount[2]))
print("Tree Count4: " + str(treeCount[3]))
print("Tree Count5: " + str(treeCount[4]))
print("Total: " + str(treeCount[0]*treeCount[1]*treeCount[2]*treeCount[3]*treeCount[4]))
"""
print("NOT THE ANSWER!! Total: 17221234068")
print("NOT THE ANSWER!! Total: 4169028864")
#3847183340
#17221234068
#9354744432
#4169028864
#3827795328