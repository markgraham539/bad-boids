from boids import Boids
from matplotlib import pyplot as plt
from matplotlib import animation

boids=Boids(
        flock_attraction=0.01/50,
        avoidance_radius=10,
        formation_flying_radius=100,
        speed_matching_strength=0.125/50
    )

boids.initialise_random(50)
boids.add_eagle(0,0,0,50)

figure=plt.figure()
axes=plt.axes(xlim=(-2000,1500), ylim=(-500,4000))
scatter=axes.scatter([b.position[0] for b in boids.boids],[b.position[1] for b in boids.boids])
scatter2=axes.scatter([boids.eagles.position[0]],[boids.eagles.position[1]])


def animate(frame):
    boids.update()
    scatter.set_offsets([b.position for b in boids.boids])
    scatter.set_color([(1,0,0) for b in boids.boids])
    scatter2.set_offsets(boids.eagles.position)
    scatter2.set_color((0,1,0))


anim = animation.FuncAnimation(figure, animate,
        frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
