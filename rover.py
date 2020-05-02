import time

# MARS ROVER KATA:

# Starting Point = (x, y)
# Directions: [N, S, E, W]
# Collection of commands : [f, f, l, f, f, r, r, b, b, l, l, b]
# - f : move forwards
# - b : move backwards
# - l : turn left 
# - r : turn right

class Rover:
    position = None
    direction = None

    def __init__(self, pos, direct):
        print('[rover] Preparing rover for landing...')
        self.position = pos
        self.direction = direct
        time.sleep(1)
        print('[rover] The rover has landed!')
        print('[pos] \tx = %i, y = %i' % (self.position['x'], self.position['y']))
        print('[dir] \tfacing: %s\n\n' % self.direction)

    
    def executeCommands(self, commands):
        counter = 0
        for command in commands:
            counter += 1
            if command == 'l' or command == 'r':
                self.turn(command)
                print('[exec] \tTurning %s' % command.upper())
            elif command == 'f' or command == 'b':
                self.move(command)
                print('[exec] \tMoving %s' % command.upper())
            print('%i) pos: (%i, %i) | direction: %s\n' % (counter, self.position['x'], self.position['y'], self.direction))
            time.sleep(1)


    def move(self, towards):
        if towards == 'f':
            self.moveForwards()
        elif towards == 'b':
            self.moveBackwards()


    def moveForwards(self):
        if self.direction == 'N':
            self.position['y'] += 1
        elif self.direction == 'E':
            self.position['x'] += 1
        elif self.direction == 'S':
            self.position['y'] -= 1
        elif self.direction == 'W':
            self.position['x'] -= 1


    def moveBackwards(self):
        if self.direction == 'N':
            self.position['y'] -= 1
        elif self.direction == 'E':
            self.position['x'] -= 1
        elif self.direction == 'S':
            self.position['y'] += 1
        elif self.direction == 'W':
            self.position['x'] += 1



    def turn(self, direct):
        if direct == 'r':
            self.turnRight()
        elif direct == 'l':
            self.turnLeft()


    def turnRight(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'


    def turnLeft(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'W':
            self.direction = 'N'


starting_point = { 
    'x': 0, 
    'y': 0 
}
starting_direction = 'E'
commands = ['f', 'f', 'l', 'f', 'f', 'r', 'r', 'b', 'b', 'l', 'l', 'b', 'l', 'f', 'l', 'f', 'f', 'r', 'f', 'f', 'f', 'r', 'f', 'l']

rover = Rover(starting_point, starting_direction)
rover.executeCommands(commands)