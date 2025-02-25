class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type. Must be one of: {self.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("The owner must be an instance of the Owner class.")
            self.owner = owner

        Pet.all.append(self)

    def __repr__(self):
            return f"Pet(name={self.name}, pet_type={self.pet_type})"


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a full list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Adds the owner to the pet, ensuring that the pet is of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("The object passed is not of type Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)
    

# Example usage:
owner1 = Owner("Sandra")
pet1 = Pet("Buddy", "dog", owner1)
pet2 = Pet("Whiskers", "cat", owner1)
pet3 = Pet("Polly", "bird")

# Add pet3 to owner1
owner1.add_pet(pet3)

# Get owner's pets and sorted list of pets
print(owner1.pets())  # Returns list of pets
print(owner1.get_sorted_pets())  # Returns sorted list of pets by name