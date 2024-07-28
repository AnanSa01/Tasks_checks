class Utilities:

    @staticmethod
    def pets_return_in_json(pet):
        try:
            pet._breed
        except AttributeError:
            pet._breed = None

        try:
            pet.indoor
        except AttributeError:
            pet.indoor = None

        return {
            "Identification Number": pet._pet_id,
            "Pet Name": pet.pet_name,
            "Species": pet._species,
            "Age": pet.age,
            "Vaccinated": pet._vaccinated,
            "Owner Name": pet.owner_name,
            "Owner Phone Number": pet.owner_phone_number,
            "Breed": pet._breed,
            "Indoor": pet.indoor
        }

    @staticmethod
    def owners_return_in_json(owner_name, owner_phone_number, _pet_id, pet_species, pet_name, number_of_pets=1):

        return {
            "Owner Name": owner_name,
            "Owner Phone Number": owner_phone_number,
            "Number Of Pets Owned": number_of_pets,
            "Pets Details": [
                {"Pet I.D.": _pet_id,
                 "Pet Species": pet_species,
                 "Pet Name": pet_name}

            ]
        }
