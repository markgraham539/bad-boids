class Viewer(object):
	def __init__(self, boids):
		from matplotlib import pyplot as plt
		self.model=boids
		self.figure = plt.figure() 
		axes =plt.axes(xlim=(-2000,1500), ylim=(-500,4000))
		self.xlabel = plt.xlabel('x')
		self.scatterBoids=axes.scatter([b.position[0] for b in self.model.boids],[b.position[1] for b in self.model.boids]) 
		self.scatterEagles=axes.scatter([self.model.eagles.position[0]],[self.model.eagles.position[1]])

	def update(self, newmodel,frame):
		from matplotlib import pyplot as plt
		self.scatterBoids.set_offsets([b.position for b in newmodel.boids])
   		self.scatterBoids.set_color((1,0,0))
   		self.scatterEagles.set_offsets(newmodel.eagles.position)
   		self.scatterEagles.set_color((0,1,0))
   		self.xlabel = plt.xlabel(frame)
   		return self.scatterBoids,self.scatterEagles, self.xlabel

