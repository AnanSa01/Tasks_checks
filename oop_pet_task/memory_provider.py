import json


class MemoryProvider:

    @staticmethod
    def load_data_pets():
        try:
            with open("pet_store.json", 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File pet_store.json not found. Starting with an empty library.")

    @staticmethod
    def save_data_pets(pet):
        memory = MemoryProvider.load_data_pets()
        data = memory["data_for_pets"]
        data.append(pet)
        memory["data_for_pets"] = data
        with open("pet_store.json", "w") as file:
            json.dump(memory, file, indent=3)

    @staticmethod
    def load_data_owners():
        try:
            with open("pet_store.json", 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File pet_store.json not found. Starting with an empty library.")

    @staticmethod
    def save_data_owners(owner, i=None):
        memory = MemoryProvider.load_data_owners()
        data = memory["data_for_owners"]
        if i:
            data[i] = owner
        else:
            data.append(owner)
        memory["data_for_owners"] = data
        with open("pet_store.json", "w") as file:
            json.dump(memory, file, indent=3)

    @staticmethod
    def delete_owners(delete_owners):
        memory = MemoryProvider.load_data_owners()
        data = memory["data_for_owners"]
        i = 0
        for owner in data:
            if owner["Owner Phone Number"] == delete_owners:
                del data[i]
            i += 1
        memory["data_for_owners"] = data
        with open("pet_store.json", "w") as file:
            json.dump(memory, file, indent=3)
