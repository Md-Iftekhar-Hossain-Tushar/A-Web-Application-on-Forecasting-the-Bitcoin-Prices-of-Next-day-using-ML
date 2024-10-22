from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the pickled model
with open('Close_LinearR.pkl', 'rb') as Close_model_file:
    Close_model = pickle.load(Close_model_file)
with open('Open_LinearR.pkl', 'rb') as Open_model_file:
    Open_model = pickle.load(Open_model_file)
with open('Low_LinearR.pkl', 'rb') as Low_model_file:
    Low_model = pickle.load(Low_model_file)
with open('High_LinearR.pkl', 'rb') as High_model_file:
    High_model = pickle.load(High_model_file)

    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_prices', methods=['POST'])
def predict_fraud(): 
        if request.method =='POST':
            Close1 = float(request.form.get('Close1'))
            Open1 = float(request.form.get('Open1'))
            Low1 = float(request.form.get('Low1'))
            High1 = float(request.form.get('High1'))

            Close2 = float(request.form.get('Close2'))
            Open2 = float(request.form.get('Open2'))
            Low2= float(request.form.get('Low2'))
            High2 = float(request.form.get('High2'))

            Close3 = float(request.form.get('Close3'))
            Open3 = float(request.form.get('Open3'))
            Low3 = float(request.form.get('Low3'))
            High3 = float(request.form.get('High3'))
        
   
        Close_prediction_arr = Close_model.predict([[Close1,Close2,Close3]])
        Open_prediction_arr = Open_model.predict([[Open1,Open2,Open3]])
        Low_prediction_arr = Low_model.predict([[Low1,Low2,Low3]])
        High_prediction_arr = High_model.predict([[Close1,Close2,Close3]])


        # Return the prediction result
        
        return render_template('/predict.html', 
                                Close_Prediction = "{:.6f}".format(Close_prediction_arr[0]),
                                Open_Prediction = "{:.6f}".format(Open_prediction_arr[0]),
                                Low_Prediction = "{:.6f}".format(Low_prediction_arr[0]),
                                High_Prediction = "{:.6f}".format(High_prediction_arr[0]), )
   
if __name__ == '__main__':
    app.run(debug=True)