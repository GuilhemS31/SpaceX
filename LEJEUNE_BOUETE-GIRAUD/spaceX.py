class Map:

    def __init__(self, nb_lines, nb_columns):
        self.lines = nb_lines
        self.columns = nb_columns
        self.robots_list = {}
        self.resources_list = []
        self.obstacles_list = []

    def add_robot(self, adresse_client, robot):
        if robot.line < 0 or robot.line > self.lines or robot.column < 0 or robot.column > self.columns:
            return self
        self.robots_list[adresse_client] = robot

    def add_resource(self, resource):
        if resource.line < 0 or resource.line > self.lines or resource.column < 0 or resource.column > self.columns:
            return self
        self.resources_list.append(resource)

    def add_obstacle(self, obstacle):
        if obstacle.line < 0 or obstacle.line > self.lines or obstacle.column < 0 or obstacle.column > self.columns:
            return self
        self.obstacles_list.append(obstacle)

    def delete_robot(self, adresse_client):
        self.robots_list[adresse_client] = None

    def delete_resource(self, resource):
        self.resources_list.remove(resource)

    def delete_obstacle(self, obstacle):
        self.obstacles_list.remove(obstacle)

    def __str__(self):
        result = "ROBOTS : \n"
        for robot in self.robots_list.values():
            result = result + str(robot) + "\n"
        return result

    def get_robot(self, adresse_client):
        return self.robots_list[adresse_client]

    def client_exists(self, adresse_client):
        if adresse_client in self.robots_list:
            return True
        else:
            return False

    def move_robot(self, adresse_client, direction):
        if direction == 'u':
            return self.moveUp(adresse_client)
        elif direction == 'd':
            return self.moveDown(adresse_client)
        elif direction == 'l':
            return self.moveLeft(adresse_client)
        elif direction == 'r':
            return self.moveRight(adresse_client)
        elif direction == '':
            return 'Missing argument : direction (usage : move <direction>)'
        return 'Direction not recognized'

    def moveUp(self, adresse_client):
        blocked = 'Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if self.robots_list[adresse_client].line == obstacle.line - 1 and self.robots_list[adresse_client].column == obstacle.column:
                return blocked
        if self.robots_list[adresse_client].line == self.lines - 1:
            return blocked
        self.robots_list[adresse_client].line = self.robots_list[adresse_client].line + 1
        return 'Robot moved Up'

    def moveDown(self, adresse_client):
        blocked = 'Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if self.robots_list[adresse_client].line == obstacle.line + 1 and self.robots_list[adresse_client].column == obstacle.column:
                return blocked
        if self.robots_list[adresse_client].line == self.lines + 1:
            return blocked
        self.robots_list[adresse_client].line = self.robots_list[adresse_client].line - 1
        return 'Robot moved Down'

    def moveLeft(self, adresse_client):
        blocked = 'Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if self.robots_list[adresse_client].line == obstacle.line and self.robots_list[adresse_client].column == obstacle.column + 1:
                return blocked
        if self.robots_list[adresse_client].column == self.columns + 1:
            return blocked
        self.robots_list[adresse_client].column = self.robots_list[adresse_client].column - 1
        return 'Robot moved Left'

    def moveRight(self, adresse_client):
        blocked = 'Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if self.robots_list[adresse_client].line == obstacle.line and self.robots_list[adresse_client].column == obstacle.column - 1:
                return blocked
        if self.robots_list[adresse_client].column == self.columns - 1:
            return blocked
        self.robots_list[adresse_client].column = self.robots_list[adresse_client].column + 1
        return 'Robot moved Right'


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
        if new_username == None:
            return 'Missing argument (usage : rename <name>)'
        self.username = new_username
        return 'Rename successful'


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
