import numpy as np 
import pandas as pd 

def main():
    df = pd.read_json('farmers-protest-tweets-2021-03-5.json',lines=True)