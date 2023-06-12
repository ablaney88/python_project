from flask import Flask, render_template, redirect, request, Blueprint

from repositories import manufacturer_repository, weapon_repository
from models.weapon import Weapon

weapons_blueprint = Blueprint("weapons", __name__)

# GET '/weapons'

@weapons_blueprint.route("/weapons")
def weapons():
    weapons = weapon_repository.select_all()
    return render_template("weapons/index.html", all_weapons = weapons)

# NEW. GET '/weapons/new'

@weapons_blueprint.route("/weapons/new", methods=["GET"])
def new_weapon():
    manufacturers = manufacturer_repository.select_all()
    return render_template("weapons/new.html", all_manufacturers = manufacturers)

# CREATE. PST '/weapons'

@weapons_blueprint.route("/weapons", methods=["POST"])
def create_weapon():
    name = request.form["name"]
    description = request.form["description"]
    weight = request.form["weight"]
    material = request.form["material"]
    cost_to_buy = request.form["cost_to_buy"]
    cost_to_sell = request.form["cost_to_sell"]
    manufacturer_id = request.form["manufacturer_id"]

    manufacturer = manufacturer_repository.select(manufacturer_id)
    weapon = Weapon(name, description, weight, material, cost_to_buy, cost_to_sell, manufacturer)

    weapon_repository.save(weapon)
    return redirect('/weapons')

# EDIT. GET'/weapons/<id>/edit'

@weapons_blueprint.route("/weapons/<id>/edit", methods=['GET'])
def edit_task(id):
    weapon = weapon_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('weapons/edit.html', weapon = weapon, all_manufacturers = manufacturers)

# UPDATE. PUT '/weapons/<id>'

@weapons_blueprint.route("/weapons/<id>", methods=['POST'])
def update_weapon(id):
    name = request.form["name"]
    description = request.form["description"]
    weight = request.form["weight"]
    material = request.form["material"]
    cost_to_buy = request.form["cost_to_buy"]
    cost_to_sell = request.form["cost_to_sell"]
    manufacturer_id = request.form["manufacturer_id"]

    manufacturer = manufacturer_repository.select(manufacturer_id)
    weapon = Weapon(name, description, weight, material, cost_to_buy, cost_to_sell, manufacturer)

    weapon_repository.update(weapon)
    return redirect('/weapons')

# DELETE. DELETE '/weapons/<id>'

@weapons_blueprint.route("/weapons/<id>/delete", methods=['POST'])
def delete_weapon(id):
    weapon_repository.delete(id)
    return redirect('/weapons')

