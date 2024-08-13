from flask import Flask, render_template, request, redirect, url_for

from classes.owner import Owner
from classes.pet import Pet
from memory_provider import MemoryProvider
from utilities import Utilities

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/owners")
def owners():
    memory = MemoryProvider.load_data_owners()
    owners = memory["data_for_owners"]
    return render_template("owners.html", owners=owners)


@app.route("/add_owner", methods=["POST", "GET"])
def add_owner():
    if request.method == 'POST':
        owner_name = request.form.get("owner_name")
        owner_phone_number = request.form.get("owner_phone_number")

        MemoryProvider.save_data_owners(Utilities.owners_return_in_json(owner_name, owner_phone_number))

        return redirect(url_for('owners'))

    return render_template("add_owner.html")


@app.route("/pets")
def pets():
    memory = MemoryProvider.load_data_pets()
    pets = memory["data_for_pets"]
    return render_template("pets.html", pets=pets)


@app.route("/add_pet", methods=["POST", "GET"])
def add_pet():
    if request.method == 'POST':
        pet_name = request.form.get("pet_name")
        species = request.form.get("species")
        age = request.form.get("age")
        vaccinated = request.form.get("vaccinated")
        owner_name = request.form.get("owner_name")
        owner_phone_number = request.form.get("owner_phone_number")

        my_owner = Owner(owner_name, owner_phone_number)
        new_pet = Pet(pet_name, species, age, vaccinated, my_owner)

        MemoryProvider.save_data_pets(Utilities.pets_return_in_json(new_pet))

        return redirect(url_for('pets'))
    pets_species = ['Rabbit', 'Bird', 'Cat', 'Dog', 'Rat', 'Horse', 'Tortoise', 'Duck', 'Snake']
    return render_template("add_pet.html", pets_species=pets_species)


@app.route("/services")
def services():
    return render_template("services.html")


if __name__ == "__main__":
    app.run(debug=True)
