import random
import time

class GrassTexture:
    def __init__(self, name):
        self.name = name
        self.length = random.randint(1, 5)
        self.thickness = random.randint(1, 5)
        self.moisture = random.randint(1, 5)

class GrasslandExplorer:
    def __init__(self, name):
        self.name = name
        self.catalog = []
    
    def touch_grass(self, grass):
        self.catalog.append(grass)

class Game:
    def __init__(self):
        self.explorer = None
        self.grass_textures = []
        self.time_limit = 60  # Time limit in seconds
    
    def create_grass_textures(self):
        # Add various grass textures with randomized attributes
        self.grass_textures.append(GrassTexture("Freshly Cut Grass"))
        self.grass_textures.append(GrassTexture("Mossy Patch"))
        self.grass_textures.append(GrassTexture("Swaying Blades"))
        self.grass_textures.append(GrassTexture("Fluffy Tuffet"))
        self.grass_textures.append(GrassTexture("Fluffy Tuffet"))
        self.grass_textures.append(GrassTexture("Spongy Sedge"))
        self.grass_textures.append(GrassTexture("Whispering Whiskers"))
        self.grass_textures.append(GrassTexture("Thorny Blades"))
        self.grass_textures.append(GrassTexture("Wavy Sea Grass"))
        self.grass_textures.append(GrassTexture("Golden Prairie"))
        self.grass_textures.append(GrassTexture("Frosty Fronds"))
        self.grass_textures.append(GrassTexture("Lush Clover"))
        self.grass_textures.append(GrassTexture("Fine Filaments"))
        self.grass_textures.append(GrassTexture("Velvet Grass"))
        self.grass_textures.append(GrassTexture("Crunchy Blades"))
        self.grass_textures.append(GrassTexture("Dense Tuft"))
        self.grass_textures.append(GrassTexture("Silky Meadow"))
        self.grass_textures.append(GrassTexture("Curly Stems"))



    
    def start(self):
        print("Welcome to Grassland Explorers: Tactile Terrain!")
        self.create_grass_textures()
        self.explorer = GrasslandExplorer(input("Enter your explorer name: "))
        self.play()

    def play(self):
        print("Explore the grassland and touch different textures!")
        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            remaining_time = self.time_limit - elapsed_time

            if remaining_time <= 0:
                print("Time's up!")
                break

            print("\nOptions:")
            print("1. Touch grass")
            print("2. Catalog")
            print("3. Quit")

            choice = input("Select an option: ")
            
            if choice == "1":
                self.touch_grass()
            elif choice == "2":
                self.view_catalog()
            elif choice == "3":
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Try again.")

    def touch_grass(self):
        grass = random.choice(self.grass_textures)
        self.explorer.touch_grass(grass)
        print(f"You touched {grass.name}!")

    def view_catalog(self):
        print("\nCatalog:")
        if len(self.explorer.catalog) > 0:
            for grass in self.explorer.catalog:
                print(f"- {grass.name}: Length={grass.length}, Thickness={grass.thickness}, Moisture={grass.moisture}")
        else:
            print("Your catalog is empty.")

# Run the game
game = Game()
game.start()

