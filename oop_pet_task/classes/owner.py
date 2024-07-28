from memory_provider import MemoryProvider
from utilities import Utilities


class Owner:
    def __init__(self, owner_name, owner_phone_number):
        self._owner_name = owner_name
        self.owner_phone_number = owner_phone_number

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value

    def __str__(self):
        memory = MemoryProvider.load_data_owners()
        owners = memory["data_for_owners"]
        for check_owner in owners:
            if check_owner["Owner Name"] == self.owner_name:
                return f"\nOwner's name: {self.owner_name}, Pets of the owner: {check_owner["Pets Details"]}"

    def add_pet_to_list_of_owner(self, owner_name, owner_phone_number, pet_id, pet_species, pet_name):
        memory = MemoryProvider.load_data_owners()
        owners = memory["data_for_owners"]
        pets_details = {"Pet I.D.": pet_id, "Pet Species": pet_species, "Pet Name": pet_name}
        i = 0
        for check_owner in owners:
            if check_owner["Owner Phone Number"] == owner_phone_number:
                check_owner["Pets Details"].append(pets_details)
                check_owner["Number Of Pets Owned"] += 1
                MemoryProvider.save_data_owners(check_owner, i)
                break
            i += 1
        if len(owners) == i:
            MemoryProvider.save_data_owners(
                Utilities.owners_return_in_json(owner_name, owner_phone_number, pet_id, pet_species, pet_name))

    @staticmethod
    def remove_pet_from_list_of_owner(owner_phone_number, pet_name):
        memory = MemoryProvider.load_data_owners()
        owners = memory["data_for_owners"]
        for check_owner in owners:
            if check_owner["Owner Phone Number"] == owner_phone_number:
                pets_details = check_owner["Pets Details"]
                j = 0
                for pet in pets_details:
                    if pet["Pet Name"] == pet_name:
                        del pets_details[j]
                        check_owner["Number Of Pets Owned"] -= 1
                        MemoryProvider.save_data_owners(check_owner)
                        MemoryProvider.delete_owners(owner_phone_number)
                        break
                    j += 1
