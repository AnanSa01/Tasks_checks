from classes.pet import Pet
from utilities import Utilities
from classes.cat import Cat
from classes.dog import Dog
from classes.owner import Owner
from memory_provider import MemoryProvider


def main():

    pet_name = "Bella"
    species = "Dog"
    age = 11
    vaccinated = True
    breed = "Golden"
    owner_name = "Majd"
    owner_phone_number = "0501111111"
    my_owner = Owner(owner_name, owner_phone_number)
    bella = Dog(pet_name, species, age, vaccinated, breed, my_owner)
    print(bella)
    MemoryProvider.save_data_pets(Utilities.pets_return_in_json(bella))

    pet_name = "Alex"
    species = "Cat"
    age = 5
    vaccinated = False
    indoor = True
    owner_name = "Shebel"
    owner_phone_number = "0502222222"
    my_owner = Owner(owner_name, owner_phone_number)
    alex = Cat(pet_name, species, age, vaccinated, indoor, my_owner)
    print(alex)
    MemoryProvider.save_data_pets(Utilities.pets_return_in_json(alex))

    pet_name = "Bob"
    species = "Snake"
    age = 20
    vaccinated = False
    owner_name = "Ehab"
    owner_phone_number = "0503333333"
    my_owner = Owner(owner_name, owner_phone_number)
    bob = Pet(pet_name, species, age, vaccinated, my_owner)
    print(bob)
    MemoryProvider.save_data_pets(Utilities.pets_return_in_json(bob))

    pet_name = "Mark"
    species = "Mouse"
    age = 3
    vaccinated = False
    owner_name = "Ehab"
    owner_phone_number = "0503333333"
    my_owner = Owner(owner_name, owner_phone_number)
    mark = Pet(pet_name, species, age, vaccinated, my_owner)
    print(mark)
    MemoryProvider.save_data_pets(Utilities.pets_return_in_json(mark))

    pet_name = "Rick"
    species = "Owl"
    age = 8
    vaccinated = True
    owner_name = "Ehab"
    owner_phone_number = "0503333333"
    my_owner = Owner(owner_name, owner_phone_number)
    rick = Pet(pet_name, species, age, vaccinated, my_owner)
    print(rick)
    MemoryProvider.save_data_pets(Utilities.pets_return_in_json(rick))
    #
    # Owner.remove_pet_from_list_of_owner("0503333333", "Mark")

    # shebel = Owner("Shebel", "0502222222")
    # print(shebel)
    # print(Pet.total_pets())

if __name__ == '__main__':
    main()
