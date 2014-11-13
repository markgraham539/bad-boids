"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

def flyTowardsMiddle(posTargetBird, posOtherBird):
	return (posOtherBird-posTargetBird)*0.01/numberOfBoids

def flyAwayFromNearby(posTargetBird, posOtherBird):
	return posTargetBird-posOtherBird

def matchSpeed(velTargetBird, velOtherBird):
	return (velOtherBird-velTargetBird)*0.125/numberOfBoids

# Deliberately terrible code for teaching purposes
numberOfBoids = 50

boids_x=[random.uniform(-450,50.0) for x in range(numberOfBoids)]
boids_y=[random.uniform(300.0,600.0) for x in range(numberOfBoids)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(numberOfBoids)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(numberOfBoids)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	xPos,yPos,xVel,yVel=boids
	
	for i in range(numberOfBoids):
		for j in range(numberOfBoids):	
			xVel[i]+=flyTowardsMiddle(xPos[i],xPos[j])
			yVel[i]+=flyTowardsMiddle(yPos[i],yPos[j])
			
			nearOtherBird = (xPos[j]-xPos[i])**2 + (yPos[j]-yPos[i])**2 < 100
			if nearOtherBird == True:
				xVel[i]+=flyAwayFromNearby(xPos[i],xPos[j])
				yVel[i]+=flyAwayFromNearby(yPos[i],yPos[j])

			quiteNearOtherBird = (xPos[j]-xPos[i])**2 + (yPos[j]-yPos[i])**2 < 10000
			if quiteNearOtherBird == True:
				xVel[i]+=matchSpeed(xVel[i],xVel[j])
				yVel[i]+=matchSpeed(yVel[i],yVel[j])
				
		# Move according to velocities
		xPos[i]=xPos[i]+xVel[i]
		yPos[i]=yPos[i]+yVel[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
