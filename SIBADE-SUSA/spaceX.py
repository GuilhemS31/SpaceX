
class Tiles:
	def __init__(self,x,y):
		self._posX = x            
		self._posY = y         
		self._overRide = True       
		self._overRide = True
		
	@property
	def posX(self) : return self._posX
	@property
	def posY(self) : return self._posY
	@property
	def overide(self) : return self._overRide

class Obstacle(Tiles):
	def __init__(self,x,y):
		self._posX = x            
		self._posY = y         
		self._overRide = False
		
class Ressource(Tiles):
	def __init__(self,x,y):
		self._posX = x            
		self._posY = y         
		self._overRide = True
		
class Robot(Tiles):
	def __init__(self,x,y,name):
		self._posX = x            
		self._posY = y
		self._name = name
		self._ress = 0
		
	@property
	def name(self) : return self._name
	@property
	def ress(self) : return self._ress
	@ress.setter
	def addRess(self) : self._ress += 1
		

class Map:
	
	def refreshRess():
		...
		
	def __init__(self,nbX,nbY):
		self._grid = 
			[[Tiles(0,0), Tiles(0,1), Tiles(0,2), Tiles(0,3), Tiles(0,4), Tiles(0,5), Tiles(0,6), Tiles(0,7), Tiles(0,8), Tiles(0,9), Tiles(0,10)],
			['L1C0', 'L1C1', 'L1C2'],
			['L2C0', 'L2C1', 'L2C2'],
			['L3C0', 'L3C1', 'L3C2']]
		refreshRess()
