from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Hacer la solicitud a la API
    api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        drinks = data.get('drinks', [])
        drink_info = [{'name': drink['strDrink'], 'category': drink['strCategory'], 'id': drink['idDrink']} for drink in drinks]
    else:
        drink_info = []

    return render_template('index.html', drink_info=drink_info)

@app.route('/detalle/<drink_id>')
def detalle(drink_id):
    api_url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        drink = data.get('drinks', [])[0]
    else:
        return render_template('error.html', message='No se pudo obtener la información de la bebida.')
    return render_template('detalle_drink.html', drink=drink)

if __name__ == '__main__':
    app.run(port=7000, host="0.0.0.0",debug=True)

