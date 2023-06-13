from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.weapon import Weapon

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, description, year_founded) VALUES (%s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.description, manufacturer.year_founded]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'],
                                     row['description'],
                                     row['year_founded'],
                                     row['id'])
        manufacturers.append(manufacturer)
    
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'],
                                     result['description'],
                                     result['year_founded'],
                                     result['id'])
    
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, description, year_founded) = (%s, %s, %s) WHERE id = %s" 

