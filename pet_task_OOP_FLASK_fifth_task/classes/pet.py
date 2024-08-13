from pet_task_OOP_FLASK_fifth_task.classes.owner import Owner
from pet_task_OOP_FLASK_fifth_task.memory_provider import MemoryProvider


class Pet(Owner):
    def __init__(self, pet_name, species, age, vaccinated, owner):
        super().__init__(owner.owner_name, owner.owner_phone_number)
        self.pet_name = pet_name
        self._species = species
        self.age = age
        self._vaccinated = vaccinated
        self._pet_id = self.set_id_for_new_pet()
        self.add_pet_to_list_of_owner(owner.owner_name, owner.owner_phone_number, self._pet_id, self._species, self.pet_name)
        self.total_pets = self.total_pets_count()

    def __str__(self):
        return (f"\nThis pet is called {self.pet_name}, The pet is a {self._species}, aged {self.age} years old. \nHis "
                f"owner is: {self.owner_name}, \nVaccinated? {self._vaccinated}.\nTotal pets at the moment: {self.total_pets}")

    def check_if_pet_vaccinated(self):
        return self._vaccinated

    def set_pet_as_vaccinated(self):
        if not self._vaccinated:
            self._vaccinated = True

    @staticmethod
    def total_pets_count():
        memory = MemoryProvider.load_data_pets()
        data = memory["data_for_pets"]
        return len(data)

    def retrieve_pet_age_in_human_years(self):
        return self.age * 7

    def __eq__(self, other):
        if isinstance(other, Pet):
            return self.pet_name == other.pet_name and self._species == other._species
        return False

    def set_id_for_new_pet(self):
        memory = MemoryProvider.load_data_pets()
        data = memory["data_for_pets"]
        try:
            return data[-1]["Identification Number"] + 1
        except IndexError:
            return 1
