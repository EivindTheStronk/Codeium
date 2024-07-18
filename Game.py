# text based game with terminal
#TODO: player can choose their name - player movement is WASD - player charater is a "@", enemies are "!", walls are "|", and items are ".", roof and floors are "_" and " " respectively

class Game:
    def __init__(self):
        pass

    def start(self):
        # TODO: Implement game start logic here
        # For example, print a welcome message or start a new game
        print("Welcome to the game!")
        
        # asks to create a new game
        new_game = input("Do you want to start a new game? (y/n) ")
        if new_game.lower() == "y":
            print("Starting a new game...")
        else:
            print("Goodbye!")
        
        # TODO: Implement game start logic
        print("Game started!")

        # spawns player
        player = Player()
        print("Player spawned at position", player.position)

        # game loop
        while True:
            player.move()
            player.attack()
        
        

    def play(self):
        # TODO: Implement game play logic here
        pass

    def end(self):
        pass
class Player:
    def __init__(self):
        self.character = "@"
        self.position = (0, 0)  # initial position

    def move(self):
        # get input from the player
        direction = input("Enter the direction to move (W, A, S, D): ")

        # check if the input is valid
        if direction.lower() in ["w", "a", "s", "d"]:
            # update the player position based on the input
            if direction.lower() == "w":
                self.position = (self.position[0], self.position[1] - 1)
            elif direction.lower() == "a":
                self.position = (self.position[0] - 1, self.position[1])
            elif direction.lower() == "s":
                self.position = (self.position[0], self.position[1] + 1)
            elif direction.lower() == "d":
                self.position = (self.position[0] + 1, self.position[1])
        else:
            print("Invalid input. Please enter W, A, S, or D.")

    def get_input(self):
        # get input from the player
        return input("Enter your command: ")

    def attack(self):
        # attack logic goes here
        pass

class Map:
    def __init__(self, width, height):
        """
        Initialize the map with the given width and height.

        Args:
            width (int): The width of the map.
            height (int): The height of the map.
        """
        # Set the width of the map
        self.width = width
        
        # Set the height of the map
        self.height = height
        self.map = [[' ' for _ in range(width)] for _ in range(height)]

    def draw(self):
        for row in self.map:
            print(' '.join(row))

    def update(self, x, y, char):
        self.map[y][x] = char

class Player:
    def __init__(self, map):
        self.character = "@"
        self.position = (0, 0)
        self.map = map

    def move(self):
        direction = input("Enter the direction to move (W, A, S, D): ")

        if direction.lower() in ["w", "a", "s", "d"]:
            if direction.lower() == "w":
                new_y = self.position[1] - 1
            elif direction.lower() == "a":
                new_x = self.position[0] - 1
            elif direction.lower() == "s":
                new_y = self.position[1] + 1
            elif direction.lower() == "d":
                new_x = self.position[0] + 1

            if new_x >= 0 and new_x < self.map.width and new_y >= 0 and new_y < self.map.height:
                self.map.update(self.position[0], self.position[1], ' ')
                self.position = (new_x, new_y)
                self.map.update(new_x, new_y, self.character)

    def attack(self):
        pass

# Create the map
map = Map(10, 10)

# Create the player
player = Player(map)

# Start the game
while True:
    map.draw()
    player.move()
class Item:
    def __init__(self):
        pass

    def use(self):
        pass

    def drop(self):
        pass

    def destroy(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.start()