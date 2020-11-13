import point
import greedyRobot
import sys

#from command line pull robot points
robot = greedyRobot.robot(eval(sys.argv[1]), eval(sys.argv[2]))
#from command line pull treasure points
treasurePoint = point.point(eval(sys.argv[3]), eval(sys.argv[4]))
#find the total number of paths
total = robot.findTreasure(robot.getX(), robot.getY(),treasurePoint.getX(),treasurePoint.getY(),[])
#print out total number of paths
print("Number of paths: ", total)