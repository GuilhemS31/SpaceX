class Map:

    def __init__(self, nb_lines, nb_columns):
        self.lines = nb_lines
        self.columns = nb_columns
        self.robots_list = []
        self.resources_list = []
        self.obstacles_list = []

    def add_robot(self, robot):
        if robot.line < 0 or robot.line > self.lines or robot.column < 0 or robot.column > self.columns:
            return self
        self.robots_list.append(robot)

    def add_resource(self, resource):
        if resource.line < 0 or resource.line > self.lines or resource.column < 0 or resource.column > self.columns:
            return self
        self.resources_list.append(resource)

    def add_obstacle(self, obstacle):
        if obstacle.line < 0 or obstacle.line > self.lines or obstacle.column < 0 or obstacle.column > self.columns:
            return self
        self.obstacles_list.append(obstacle)

    def delete_robot(self, robot):
        self.robots_list.remove(robot)

    def delete_resource(self, resource):
        self.resources_list.remove(resource)

    def delete_obstacle(self, obstacle):
        self.obstacles_list.remove(obstacle)

    def __str__(self):
        result = "ROBOTS : \n"
        for robot in self.robots_list:
            result = result + str(robot) + "\n"
        return result

    def move_robot(self, robot, direction):
        options = {
            'u' : moveUp,
            'd' : moveDown,
            'l' : moveLeft,
            'r' : moveRight
            '' : 'Missing argument : direction (usage : move <direction>)'
        }
        if direction in options:
            return options[direction]()
        else:
            return 'Direction not recognized'

    def moveUp(self, robot):
        blocked = 'Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if robot.line == obstacle.line - 1:
                return blocked
        if robot.line == self.lines - 1:
            return blocked
        robot.line = robot.line + 1
        return

    def moveDown(self, robot):


    def moveLeft(self, robot):


    def moveRight(self, robot):


class Robot:

    def __init__(self, _username, pos_line, pos_column):
        self.username = _username
        self.line = pos_line
        self.column = pos_column
        self.state = False
        self.resources_list = []

    def __add__(self, resource):
        self.resources_list.append(resource)
        return self

    def delete_resource(self, resource):
        self.resources_list.remove(resource)

    def switch_state(self):
        if self.state == False:
            self.state = True
        else:
            self.state = False

    def rename(self, new_username):
        self.username = new_username

    def __str__(self):
        result = "USERNAME : " + self.username + "\n"
        result = result + "RESOURCES : \n"
        for resource in self.resources_list:
            result = result + resource + "\n"
        return result


class Resource:

    def __init__(self, r_name, pos_line, pos_column):
        self.name = r_name
        self.line = pos_line
        self.column = pos_column

    def __str__(self):
        return self.name


class Obstacle:

    def __init__(self, pos_line, pos_column):
        self.line = pos_line
        self.column = pos_column
