import pandas as pd 
import numpy as np

def insect_load():
    train = pd.read_csv('/Users/nathanjones/Downloads/NUWE/CodingChallenges/Insect_Classification/repo_insect_classification/nuwe-data-ml1/data/train.csv')
    test = pd.read_csv('/Users/nathanjones/Downloads/NUWE/CodingChallenges/Insect_Classification/repo_insect_classification/nuwe-data-ml1/data/test.csv')
    print('load complete')
    return train, test

def insect_preprocessing(df):
    df.fillna(df.median(), inplace=True)
    df["hour_sin"] = np.sin(2 * np.pi * df["Hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["Hour"] / 24)
    print('prepocessing complete')
    return df 


if __name__ == "__main__":
    train, test = insect_load()
    train = insect_preprocessing(train)
    test = insect_preprocessing(test)
    print("Data processing complete")

    
