DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS weapons;

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
    weight VARCHAR(255),
    material VARCHAR(255),
    cost_to_buy INT,
    cost_to_sell INT,
    weapon_id INT NOT NULL REFERENCES weapons(id) ON DELETE CASCADE
);