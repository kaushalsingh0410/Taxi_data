print('Ritu')
from flask import Flask,render_template,request
from datetime import datetime
from geopy.distance import geodesic
import joblib
app = Flask(__name__)

model = joblib.load('final_model.pkl')
scaler = joblib.load('scaler.pkl')



@app.route("/")
def index():
    return render_template('index.html',fare = '$0.0')

@app.route('/predict',methods = ('POST','GET'))
def predict():
    if request.method == "POST":
        pickup_datetime = request.form['pickup_datetime']
        pickup_longitude = float(request.form['pickup_longitude'])
        pickup_latitude = float(request.form['pickup_latitude'])
        dropoff_longitude = float(request.form['dropoff_longitude'])
        dropoff_latitude = float(request.form['dropoff_latitude'])
        passenger_count = int(request.form['passenger_count'])

        pickup_datetime = datetime.strptime(pickup_datetime,'%Y-%m-%dT%H:%M')
        
        year = pickup_datetime.year
        month = pickup_datetime.month
        day = pickup_datetime.day
        hour = pickup_datetime.hour
        minute = pickup_datetime.minute
        second = pickup_datetime.second

        distance = geodesic((pickup_latitude,pickup_longitude),(dropoff_latitude,dropoff_longitude)).miles

        X = scaler.transform([[pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,passenger_count,distance,year,month,day,hour,minute,second]])

        

        
       
        return render_template('index.html',fare =f'${round(model.predict(X)[0],2)}' )
    return render_template('index.html',fare =f'$0.0' )




if __name__ == '__main__':
    app.run(debug = True)