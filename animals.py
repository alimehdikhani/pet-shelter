class Animal:

    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.adopted = False

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Breed: {self.breed}")
        print(f"Adopted: {self.adopted}")
        print()

    @property
    def is_adopted(self):
        return self.adopted

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["gender"],
            data["breed"]
        )

    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):

    def make_sound(self):
        print("Dog says: Woof!")


class Cat(Animal):

    def make_sound(self):
        print("Cat says: Meow!")


class Bird(Animal):

    def make_sound(self):
        print("Bird says: Tweet!")


class Wolf(Animal):

    def make_sound(self):
        print("Wolf says: Awooo!")