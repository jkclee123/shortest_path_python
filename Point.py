class Point:
	def __init__(self, y, x):
		self.y = y
		self.x = x

	def north(self):
		return Point(self.y + 1, self.x)

	def east(self):
		return Point(self.y, self.x + 1)

	def south(self):
		return Point(self.y - 1, self.x)

	def west(self):
		return Point(self.y, self.x - 1)
	# return list of neighbouring Points
	def neighbour(self):
		return [self.north(), self.east(), self.south(), self.west()]
	# compare two Point 
	def equals(self, point):
		return self.y == point.y and self.x == point.x