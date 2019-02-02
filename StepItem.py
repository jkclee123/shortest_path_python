from Point import Point

class StepItem:
	# compose of a Point and steps required
	def __init__(self, point, step):
		self.point = Point(point.y, point.x)
		self.step = step