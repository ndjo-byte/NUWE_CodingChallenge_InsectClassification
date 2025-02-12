import pickle
import pandas as pd
from data_processing import insect_load, insect_preprocessing
import json

def predict():

    with open('/Users/nathanjones/Downloads/NUWE/CodingChallenges/Insect_Classification/repo_insect_classification/nuwe-data-ml1/models/rfc_model.pkl', "rb") as f:
        model = pickle.load(f)

    _, test = insect_load()
    X_test = insect_preprocessing(test)
    features = ['hour_sin', 'hour_cos', 'Sensor_beta', 'Sensor_gamma', 'Sensor_alpha_plus']
    X_test = X_test[features]

    predictions = model.predict(X_test)

    predictions_df = pd.DataFrame({'test_id': test['Unnamed: 0'], 'target': predictions})

    final_predictions = predictions_df.groupby('test_id')['target'].agg(lambda x: x.mode()[0])

    output = {'target':final_predictions.to_dict()}

    with open('/Users/nathanjones/Downloads/NUWE/CodingChallenges/Insect_Classification/repo_insect_classification/nuwe-data-ml1/predictions/predictions.json', 'w') as json_file:
        json.dump(output, json_file, indent=4)

    print("Predictions saved to 'predictions/predictions.json'")


if __name__ == "__main__":
    predict()


