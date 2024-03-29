from flask  import Flask, render_template, request
from statsmodels.tsa.ar_model import AutoRegResults
import numpy as np
from datetime import datetime

app = Flask(__name__)

model = AutoRegResults.load('model_ar_engineoil.pb')
start = 497 # train size
end =  500 # len(engineoil_df_train)+9


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        days = int(request.form['days'])
        #date = datetime.strptime(request.form['date'],'%Y-%m-%d')
        if days!=None:
            forecast_ = model.forecast(days)
            list_ = forecast_.to_list()
            prediction = list(map(round, list_))
        #if date!=None:
            #pred_loaded_model = model.predict(start=len(engineoil_df_train), end=len(engineoil_df_train)+9, dynamic=False)
            
        return render_template('index.html',pred=prediction)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port='8000')

