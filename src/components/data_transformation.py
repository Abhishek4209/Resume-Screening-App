import numpy as np
import pandas as pd
import os
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler,MinMaxScaler, RobustScaler
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass

## Data Transformation Config:
@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')
    
## Data Transformation class:
class DataTransformation():
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def get_data_transformation_object(self):
        try:
            logging.info('Data transformation Intiated')
            
            numeric_features=[]
            categorical_features=[]
            
            logging.info('Pipeline Initiated')
            
            preprocessor=ColumnTransformer(
                transformers=[
                    ('trf1',OneHotEncoder(sparse_output=False,handle_unknown='ignore'),categorical_features),
                    ('trf2',StandardScaler(),numeric_features),
                            ],remainder='passthrough'
                )
            return preprocessor
            logging.info('pipeline Completed')
            
        
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error Occured into Data Transformation  Class')
            
    def intiate_data_transformation(self,train_path,test_path):
        try:
            ## Reading train and test data
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info('Read train and test data Completed')
            logging.info(f"Train Dataframe Head : \n{train_df.head().to_string()}")
            logging.info(f"Test Dataframe Head : \n{test_df.head().to_string()}")
        

            logging.info("Obtaing preprocessing object")
            
            
            preprocessor_obj=self.get_data_transformation_object()
            
            
            target_column_name=''
            drop_columns=[target_column_name]
            
            input_feature_train_df=train_df.drop(drop_columns)









        
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error occure into Intiation of Data Transformation Class')
            