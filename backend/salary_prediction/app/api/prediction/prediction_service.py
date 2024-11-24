from configuration.config import get_model,Depends

def prediction_service(args):
    age, exp, model = args
    if model is not None:
        prediction = model.predict([[age, exp]])
    else:
        return "Model is not loaded"
    return prediction[0]
