import pdb
from models.manufacturer import Manufacturer
from models.weapon import Weapon

import repositories.manufacturer_repository as manufacturer_repository
import repositories.weapon_repository as weapon_repository

manufacturer_repository.delete_all()
weapon_repository.delete_all()