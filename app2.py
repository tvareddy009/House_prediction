import pandas as pd
import numpy as np
import pickle
import streamlit as st

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))
df['total_sqft']=df['total_sqft'].astype(int)
df['bath']=df['bath'].astype(int)
df['price']=df['price'].astype(int)
df['BHK']=df['BHK'].astype(int)

location = st.text_input('Enter the location')
BHK = st.text_input('Enter the number of bedrooms')
bath = st.text_input('Enter the number of bathrooms')
total_sqft = st.text_input('Enter the total square feet area')
price = st.text_input('Enter the price')




if st.button('Predict Price'):
    
    query_df = pd.DataFrame({
        'location': [location],
        'total_sqft': [total_sqft],
        'bath': [bath],
        'price':[price],
        'BHK': [BHK]
        
        
       
    })

   
    print("Query DataFrame columns:", query_df.columns)

    prediction = pipe.predict(query_df)
    st.write(f"The predicted price is: {prediction}")
