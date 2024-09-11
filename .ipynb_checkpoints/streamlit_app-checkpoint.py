import streamlit as st
import tensorflow as tf
from tf.keras.models import load_model # type: ignore



def predict(inputs, model_path="churn_model.h5"):
    try:
        model = load_model(model_path)
        pred = model.predict(inputs)

        return pred
    
    except Exception as e:
        print(f"Error loading model: {e}")
    

def main():
    st.title('Customer Churn')

    # Get user input
    CreditScore = st.number_input('Credit Score', min_value=0, max_value=1000)
    Age = st.number_input('Age', min_value=18, max_value=150)
    Tenure = st.number_input('Tenure', min_value=0, max_value=50)
    Balance = st.number_input('Balance', min_value=0)
    NumOfProducts = st.number_input('NumOfProducts', min_value=1, max_value=10)
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    Geography = st.selectbox('Geography', ['France', 'Spain', 'Germany'])
    HasCrCard = st.selectbox('Has Credit Card', ['Yes', 'No'])
    IsActiveMember = st.selectbox('Is Active Member', ['Yes', 'No'])
    EstimatedSalary = st.number_input('Estimated Salary', min_value=100)

    if Gender == "Male":
        Gender = [0]
    else:
        Gender = [1]

    if HasCrCard == "Yes":
        HasCrCard = 0
    else:
        HasCrCard = 1

    if IsActiveMember == "Yes":
        IsActiveMember = 0
    else:
        IsActiveMember = 1

    if Geography == "France":
        geography = [0, 0]
    elif Geography == "Spain":
        geography = [0, 1]
    else:
        geography = [1, 0]

    inputs = [CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]
    inputs_1 = geography + Gender # [1, 0, 0]
    
    inputs.append(inputs_1)
    

    if st.button("Predict"):
        pred = predict([inputs])

        if pred == 1:
            st.write("The customer will exit")
        else:
            st.write("The customer will not exit")


if __name__ == "__main__":
    main()
    
    