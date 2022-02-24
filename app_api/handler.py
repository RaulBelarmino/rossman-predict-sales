import os
import pandas as pd
import pickle
from flask           import Flask, request, Response
from rossman.Rossman import Rossman

# Loading model

model = pickle.load(open('model/model_rossman.pkl', 'rb'))

app = Flask(__name__)

#Método post, o usuário envia dados para receber outros
#Método Get, osuário solicita algo para receber

@app.route('/rossman/predict', methods=['POST'])
def rossman_predict():
    test_json = request.get_json()
    
    if test_json: #há dados?
        if isinstance(test_json, dict): #Unique data
            test_raw = pd.DataFrame(test_json, index=[0])
        
        else: #Multi data
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
    
        # Instantiate Rossman Class
        pipeline = Rossman()

        # Data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # Feature engineering
        df2 = pipeline.feature_engineering(df1) 

        # Data preparation
        df3 = pipeline.data_preparation(df2)

        #Prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)
    
        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')

    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
