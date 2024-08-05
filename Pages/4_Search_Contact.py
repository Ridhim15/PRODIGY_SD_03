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

# Function to search contacts
def search_contacts(query):
    results = list(contacts_collec.find({"name": {"$regex": query, "$options": "i"}}))
    return results

# Streamlit UI
st.write("## Search Contacts")
search_query = st.text_input("Enter a name or part of a name to search:")

if st.button("Search"):
    if search_query:
        search_results = search_contacts(search_query)
        if search_results:
            df_results = pd.DataFrame(search_results)
            if '_id' in df_results.columns:
                df_results.drop('_id', axis=1, inplace=True)
            st.write("### Search Results")
            st.dataframe(df_results)
        else:
            st.write("No contacts found.")
    else:
        st.error("Please enter a search query.")
