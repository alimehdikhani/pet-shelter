import re

from exceptions import (
    MaximumAdoptionReachedError,
    AnimalAlreadyAdoptedError
)


class Adopter:

    @staticmethod
    def validate_phone(phone):

        return bool(re.fullmatch(r"09\d{9}", phone))


    @staticmethod
    def validate_national_id(national_id):

        return bool(re.fullmatch(r"\d{10}", national_id))


    def __init__(self, name, phone, national_id):

        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number")

        if not self.validate_national_id(national_id):
            raise ValueError("Invalid national id")

        self.name = name
        self.phone = phone
        self.national_id = national_id
        self.adopted_animals = []


    def adopt_animal(self, animal):

        if len(self.adopted_animals) >= 9:
            raise MaximumAdoptionReachedError(
                "Maximum adoption limit reached."
            )

        if animal.adopted:
            raise AnimalAlreadyAdoptedError(
                "Animal is already adopted."
            )

        self.adopted_animals.append(animal)

        animal.adopted = True

        return True


    def return_animal(self, animal):

        if animal in self.adopted_animals:

            self.adopted_animals.remove(animal)

            animal.adopted = False

            return True

        return False