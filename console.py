from models.manufacturer import Manufacturer
from models.weapon import Weapon

import repositories.manufacturer_repository as manufacturer_repository
import repositories.weapon_repository as weapon_repository

weapon_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer("Adeptus Mechanicus", "Producer of arms for the Astartes", "M25")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("Amethal: Forge World", "Producer of arms for the Imperium", "M25")
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer("Deimos: Forge World", "Producer of arms for the Imperium", "M25")
manufacturer_repository.save(manufacturer3)

manufacturer4 = Manufacturer("Adeptus Mechanicus", "Producer of arms for the Astartes", "M25")
manufacturer_repository.save(manufacturer4)

manufacturer5 = Manufacturer("Adeptus Mechanicus", "Producer of arms for the Astartes", "M25")
manufacturer_repository.save(manufacturer5)

weapon1 = Weapon("Boltgun", manufacturer1, "Big gun kills xenos", 35, "Steel", 300, 500, 2)
weapon_repository.save(weapon1)

weapon2 = Weapon("Lasgun", manufacturer2, "Pew Pew Pew", 2, "Steel", 100, 200, 300)
weapon_repository.save(weapon2)

weapon3 = Weapon("Chainsword", manufacturer3, "Chainsaw + Sword", 15, "Steel", 250, 400, 125)
weapon_repository.save(weapon3)

weapon4 = Weapon("Thunder Hammer", manufacturer4, "Hammer go smash", 150, "Steel", 1500, 4000, 10)
weapon_repository.save(weapon4)

weapon5 = Weapon("Plasma Pistol", manufacturer5, "Melt youre enemies", 6, "Steel", 800, 1400, 25)
weapon_repository.save(weapon5)

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