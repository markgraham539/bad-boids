class Controller(object):
	def __init__(self):
		from boids import Boids
		from boidsViewer import Viewer

		self.boids=Boids(
        flock_attraction=0.01/50,
        avoidance_radius=10,
        formation_flying_radius=100,
        speed_matching_strength=0.125/50
    	)

		self.boids.initialise_random(50)
		self.boids.add_eagle(0,0,0,50)

		self.viewer=Viewer(self.boids)

		def animate(frame):
			self.boids.update()
			self.viewer.update(self.boids,frame)

		self.animator = animate

	def go(self):
		from matplotlib import animation
		from matplotlib import pyplot as plt
		anim = animation.FuncAnimation(self.viewer.figure, self.animator, frames =50, interval = 50)
		plt.show()
