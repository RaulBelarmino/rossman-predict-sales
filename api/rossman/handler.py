import pandas as pd
import pickle
from flask           import Flask, request, Response
import Rossman

# Loading model

model = pickle.load(open('C:/Users/Arbo/repos/my_git/rossman-predict-sales/model/model_rossman.pkl', 'rb'))

app = Flask(__name__)

#Método post, o usuário envia dados para receber outros
#Método Get, osuário solicita algo para receber

@app.route('/rossman/predict', methods=['POST'])
def rossman_predict():
    test_json = request.get_json()
    
    if test_json: #há dados?
        if isinstance(test_json, dict): #Unique data
            test_raw = pd.DataFrame(test_jason, index=[0])
        
        else: #Multi data
            test_raw = pd.DataFrame(test_json, columns=test_jason[0].keys())
    
        # Instantiate Rossman Class
        pipeline = Rossman()

        # Data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # Feature engineering
        df2 = pipeline.feature_engineering(df1) 

        # Data preparation
        df3 = pipeline.data_preparation(df2)

        #Prediction
        df_response = pipeline.get_prediction(model, df3, test_raw)
    
        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')

    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)