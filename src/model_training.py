import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from data_processing import insect_load, insect_preprocessing 

def train_model():
    train, _ = insect_load()
    train = insect_preprocessing(train)  

    features = ['hour_sin', 'hour_cos', 'Sensor_beta', 'Sensor_gamma', 'Sensor_alpha_plus']
    X = train[features]
    y = train['Insect']
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.15, random_state=24, stratify=y)
    rfc_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rfc_model.fit(train_X, train_y)

    y_pred = rfc_model.predict(test_X)  
    print(f"Validation F1 Score: {f1_score(test_y, y_pred, average='weighted'):.4f}") 

    with open("/Users/nathanjones/Downloads/NUWE/CodingChallenges/Insect_Classification/repo_insect_classification/nuwe-data-ml1/models/rfc_model.pkl", "wb") as f:
        pickle.dump(rfc_model, f)


if __name__ == "__main__":
    train_model()

