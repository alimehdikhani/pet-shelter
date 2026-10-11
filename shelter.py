from exceptions import (
    AnimalNotFoundError,
    DuplicateAnimalError,
    AnimalAlreadyAdoptedError
)

from decorators import log_operation


class Shelter:

    def __init__(self):

        self.animals = []


    @log_operation
    def add_animal(self, animal):

        try:
            self.search_animal(animal.name)

            raise DuplicateAnimalError(
                "Animal with this name already exists."
            )

        except AnimalNotFoundError:

            self.animals.append(animal)

            return True


    def show_animals(self):

        if len(self.animals) == 0:

            print("No animals in shelter.")

            return

        for animal in self.animals:

            animal.show_info()


    def search_animal(self, name):

        for animal in self.animals:

            if animal.name.lower() == name.lower():

                return animal

        raise AnimalNotFoundError(
            f"Animal '{name}' not found."
        )


    def search_by_species(self, species):

        results = []

        for animal in self.animals:

            if animal.__class__.__name__.lower() == species.lower():

                results.append(animal)

        return results


    @log_operation
    def remove_animal(self, name):

        animal = self.search_animal(name)

        self.animals.remove(animal)

        return True


    @log_operation
    def adopt_animal(self, name, adopter):

        animal = self.search_animal(name)

        if animal.adopted:
            raise AnimalAlreadyAdoptedError(
                "Animal is already adopted."
            )

        adopter.adopt_animal(animal)

        return True


    @log_operation
    def return_animal(self, name, adopter):

        animal = self.search_animal(name)

        return adopter.return_animal(animal)


    def show_available_animals(self):

        found = False

        for animal in self.animals:

            if not animal.adopted:

                animal.show_info()

                found = True

        if not found:

            print("No available animals.")


    def show_adopted_animals(self):

        found = False

        for animal in self.animals:

            if animal.adopted:

                animal.show_info()

                found = True

        if not found:

            print("No adopted animals.")