from models.manufacturer import Manufacturer
from models.weapon import Weapon

import repositories.manufacturer_repository as manufacturer_repository
import repositories.weapon_repository as weapon_repository

weapon_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer("Adeptus Mechanicus", "Producer of arms for the Imperium", "M25")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("Telchar", "Dwarven smith", "First Age")
manufacturer_repository.save(manufacturer2)



weapon1 = Weapon("Boltgun", manufacturer1, "Big gun kills xenos", 35, "Steel", 300, 500, 2)
weapon_repository.save(weapon1)

weapon2 = Weapon("Nasir", manufacturer2, "Sauron's worst nightmare", 2, "Steel", 1000, 3000, 8)
weapon_repository.save(weapon2)

# weapon1.name ="abc"
# manufacturer1.name = "abc"
# manufacturer_repository.update(manufacturer1)

# weapon_repository.update(weapon1)

# manufacturer_repository.delete(manufacturer1.id)
# weapon_repository.delete(weapon2.id)

# print(manufacturer_repository.select_all())
# print(weapon_repository.select_all())

# print(manufacturer_repository.select(manufacturer1.id).name)
# print(weapon_repository.select(weapon2.id).name)