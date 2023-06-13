from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.weapon import Weapon

import repositories.manufacturer_repository as manufacturer_repository

def save(weapon):
    sql = "INSERT INTO weapons (name, description, weight, material, cost_to_buy, cost_to_sell, quantity, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [weapon.name, weapon.description, weapon.weight, weapon.material, weapon.cost_to_buy, weapon.cost_to_sell, weapon.quantity, weapon.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    weapon.id = id
    
    return weapon

def select_all():
    weapons = []

    sql = "SELECT * FROM weapons"
    results = run_sql(sql)
    # print(results)
    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        weapon = Weapon(row['name'],
                        manufacturer,
                        row['description'],
                        row['weight'],
                        row['material'],
                        row['cost_to_buy'],
                        row['cost_to_sell'],
                        row['quantity'],
                        row['id'])
        # print(weapon)
        # print(weapon.name)
        weapons.append(weapon)

    return weapons

def select(id):
    weapon = None
    sql = "SELECT * FROM weapons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        weapon = Weapon(result['name'],
                        manufacturer,
                        result['description'],
                        result['weight'],
                        result['material'],
                        result['cost_to_buy'],
                        result['cost_to_sell'],
                        result['quantity'],
                        result['id'])
    
    return weapon

def delete_all():
    sql = "DELETE FROM weapons"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM weapons WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(weapon):
    sql = "UPDATE weapons SET (name, description, weight, material, cost_to_buy, cost_to_sell, quantity, manufacturer_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [weapon.name, weapon.description, weapon.weight, weapon.material, weapon.cost_to_buy, weapon.cost_to_sell, weapon.quantity, weapon.manufacturer.id]
    run_sql(sql, values)

def weapons_from_manufacturer(manufacturer):
    weapons = []

    sql = "SELECT * FROM weapons WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        weapon = Weapon(row['name'],
                        manufacturer,
                        row['description'],
                        row['weight'],
                        row['material'],
                        row['cost_to_buy'],
                        row['cost_to_sell'],
                        row['quantity'],
                        row['id'])
        weapons.append(weapon)

    return weapons