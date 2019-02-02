import queue
from copy import copy, deepcopy
from colorama import init, Fore, Back
from Point import Point
from StepItem import StepItem
init(convert=True)

def printMap(map, h, w, stack):
	# if stack exists, append to stepList
	# stack of shortest path points
	stepList = []	
	for i in stack.queue:
		stepList.append(i.point)
	for y in range(h):
		for x in range(w):
			printed = False
			elem = str(map[y][x])
			# red for barrier
			if elem == 'x':
				print("%s%s%3s"%(Fore.WHITE, Back.RED, elem), end=" ")
			else:
				# blue for shortest path
				elemPoint = Point(y, x)
				for stepPoint in stepList:
					if stepPoint.equals(elemPoint):
						print("%s%s%3s"%(Fore.WHITE, Back.BLUE, elem), end=" ")
						printed = True
				# green for path
				if not printed:
					print("%s%s%3s"%(Fore.WHITE, Back.GREEN, elem), end=" ")
		print()
	print()

# test maze
maze = [
	['A','b','b','x','b','b','b','x','a'],
	['b','x','b','x','b','x','b','x','b'],
	['b','x','b','x','b','x','b','x','b'],
	['b','x','b','x','b','x','b','x','b'],
	['b','x','b','x','b','x','b','x','b'],
	['b','x','b','x','b','x','b','x','b'],
	['b','x','b','b','b','x','b','b','b'],
	['b','x','x','x','x','x','x','x','b'],
	['b','b','b','b','b','b','b','b','b'],
]
# height and width of maze
height = len(maze)
width = len(maze[0])

# find startPoint and endPoint
for y in range(height):
	for x in range(width):
		if (maze[y][x] == 'A'):
			startPoint = Point(y, x)
		if (maze[y][x] == 'a'):
			endPoint = Point(y, x)

# prepare minimum distance map stepMap
stepMap = deepcopy(maze)
printMap(stepMap, height, width, queue.Queue())

# write all points' minimun distance on step map
# push visited points to step stack
stepStack = queue.LifoQueue()
q = queue.Queue()
startQItem = StepItem(startPoint, 0)
q.put(startQItem)
success = False
while q.qsize() > 0:
	item = q.get()
	if isinstance(stepMap[item.point.y][item.point.x], int) and stepMap[item.point.y][item.point.x] <= item.step:
		continue
	stepMap[item.point.y][item.point.x] = item.step
	stepStack.put(item)
	if item.point.equals(endPoint):
		success = True
		break
	neighbourList = item.point.neighbour()
	for nextPoint in neighbourList:
		if nextPoint.y < height and nextPoint.y >= 0 and nextPoint.x < width and nextPoint.x >= 0 and stepMap[nextPoint.y][nextPoint.x] != 'x':
			q.put(StepItem(nextPoint, item.step + 1))
# no possible route exit
if not success:
	print("%s%sNo possible route."%(Fore.WHITE, Back.BLACK))
	exit(0)

# back tracking
# pop step stack
# push path from end to start
pathStack = queue.LifoQueue()
item = stepStack.get()
currentPoint = item.point
currentStep = item.step
pathStack.put(item)
while stepStack.qsize() > 0:
	item = stepStack.get()
	if currentStep > item.step:
		neighbourList = item.point.neighbour()
		for nextPoint in neighbourList:
			if currentPoint.equals(nextPoint):
				pathStack.put(item)
				currentPoint = item.point
				currentStep = item.step
# print shortest path on map
printMap(stepMap, height, width, pathStack)

# pop path stack print path coordinates
while pathStack.qsize() > 0:
	item = pathStack.get()
	print("%s%s[%s,%s]"%(Fore.WHITE, Back.BLACK, str(item.point.x), str(item.point.y)), end="-->")
print("%s%sEND"%(Fore.WHITE, Back.BLACK))




