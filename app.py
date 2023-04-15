import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.neural_network import MLPClassifier

st.set_page_config(
    page_title="Breast Cancer Prediction",
    initial_sidebar_state="expanded"
)

MODEL_PATH = ('data/model.pkl')
characteristics = ['Radious Mean','Texture Mean','Perimeter Mean','Area Mean','Smoothness Mean',
            'Compactness Mean','Concavity Mean','Concave Points Mean','Simetry Mean','Fractal Dimension Mean',
            'Radious SE','Texture SE','Perimeter SE','Area SE','smoothness SE',
            'Compactness SE','Concavity SE','Concave Points SE','Simetry SE','Fractal Dimension SE',
            'Radious Worst','Texture Worst','Perimeter Worst','Area Worst','Smoothness Worst',
            'Compactness Worst','Concavity Worst','Concave Points Worst','Simetry Worst','Fractal Dimension Worst']

variables_independient = []
values = []

# def load_model():
#     """
#     load the trained model file
#     """

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

def variable_input(data):
    """Description variable_input function
    Arg:
        arg1(array):name of the independent variables
    """
    for name in data:
        
        new_name = name.lower().replace(" ","_")
        number_input = st.number_input(f"{name}")
        variable_result = f"{new_name}={number_input}"
        variables_independient.append(variable_result)
    return variables_independient

def model_prediction(x_pred, mod):
    """Description model_prediction function
    Args:
        arg1():predicted values
        arg2():ML model train
    """
    y_pred = np.asarray(x_pred).reshape(1,-1)
    prediction = mod.predict(y_pred)
    return prediction

def get_values():
    """
    gets the value of the input of the characteristics
    """
    for variable in variables_independient:
        value = variable.split("=")
        num = float(value[1])
        values.append(num)

def pred_btn():
    """Description pred_btn function
    """
    if st.button('Prediccion'):
        get_values()
        prediction = model_prediction(values,model)
        if prediction[0] == 'B':
            # st.success(f"La prediccion para este caso es: {prediction[0]}")
            st.success("La prediccion para este caso es: Benigna")
            st.balloons()
        else:
            st.success("La prediccion para este caso es: Maligna")
def main():
    """
    Main function running the breast cancer prediction application.
    """
    st.title('Breast Cancer Prediction')
    #load trained model
    # load_model()
    #data readout
    data = characteristics
    variable_input(data)
    #prediction button
    pred_btn()

if __name__ == '__main__':
    main()
