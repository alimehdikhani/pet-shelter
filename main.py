from animals import Dog, Cat, Bird, Wolf

from shelter import Shelter

from people import Adopter

from exceptions import (
    AnimalNotFoundError,
    DuplicateAnimalError,
    AnimalAlreadyAdoptedError,
    MaximumAdoptionReachedError
)


shelter = Shelter()
 


# Sample animals

shelter.add_animal(
    Dog("Rex", 3, "Male", "Labrador")
)

shelter.add_animal(
    Cat("Luna", 2, "Female", "Persian")
)

shelter.add_animal(
    Bird("Tweety", 1, "Male", "Parrot")
)

shelter.add_animal(
    Wolf("Shadow", 5, "Male", "Grey Wolf")
)


# Sample adopter

adopter = Adopter(
    "Ali",
    "09123456789",
    "1234567890"
)


while True:

    print("\n--- PET SHELTER ---")

    print("1. Add animal")
    print("2. Show animals")
    print("3. Search animal")
    print("4. Adopt animal")
    print("5. Return animal")
    print("6. Show available animals")
    print("7. Show adopted animals")
    print("8. Exit")


    choice = input("Enter your choice: ").strip()


    if choice == "1":

        try:

            name = input("Enter animal name: ").strip()

            age = int(input("Enter animal age: "))

            gender = input("Enter animal gender: ").strip()

            breed = input("Enter animal breed: ").strip()

            animal_type = input(
                "Enter animal type (dog/cat/bird/wolf): "
            ).strip().lower()


            if animal_type == "dog":

                animal = Dog(
                    name,
                    age,
                    gender,
                    breed
                )


            elif animal_type == "cat":

                animal = Cat(
                    name,
                    age,
                    gender,
                    breed
                )


            elif animal_type == "bird":

                animal = Bird(
                    name,
                    age,
                    gender,
                    breed
                )


            elif animal_type == "wolf":

                animal = Wolf(
                    name,
                    age,
                    gender,
                    breed
                )


            else:

                print("Invalid animal type.")

                continue


            shelter.add_animal(animal)

            print("Animal added successfully.")


        except ValueError:

            print("Age must be a number.")


        except DuplicateAnimalError as error:

            print(error)


    elif choice == "2":

        shelter.show_animals()


    elif choice == "3":

        search_choice = input(
            "Search by name or species? (name/species): "
        ).strip().lower()


        if search_choice == "name":

            name = input("Enter animal name: ").strip()


            try:

                animal = shelter.search_animal(name)

                animal.show_info()


            except AnimalNotFoundError as error:

                print(error)


        elif search_choice == "species":

            species = input(
                "Enter species (dog/cat/bird/wolf): "
            ).strip().lower()


            results = shelter.search_by_species(species)


            if results:

                for animal in results:

                    animal.show_info()


            else:

                print("No animals found.")


        else:

            print("Invalid search type.")


    elif choice == "4":

        name = input("Enter animal name: ").strip()


        try:

            shelter.adopt_animal(
                name,
                adopter
            )

            print("Animal adopted successfully.")


        except AnimalNotFoundError as error:

            print(error)


        except AnimalAlreadyAdoptedError as error:

            print(error)


        except MaximumAdoptionReachedError as error:

            print(error)


    elif choice == "5":

        name = input("Enter animal name: ").strip()


        try:

            returned = shelter.return_animal(
                name,
                adopter
            )


            if returned:

                print("Animal returned successfully.")

            else:

                print("This animal is not adopted by this adopter.")


        except AnimalNotFoundError as error:

            print(error)


    elif choice == "6":

        shelter.show_available_animals()


    elif choice == "7":

        shelter.show_adopted_animals()


    elif choice == "8":

        print("Goodbye!")

        break


    else:

        print("Invalid choice. Please enter a number from 1 to 8.")