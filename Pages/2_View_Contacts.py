import os
import streamlit as st
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd

# Load environment variables
load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv('MONGO_URI')
CLIENT = MongoClient(MONGO_URI)

db = CLIENT["contacts_db"]
contacts_collec = db["contacts_collection"] 

# View Contacts from MongoDB
def get_data():
    items = list(contacts_collec.find())
    return items

# Retrieve the data
items = get_data()

# Convert the data to a Pandas DataFrame for better visualization and Handle data 
if items:
    df = pd.DataFrame(items)
    # Remove MongoDB's default '_id' field if you don't want to display it
    if '_id' in df.columns:
        df.drop('_id', axis=1, inplace=True)

    # {"country":"IN","countryCallingCode":"91","nationalNumber":"8755076866","number":"+918755076866","type":"PHONE_NUMBER_CHANGE"}

    # Extract the 'number' field from the JSON and replace the 'phone_number' column in the DataFrame
    df['phone'] = df['phone'].apply(lambda x: x['number'] if isinstance(x, dict) and 'number' in x else x)


    # Display the DataFrame
    st.write("### Contact List")
    st.dataframe(df)  # Display the DataFrame in Streamlit
else:
    st.write("No contacts found.")
