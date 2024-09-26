class gardenBox:

    def __init__(self, plantCount=0):
        self.plantCount = plantCount

    def plant(self):
        self.plantCount += 1
        print("You added a plant to your garden!")
        print("You now have", self.plantCount, "plants in your garden!")

    def water(self):
        print("You watered your plants!")
        print("You have", self.plantCount, "plants in your garden!")

    def harvest(self):
        if self.plantCount > 0:
            self.plantCount -= 1
        print("You harvested a plant from your garden!")
        print("You now have", self.plantCount, "plants in your garden!")


gardenOne = gardenBox()

gardenOne.plant()
gardenOne.plant()

gardenOne.water()

gardenOne.harvest()
