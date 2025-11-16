
import joblib

def save_model(model, filepath='models/titanic_model.pkl'):
    joblib.dump(model, filepath)
    print(f"Model saved at {filepath}")

def load_model(filepath='models/titanic_model.pkl'):

    model = joblib.load(filepath)
    print(f"Model loaded from {filepath}")
    return model
