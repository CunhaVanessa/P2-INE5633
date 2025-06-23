import joblib


def load_model():
    model = joblib.load('outputs/modelo_mlp.pkl')
    return model
