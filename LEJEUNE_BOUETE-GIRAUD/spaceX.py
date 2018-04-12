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
        result = "1071 ROBOTS : \n"
        for robot in self.robots_list.values():
            result = result + robot.username + "\n"
        return result

    def get_robot(self, adresse_client):
        return self.robots_list[adresse_client]

    def client_exists(self, adresse_client):
        if adresse_client in self.robots_list:
            return True
        else:
            return False

    def move_robot(self, adresse_client, direction):
        if self.robots_list[adresse_client].state == False:
            if direction == 'u':
                return self.moveUp(adresse_client)
            elif direction == 'd':
                return self.moveDown(adresse_client)
            elif direction == 'l':
                return self.moveLeft(adresse_client)
            elif direction == 'r':
                return self.moveRight(adresse_client)
            elif direction == '':
                return '3081 Missing argument : direction (usage : move <direction>)'
            return '3082 Direction not recognized'
        return '2081 Robot is paused'

    def moveDown(self, adresse_client):
        blocked = '2081 Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if self.robots_list[adresse_client].line == obstacle.line - 1 and self.robots_list[adresse_client].column == obstacle.column:
                return blocked
        if self.robots_list[adresse_client].line == self.lines - 1:
            return blocked
        self.robots_list[adresse_client].line = self.robots_list[adresse_client].line + 1
        return '1081 Robot moved Down'

    def moveUp(self, adresse_client):
        blocked = '2081 Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if self.robots_list[adresse_client].line == obstacle.line + 1 and self.robots_list[adresse_client].column == obstacle.column:
                return blocked
        if self.robots_list[adresse_client].line == self.lines + 1:
            return blocked
        self.robots_list[adresse_client].line = self.robots_list[adresse_client].line - 1
        return '1081 Robot moved Up'

    def moveLeft(self, adresse_client):
        blocked = '2081 Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if self.robots_list[adresse_client].line == obstacle.line and self.robots_list[adresse_client].column == obstacle.column + 1:
                return blocked
        if self.robots_list[adresse_client].column == self.columns + 1:
            return blocked
        self.robots_list[adresse_client].column = self.robots_list[adresse_client].column - 1
        return '1081 Robot moved Left'

    def moveRight(self, adresse_client):
        blocked = '2081 Robot blocked by obstacle'
        for obstacle in self.obstacles_list:
            if self.robots_list[adresse_client].line == obstacle.line and self.robots_list[adresse_client].column == obstacle.column - 1:
                return blocked
        if self.robots_list[adresse_client].column == self.columns - 1:
            return blocked
        self.robots_list[adresse_client].column = self.robots_list[adresse_client].column + 1
        return '1081 Robot moved Right'

    def status(self, adresse_client):
        return str(self.robots_list[adresse_client])

    def pause_robot(self, adresse_client):
        return self.robots_list[adresse_client].pause()

    def unpause_robot(self, adresse_client):
        return self.robots_list[adresse_client].unpause()



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

    def pause(self):
        if self.state == True:
            return '2041 Robot is already paused'
        self.state = True
        return '1041 Robot\'s behavior has been paused'

    def unpause(self):
        if self.state == False:
            return '2051 Robot is already behaving normally'
        self.state = False
        return '1051 Robot resumed his normal behavior'

    def rename(self, new_username):
        if new_username == None:
            return '3021 Missing argument (usage : rename <name>)'
        self.username = new_username
        return '1021 Rename successful'


    def __str__(self):
        result = "1061 POSITION : "+ str(self.column) + " " + str(self.line) + "\n"
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
