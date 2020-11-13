# Recursion
 CSS 340 Assignment 4: Recursion
 
	Purpose
		The programming assignment will provide an exercise in using recursion. There are two
		problems which need to be solved. The first asks for a recursive function to calculate a Catalan
		number. The second is to solve a path-finding problem in two dimensional space. The
		assignment will require the usage of recurrence as well as good class design. 
	
	Problem 1: The Good Mr. Catalan
		Write a program called Catalan which takes one argument and calls a recursive function which
		computes the nth Catalan number. The program then prints out the result to the console.
		
		For instance,
			python catalan.py 4
		Would print out: 14
		
			python catalan.py 10
		Would print out: 16796
	
	Problem 2: “The Greedy Robot” or “Lost in the Supermarket”
		A robot is positioned on an integral point in a two-dimensional coordinate grid (x1, y1). There is
		a treasure that has been placed at a point in the same grid at (x2, y2). x1, x2, y1, and y2 are all
		integers. The robot can move up (North), down (South), left (West), or right (East). Commands
		can be given to the robot to move one position in one of the four direction. That is, “E” moves
		a robot one slot East (to the right) so if the robot was on position (3, 4), it would now be on (4,
		4). The command N would move the robot one position north so a robot at position (4, 4)
		would be at (4, 5).
		
		Write a recursive program which determines all the unique shortest paths from the robot to the
		treasure.
		
		The input to the program will be the position of the robot (x1, y1) and the position of the
		treasure (x2, y2): four integers. For instance, an input of 1 3 -2 4 corresponds to the robot
		starting at position (1, 3) and needing to get to position (-2, 4). Do not worry about error
		conditions on input as we will assume the input is well formed. Read the input from the
		console.
		
		The output of the program should be the listing of the unique paths followed by the number of
		unique paths. A path should be output as a string of characters with each character
		corresponding to a direction the Robot should move. For instance, NNENE corresponds to
		having the robot move North, North, East, North and East. This would be one answer to the
		input: 3 3 5 6, which corresponds to (3,3) -> (5,6).

	Grade:
		50 / 50
