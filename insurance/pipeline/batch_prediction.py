from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.predictor import ModelResolver
from insurance.utils import load_object
import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime

PREDICTION_DIR = "prediction"


def start_batch_prediction(input_file_path):
    try:
        os.makedirs(PREDICTION_DIR, exist_ok=True)
        logging.info(f"Creating model resolver object")
        model_resolver = ModelResolver(model_registry="saved_models")
        logging.info(f"Reading file :{input_file_path}")
        df = pd.read_csv(input_file_path)
        df.replace({"na": np.NAN}, inplace=True)
        
        
        logging.info(f"Loading transformer to transform dataset")
        transformer = load_object(file_path=model_resolver.get_latest_transformer_path())

        logging.info(f"Target encoder to convert predicted column into categorical")
        target_encoder = load_object(file_path=model_resolver.get_latest_target_encoder_path())

        # Encoding the categorical variables
        input_feature_names = list(transformer.feature_names_in_)
        for i in input_feature_names:       
            if df[i].dtypes =='object':
                df[i] =target_encoder.fit_transform(df[i])  
              
        # transformed data      
        input_arr = transformer.transform(df[input_feature_names])

        logging.info(f"Loading model to make prediction")
        model = load_object(file_path=model_resolver.get_latest_model_path())
        
        # Making prediction
        prediction = model.predict(input_arr)
    
        # Storing our prediction as prediction column into the file
        df["prediction"]=prediction

        # Storing our prediction into prediction folder
        prediction_file_name = os.path.basename(input_file_path).replace(".csv",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
        prediction_file_path = os.path.join(PREDICTION_DIR,prediction_file_name)
        df.to_csv(prediction_file_path,index=False,header=True)
        
        return prediction_file_path
    
    except Exception as e:
        raise InsuranceException(e, sys)