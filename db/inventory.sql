DROP TABLE IF EXISTS weapons;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    year_founded VARCHAR(255)

);

CREATE TABLE weapons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    weight INT,
    material VARCHAR(255),
    cost_to_buy INT,
    cost_to_sell INT,
    quantity INT,
    manufacturer_id INT NOT NULL REFERENCES manufacturers(id)
);

INSERT INTO manufacturers (name, description, year_founded) VALUES ('Adeptus Mechanicus', 'Producer of arms for the Imperium', 'M25');
-- INSERT INTO manufacturers (name, description, year_founded) VALUES ('Telchar', 'Dwarven smith', 'First Age');

INSERT INTO weapons (name, description, weight, material, cost_to_buy, cost_to_sell, quantity, manufacturer_id) VALUES ('Boltgun', 'Big gun for killing xenos', 35, 'Steel', 300, 500, 10, 1);

-- INSERT INTO weapons (name, description, weight, material, cost_to_buy, cost_to_sell, manufacturer_id) VALUES ('Nasir', 'Saurons worst nightmare', 2, 'Steel', 1000, 3000, 1);