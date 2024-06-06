from flask import Flask, render_template, request , jsonify
from models.crop_recommendation_model import crop_recommendation
from models.fertilizer_recommendation_model import fertilizer_recommendation
from models.yield_prediction_model import yield_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop', methods=['GET', 'POST'])
def crop():
    if request.method == 'POST':
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        rainfall = float(request.form['rainfall'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        
        input_data = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
        common_crop = crop_recommendation(input_data)
        
        return render_template('crop_result.html', crop=common_crop)
    
    return render_template('crop.html')

@app.route('/fertilizer', methods=['GET', 'POST'])
def fertilizer():
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        soil_moisture = float(request.form['soil_moisture'])
        soil_type = request.form['soil_type']
        crop_type = request.form['crop_type']
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        input_data1 = [temperature, humidity, soil_moisture, soil_type, crop_type, nitrogen, phosphorus, potassium]
        fertilizer_name = fertilizer_recommendation(input_data1)
        
        return render_template('fertilizer_result.html', fertilizer=fertilizer_name)
    
    return render_template('fertilizer.html')


@app.route('/yield', methods=['GET', 'POST'])
def yield_p():
    if request.method == 'POST':
        district = request.form['district']
        season = request.form['season']
        crops = request.form['crops']
        area = float(request.form['area'])

        input_data = (district, season, crops, area)
        prediction = yield_prediction(input_data)

        return render_template('yield_prediction_result.html', prediction=prediction)
    
    return render_template('yield.html')


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        api_key = "48de5b3d4db0b2bc53677b5c59b392ee"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}appid={api_key}&q={city}"
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main_data = data["main"]
            temperature = main_data["temp"] - 273.15
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]

            weather_data = data["weather"]
            weather_description = weather_data[0]["description"]

            return render_template('weather.html', city=city, temperature=temperature, pressure=pressure,
                                   humidity=humidity, weather_description=weather_description)
        else:
            return "City not found."

    return render_template('weather.html')
    

if __name__ == '__main__':
    app.run(debug=True)
