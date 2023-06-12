from flask import Flask, render_template, redirect, request, Blueprint

from repositories import manufacturer_repository, weapon_repository
from models.weapon import Weapon
from models.manufacturer import Manufacturer

weapons_blueprint = Blueprint("weapons", __name__)

@weapons_blueprint.route("/weapons")
def weapons():
    weapons = weapon_repository.select_all()