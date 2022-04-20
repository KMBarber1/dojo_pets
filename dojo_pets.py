class Ninja:
    
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet= pet

    def walk(self):
        self.pet.play()
        return self

#does not work -me
    # def feed(self):
    #     self.pet.eat()
    #     return self

#works - provided solution
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self

    def bathe(self):
        self.pet.noise()


# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method


class Pet:

    def __init__(self, name, species, sound, tricks):
        self.name = name
        self.species = species
        self.energy = 80
        self.health = 80
        self.sound = sound
        self.tricks = tricks


    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        #added below from provided solution
        self.energy -= 15
        return self

    def noise(self):
        #does not work - me
        # self.sound()
        # return self
        #works - provided solution
        print(self.noise)


# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound


#does not work - me 
#Sanoma.noise()
#Kate.walk().bathe().feed()

#works - provided solution
my_treats = ['Chicken', 'Tuna', 'Beff']
my_pet_food = ['Blue_Wilderness', 'Fancy_Feast']

Sanoma = Pet('Sanoma', 'Cat', 'Hiss', 'Just_Nope')
Trinity = Pet('Trinity', 'Cat', 'Meow', 'Climb') 
Alexander = Pet('Alexander', 'Cat', 'Purr', 'Fetch')

Kate = Ninja('Kate', 'Barber',my_treats,my_pet_food, Sanoma)

Kate.feed()
Kate.feed()
Kate.feed()