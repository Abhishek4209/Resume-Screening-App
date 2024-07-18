import numpy as np
import pandas as pd
import os 
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import save_objects
from dataclasses import dataclass



## Model Training Config:
@dataclass
class ModelTrainerConfig():
    trained_model_file_path=os.path.join('artifacts','model.pkl')
    
## Model Training Class:
class ModelTrainer():
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    def intiate_model_training(self,train_arr,test_arr)