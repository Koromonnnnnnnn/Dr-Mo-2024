class Frog:
    def __init__(self, name, color, size, hunger_level=10, energy_level=10):
        self.name = name
        self.color = color
        self.size = size
        self.hunger_level = hunger_level
        self.energy_level = energy_level

    def ribbit(self):
        print("Ribbit ribbit!")
        self.hunger_level -= 1

    def eat(self, fly_count):
        print(self.name, "eats", fly_count, "flies")
        self.energy_level += fly_count
        self.hunger_level -= fly_count // 2

    def jump(self):
        if self.size == "small":
            print(self.name, "jumps a little")
        elif self.size == "medium":
            print(self.name, "jumps a moderate height")
        elif self.size == "large":
            print(self.name, "jumps high")
        else:
            print(self.name, "did not jump")
        self.energy_level -= 2
        self.hunger_level -= 1

    def sleep(self):
        self.energy_level = 10
        print("Zzz... The frog is sleeping.")

    def status(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Size:", self.size)
        print("Hunger Level:", self.hunger_level)
        print("Energy Level:", self.energy_level)

if __name__ == "__main__":
    froggy = Frog(name="Freddy", color="blue", size="small")
    froggy.jump()
    froggy.eat(5)
    froggy.sleep()
    froggy.status()
