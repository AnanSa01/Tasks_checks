from pet_task_OOP_FLASK_fifth_task.classes.pet import Pet


class Cat(Pet):
    def __init__(self, pet_name, species, age, vaccinated, indoor, owner):
        super().__init__(pet_name, species, age, vaccinated, owner)
        self.indoor = indoor

    def __str__(self):
        return (f"\nThis pet is called {self.pet_name}, The pet is a Cat, aged {self.age} years old. \nHis owner is: "
                f"{self.owner_name}, \nIs it an indoor cat? {self.indoor}, \nVaccinated? {self._vaccinated} \nTotal pets at the moment: {self.total_pets}")
