# Maze Explorer
## Introduction
This is a Python application that randomly generates a maze and then through a _genetic algorithm_ it find the path to the end.
`Note that in the maze that will be generated there'll be only one path to the end`

## How does it works ?
1. The maze is generated via [Prim's algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm)
2. The genetic algorithm's fitness function calculate each "Player" _real_ distance from the end, and it maps this value in this way:
	```python
	maxdistance = AStar(startPoint, endPoint)
	currentDistance = AStar(currentPoint, endPoint)
	# [maxDistance, 0] ---> [0,1] range
	fitness = mapFromRange(currentDistance, maxdistance, 0, 0, 1)
	```
## How can i test it ?
It's **VERY** easy to run.
There're two ways for running it:
1. You can navigate to `dist/gui/` and the open `gui.exe`
2. You should have installed [python3](https://www.python.org/downloads/) and [pygame](https://www.pygame.org/wiki/GettingStarted), then open cmd (or terminal if you're on linux or mac os) and type `python3 ./gui.py`.

The advantage of using the second method is that you can change maze and genetic algorithm's config through the file `config.py`.


## Config. py file
```python
WINDOW_TITLE = "Maze Explorer" 	#this is the window title

MAZE_WIDTH = 50					#maze width (this will be multiplied by BLOCK_SIZE)
MAZE_HEIGHT = 50				#maze height (this will be multiplied by BLOCK_SIZE)
BLOCK_SIZE = 15					#dimension of single maze block

GENERATIONS = 100				#number of generations
POPULATION_SIZE = 100			#population size
MUTATION_RATE = 0.01			#population's mutation rate

START_COORDS = (1,1)			#start coords (you should use valid coords)
END_COORDS = (MAZE_HEIGHT-1,MAZE_WIDTH-1)	#end coords (you should use valid coords)
```

## Video example 

Link youtube [video](https://www.youtube.com/watch?v=KehZd5-NAlY)
