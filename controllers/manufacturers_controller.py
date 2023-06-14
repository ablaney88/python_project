from flask import Flask, render_template, redirect, request, Blueprint

from repositories import manufacturer_repository, weapon_repository
from models.manufacturer import Manufacturer

manufacturers_blueprint = Blueprint("manufacturers", __name__)

# GET manufacturers

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()

    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

# EDIT manufacturer. 

@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    print("here")
    manufacturer = manufacturer_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/edit.html', manufacturer = manufacturer, all_manufacturers = manufacturers)

# Create manufacturer

@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]
    description = request.form["description"]
    year_founded = request.form["year_founded"]
 
    manufacturer = Manufacturer(name, description, year_founded)

    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

# UPDATE manufacturer

@manufacturers_blueprint.route("/manufacturers/<id>", methods=["POST"])
def update_manufacturer(id):
    name = request.form["name"]
    description = request.form["description"]
    year_founded = request.form["year_founded"]
 
    manufacturer = Manufacturer(name, description, year_founded, id)

    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')

# DELETE manufacturer

@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    weapon_repository.delete(id)
    return redirect('/manufacturers')

