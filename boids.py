"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

def initFigure():
    figure=plt.figure()
    axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
    scatter=axes.scatter(boids[0],boids[1])
    return figure, scatter

def flyTowardsMiddle(posTargetBird, posOtherBird,attractionToMiddle):
	return (posOtherBird-posTargetBird)*attractionToMiddle/numberOfBoids

def flyAwayFromNearby(posTargetBird, posOtherBird):
	return posTargetBird-posOtherBird

def matchSpeed(velTargetBird, velOtherBird, speedMatchFactor):
	return (velOtherBird-velTargetBird)*speedMatchFactor/numberOfBoids

def getRandomNumbers(lowerLim, upperLim, number):
	return [random.uniform(lowerLim,upperLim) for x in range(number)]

# Deliberately terrible code for teaching purposes
numberOfBoids = 50
attractionToMiddle = 0.01
speedMatchFactor = 0.125

boids_x= getRandomNumbers(-450,50.0,numberOfBoids) 
boids_y=getRandomNumbers(300,600.0,numberOfBoids) 
boid_x_velocities=getRandomNumbers(0,10,numberOfBoids) 
boid_y_velocities=getRandomNumbers(-20,20,numberOfBoids) 
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	xPos,yPos,xVel,yVel=boids
	
	for i in range(numberOfBoids):
		for j in range(numberOfBoids):	
			xVel[i]+=flyTowardsMiddle(xPos[i],xPos[j],attractionToMiddle)
			yVel[i]+=flyTowardsMiddle(yPos[i],yPos[j],attractionToMiddle)
			
			nearOtherBird = (xPos[j]-xPos[i])**2 + (yPos[j]-yPos[i])**2 < 100
			if nearOtherBird == True:
				xVel[i]+=flyAwayFromNearby(xPos[i],xPos[j])
				yVel[i]+=flyAwayFromNearby(yPos[i],yPos[j])

			quiteNearOtherBird = (xPos[j]-xPos[i])**2 + (yPos[j]-yPos[i])**2 < 10000
			if quiteNearOtherBird == True:
				xVel[i]+=matchSpeed(xVel[i],xVel[j],speedMatchFactor)
				yVel[i]+=matchSpeed(yVel[i],yVel[j],speedMatchFactor)

		# Move according to velocities
		xPos[i]=xPos[i]+xVel[i]
		yPos[i]=yPos[i]+yVel[i]


figure,scatter = initFigure()

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
