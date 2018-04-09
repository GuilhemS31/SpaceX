class Map:

    def __init__(self, nb_lines, nb_columns):
        self.lines = nb_lines
        self.columns = nb_columns
        self.robots_list = []
        self.resources_list = []
        self.obstacles_list = []

    def add_robot(self, robot):
        if robot.line < 0 or robot.line > nb_lines or robot.column < 0 or robot.column > nb_columns:
            return self
        self.robots_list.append(robot)

    def add_resource(self, resource):
        if resource.line < 0 or resource.line > nb_lines or resource.column < 0 or resource.column > nb_columns:
            return self
        self.resources_list.append(resource)

    def add_obstacle(self, obstacle):
        if obstacle.line < 0 or obstacle.line > nb_lines or obstacle.column < 0 or obstacle.column > nb_columns:
            return self
        self.obstacles_list.append(obstacle)

    def delete_robot(self, robot):
        self.robots_list.remove(robot)

    def delete_resource(self, resource):
        self.resources_list.remove(resource)

    def delete_obstacle(self, obstacle):
        self.obstacles_list.remove(obstacle)

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

class Resource:

    def __init__(self, pos_line, pos_column):
        self.line = pos_line
        self.column = pos_column


class Obstacle:

    def __init__(self, pos_line, pos_column):
        self.line = pos_line
        self.column = pos_column
