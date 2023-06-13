from flask import Flask, render_template

from controllers.weapons_controller import weapons_blueprint
from controllers.manufacturers_controller import manufacturers_blueprint


app = Flask(__name__)

app.register_blueprint(weapons_blueprint, manufacturers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
