import pandas as pd 
import numpy as np 
import pickle as pk 
import streamlit as st

model = pk.load(open('model.pkl','rb'))

st.header('Car Price Prediction')

df = pd.read_csv('Pricing.csv')

def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()
df['Make'] = df['Make'].apply(get_brand_name)

Make = st.selectbox('Select Car Brand', df['Make'].unique())
Year = st.slider('Car Manufactured Year', 1900,2024)
Kilometers_Driven = st.slider('No of kms Driven', 11,200000)
Rarity = st.selectbox('Rarity', df['Rarity'].unique())
Condition_Category = st.selectbox('Condition of the Car', df['Condition_Category'].unique())
Selling_Price = st.slider('Selling_Price', 0,1000)



if st.button("Predict"):
    input_data_model = pd.DataFrame(
    [[Make, Year, Rarity, Condition_Category, Selling_Price, Kilometers_Driven]],
    columns=['Make', 'Year', 'Rarity', 'Condition_Category', 'Selling_Price', 'Kilometers_Driven'])
    
    input_data_model['Rarity'].replace(['Common', 'Rare', 'Uncommon', 'Very Rare', 'Very Common'], [1,2,3,4,5], inplace=True)
    input_data_model['Condition_Category'].replace(['Good', 'Excellent', 'Very Good', 'Poor'], [1,2,3,4], inplace=True)

    input_data_model['Make'].replace(['Ford', 'Mercer', 'Cadillac', 'Stutz', 'Dodge', 'Packard',
       'Hudson', 'Chevrolet', 'Pierce-Arrow', 'Rolls', 'Bentley',
       'Lincoln', 'Bugatti', 'Chrysler', 'Alfa Romeo', 'Mercedes-Benz',
       'Auburn', 'Cord', 'Duesenberg', 'BMW', 'Willys', 'Tucker',
       'Ferrari', 'Jaguar', 'Mercury', 'Oldsmobile', 'Mercedes',
       'Porsche', 'Austin', 'Alfa', 'Aston', 'Buick', 'Pontiac', 'Honda',
       'Fiat', 'Volkswagen', 'Plymouth', 'Citroen', 'Lamborghini',
       'Lancia', 'De', 'Renault', 'Datsun', 'Triumph', 'Maserati', 'AMC',
       'Lada', 'Lotus', 'DeLorean', 'Jeep', 'Nissan', 'Land', 'Peugeot',
       'McLaren', 'Toyota', 'Mazda', 'Mini', 'Subaru', 'Saab', 'Audi',
       'Lexus', 'Volvo', 'Dacia'], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64], inplace=True)

    car_price = model.predict(input_data_model)

    st.markdown('Car Price is going to be '+ str(car_price[0]))