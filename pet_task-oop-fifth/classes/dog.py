from classes.pet import Pet


class Dog(Pet):
    def __init__(self, pet_name, species, age, vaccinated, breed, owner):
        super().__init__(pet_name, species, age, vaccinated, owner)
        self._breed = breed

    def __str__(self):
        return (f"\nThis pet is called {self.pet_name}, The pet is a dog from breed {self._breed}, aged {self.age} years "
                f"old. \nHis owner is: {self.owner_name} \nVaccinated? {self._vaccinated} \nTotal pets at the moment: {self.total_pets}")
