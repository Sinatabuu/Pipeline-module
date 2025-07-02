import joblib

model = joblib.load("models/model.pkl")
print(model.classes_)
