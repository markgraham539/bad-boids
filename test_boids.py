import boids
from nose.tools import assert_almost_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    boids.update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	


def test_flyTowardsMiddle():
	numberOfBoids = 50
	#Test velocity update is 0 if attraction factor is 0
	assert boids.flyTowardsMiddle(1,2,0, numberOfBoids)==0
	#Test velocity update is 0 if boids are in same position
	assert boids.flyTowardsMiddle(3,3,1, numberOfBoids)==0
	#Test a fixed example
	testValue = boids.flyTowardsMiddle(2.0,3.0,1.0, numberOfBoids)
	knownValue = (1.0/50)
	assert testValue ==knownValue


def test_flyAwayFromNearby():
	#Test simple example
	a=5
	b=4
	assert boids.flyAwayFromNearby(a,b) == (a-b)


def test_matchSpeed():
	numberOfBoids = 50
	#Test velocity update 0 if speed match factor is 0
	assert boids.matchSpeed(1,2,0, numberOfBoids)==0
	#Test velocity update is 0 if boids have same speed
	assert boids.matchSpeed(3,3,1, numberOfBoids) == 0
	#Test known example
	testValue = boids.matchSpeed(3,4,2, numberOfBoids) 
	knownValue = 2/50
	assert testValue == knownValue

def test_getRandomNumbers():
	rand = boids.getRandomNumbers(0,20,1000)
	assert len(rand) == 1000
	assert min(rand) > 0
	assert max(rand) < 20


