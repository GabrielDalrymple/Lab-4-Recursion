class robot:
	#constructors
	def __init__(self, x = 0, y = 0):
		self.__x = x
		self.__y = y
		self.__path = []
	#getters/setters
	def getX(self):
		return self.__x
	def getY(self):
		return self.__y
	def getPath(self):
		temp = self.__path[:]
		return temp
	def setX(self, x):
		self.__x = x
		return True
	def setY(self, y):
		self.__y = y
		return True
	#helpers
	def findTreasure(self, rX, rY, tX, tY, path):
		#at treasure, print path and increase count
		if rX == tX and rY == tY:
			self.printPath(path)
			return 1
		#number of paths
		numPaths = 0
		#if above, move down
		if rY > tY:
			#deep copy list
			temp = path[:]
			#add change in movement
			temp.append("S")
			#increase paths and move
			numPaths += self.findTreasure(rX, rY-1, tX, tY, temp)
		#if below, move up
		if rY < tY:
			#deep copy list
			temp = path[:]
			#add change in movement
			temp.append("N")
			#increase paths and move
			numPaths += self.findTreasure(rX, rY+1, tX, tY, temp)
		#if left, move right
		if rX < tX:
			#deep copy list
			temp = path[:]
			#add change in movement
			temp.append("E")
			#increase paths and move
			numPaths += self.findTreasure(rX+1, rY, tX, tY, temp)
		#if right, move left
		if rX > tX:
			#deep copy list
			temp = path[:]
			#add change in movement
			temp.append("W")
			#increase paths and move
			numPaths += self.findTreasure(rX-1, rY, tX, tY, temp)
		#return number of paths
		return numPaths
	#print the path
	def printPath(self, path):
		print(path)
		return