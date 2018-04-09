import random 

class Tiles:
	def __init__(self,x,y,obs):
		self.__posX = x            
		self.__posY = y         
		self.__isObs = obs   # true is obstacle    
		self.__isRess = False  # true is ressource  
		
	@property
	def posX(self) : return self.__posX
	@property
	def posY(self) : return self.__posY
	@property
	def isObs(self) : return self.__isObs
	@property
	def isRess(self) : return self.__isRess
	@isRess.setter
	def isRess(self,isR) : self.__isRess = isR 
	
	def __str__(self):
		if self.isObs :
			return "X"
		elif self.isRess :
			return "O"
		else:
			return " "
		
class Robot():
	def __init__(self,x,y,name):
		self.__posX = x            
		self.__posY = y
		self.__name = name
		self.__ress = 0
		
	@property
	def posX(self) : return self.__posX
	@property
	def posY(self) : return self.__posY
	@property
	def name(self) : return self.__name
	@property
	def ress(self) : return self.__ress
	@ress.setter
	def ress(self) : self.__ress += 1
		

class Map:
	
	def refreshRess(self):
		cpt = 0
		while cpt < 5:
			x = random.randint(0,10)
			y = random.randint(0,10)
			
			print (f"{x},{y}")
			
			if self.__grid[x][y].isObs == False :
				self.__grid[x][y].isRess = True
				cpt += 1
			
	
	def __init__(self):
		"""
		_ _ _ _ _ _ _ _ _ _ _
		_ X X X _ _ _ _ _ _ _
		_ _ _ _ _ _ _ X X X X
		_ _ _ _ _ _ _ _ _ X _
		_ _ _ _ _ _ _ _ _ X _
		_ _ _ _ X X _ _ _ _ _
		_ _ _ _ X _ _ _ _ _ _
		_ X _ _ _ _ _ X _ X _
		_ X X _ _ _ _ X X X _
		_ _ X _ _ _ X X _ _ _
		_ _ _ _ _ _ _ _ _ _ _
		"""
		self.__grid = [
			[Tiles(0,0,False), Tiles(0,1,False), Tiles(0,2,False), Tiles(0,3,False), Tiles(0,4,False), Tiles(0,5,False), Tiles(0,6,False), Tiles(0,7,False), Tiles(0,8,False), Tiles(0,9,False), Tiles(0,10,False)],
			[Tiles(1,0,False), Tiles(1,1,True),  Tiles(1,2,True),  Tiles(1,3,True),  Tiles(1,4,False), Tiles(1,5,False), Tiles(1,6,False), Tiles(1,7,False), Tiles(1,8,False), Tiles(1,9,False), Tiles(1,10,False)],
			[Tiles(2,0,False), Tiles(2,1,False), Tiles(2,2,False), Tiles(2,3,False), Tiles(2,4,False), Tiles(2,5,False), Tiles(2,6,False), Tiles(2,7,True),  Tiles(2,8,True),  Tiles(2,9,True),  Tiles(2,10,True)],
			[Tiles(3,0,False), Tiles(3,1,False), Tiles(3,2,False), Tiles(3,3,False), Tiles(3,4,False), Tiles(3,5,False), Tiles(3,6,False), Tiles(3,7,False), Tiles(3,8,False), Tiles(3,9,True),  Tiles(3,10,False)],
			[Tiles(4,0,False), Tiles(4,1,False), Tiles(4,2,False), Tiles(4,3,False), Tiles(4,4,False), Tiles(4,5,False), Tiles(4,6,False), Tiles(4,7,False), Tiles(4,8,False), Tiles(4,9,True),  Tiles(4,10,False)],
			[Tiles(5,0,False), Tiles(5,1,False), Tiles(5,2,False), Tiles(5,3,False), Tiles(5,4,True),  Tiles(5,5,True),  Tiles(5,6,False), Tiles(5,7,False), Tiles(5,8,False), Tiles(5,9,False), Tiles(5,10,False)],
			[Tiles(6,0,False), Tiles(6,1,False), Tiles(6,2,False), Tiles(6,3,False), Tiles(6,4,True),  Tiles(6,5,False), Tiles(6,6,False), Tiles(6,7,False), Tiles(6,8,False), Tiles(6,9,False), Tiles(6,10,False)],
			[Tiles(7,0,False), Tiles(7,1,True),  Tiles(7,2,False), Tiles(7,3,False), Tiles(7,4,False), Tiles(7,5,False), Tiles(7,6,False), Tiles(7,7,True),  Tiles(7,8,False), Tiles(7,9,True),  Tiles(7,10,False)],
			[Tiles(8,0,False), Tiles(8,1,True),  Tiles(8,2,True),  Tiles(8,3,False), Tiles(8,4,False), Tiles(8,5,False), Tiles(8,6,False), Tiles(8,7,True),  Tiles(8,8,True),  Tiles(8,9,True),  Tiles(8,10,False)],
			[Tiles(9,0,False), Tiles(9,1,False), Tiles(9,2,True),  Tiles(9,3,False), Tiles(9,4,False), Tiles(9,5,False), Tiles(9,6,True),  Tiles(9,7,True),  Tiles(9,8,False), Tiles(9,9,False), Tiles(9,10,False)],
			[Tiles(10,0,False), Tiles(10,1,False), Tiles(10,2,False), Tiles(10,3,False), Tiles(10,4,False),  Tiles(10,5,False), Tiles(10,6,False), Tiles(10,7,False), Tiles(10,8,False), Tiles(10,9,False), Tiles(10,10,False)]
			]
		self.__listRobot = {}
		self.refreshRess()
		
	def __str__(self):
		ret = ""
		for lig in self.__grid:
			ret += "|"
			for col in lig:
				ret+= str(col) +"|"
			ret += "\n"
		return ret
				
