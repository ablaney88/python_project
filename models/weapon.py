class Weapon:

    def __init__(self, name, manufacturer, description, weight, material, cost_to_buy, cost_to_sell, id = None):
        self.name = name
        self.manufacturer = manufacturer
        self.description = description
        self.weight = weight
        self.material = material
        self.cost_to_buy = cost_to_buy
        self.cost_to_sell = cost_to_sell
        self.id = id