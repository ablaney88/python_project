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

manufacturer_repository.select_all()

weapon1 = Weapon("Boltgun", "Big gun kills xenos", 35, "Steel", "£300", "£500", manufacturer1)
weapon_repository.save(weapon1)

weapon2 = Weapon("Nasir", "Sauron's worst nightmare", 2, "Steel", "£1000", "£3000", manufacturer2)
weapon_repository.save(weapon2)
