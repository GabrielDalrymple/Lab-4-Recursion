class point:
	def __init__(self, x = 0, y = 0):
		self.__x = x
		self.__y = y
	def getX(self):
		return self.__x
	def getY(self):
		return self.__y
	def setX(self, x):
		self.__x = x
		return True
	def setY(self, y):
		self.__y = y
		return True
